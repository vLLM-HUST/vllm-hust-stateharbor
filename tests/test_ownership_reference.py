import pytest

from vllm_hust_stateharbor.ownership import (
    AttentionLeaseManager,
    EpochFenceError,
    OwnerAssignmentObservation,
    OwnerLeaseCoordinator,
    OwnerLeaseKey,
)


def key(request_id: str = "request-0", epoch: int = 0) -> OwnerLeaseKey:
    return OwnerLeaseKey(request_id, epoch)


def test_assignment_is_deterministic_and_charges_projected_work() -> None:
    coordinator = OwnerLeaseCoordinator()
    coordinator.observe(OwnerAssignmentObservation(0, 1, work=20))
    coordinator.observe(OwnerAssignmentObservation(1, 1, work=5))

    assert coordinator.assign(key(), required_num_tokens=8) == 1
    assert coordinator.assign(key(), required_num_tokens=999) == 1
    assert coordinator.assign(key("request-1"), required_num_tokens=8) == 1
    assert coordinator.assign(key("request-2"), required_num_tokens=8) == 0


def test_reserve_receipt_and_publication_round_trip() -> None:
    coordinator = OwnerLeaseCoordinator()
    coordinator.observe(OwnerAssignmentObservation(0, 1))
    lease_key = key()
    coordinator.assign(lease_key, required_num_tokens=4)
    manager = AttentionLeaseManager(owner_rank=0, capacity=8)

    command = coordinator.reserve(lease_key, 4)
    receipt = manager.apply(command)
    assert receipt.accepted
    assert coordinator.apply_receipt(receipt)

    tokens = coordinator.publish(step_seq=1)
    assert len(tokens) == 1
    assert tokens[0].runnable_num_tokens == 4
    manager.record_published(tokens[0])
    assert manager.published_num_tokens(lease_key) == 4


def test_request_id_reuse_fails_closed_for_stale_epoch() -> None:
    coordinator = OwnerLeaseCoordinator()
    coordinator.observe(OwnerAssignmentObservation(0, 1))
    coordinator.assign(key(epoch=2))

    with pytest.raises(EpochFenceError):
        coordinator.assign(key(epoch=1))


def test_wrong_owner_receipt_is_rejected_without_state_change() -> None:
    coordinator = OwnerLeaseCoordinator()
    coordinator.observe(OwnerAssignmentObservation(0, 1))
    lease_key = key()
    coordinator.assign(lease_key)
    command = coordinator.reserve(lease_key, 1)

    receipt = AttentionLeaseManager(owner_rank=1, capacity=4).apply(command)
    assert not receipt.accepted
    assert receipt.error == "wrong owner rank"
    assert not coordinator.apply_receipt(receipt)
