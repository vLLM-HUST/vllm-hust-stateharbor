"""Import-only StateHarbor contracts and reference policy implementation."""

from .ownership import (
    AttentionLeaseManager,
    OwnerAssignmentObservation,
    OwnerLeaseCoordinator,
    OwnerLeaseKey,
)

__all__ = [
    "AttentionLeaseManager",
    "OwnerAssignmentObservation",
    "OwnerLeaseCoordinator",
    "OwnerLeaseKey",
    "StateHarborDescriptor",
]


class StateHarborDescriptor:
    """Metadata anchor; importing the package installs no runtime hooks."""

    extension_id = "org.vllm-hust.stateharbor"
    activation_status = "import_only"
