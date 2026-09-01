# Provenance

Immutable source archives:

- [intellistream/vllm-hust-legacy-20260831](https://github.com/intellistream/vllm-hust-legacy-20260831)
- [intellistream/vllm-ascend-hust-legacy-20260831](https://github.com/intellistream/vllm-ascend-hust-legacy-20260831)

Primary history:

- [Core PR #253: integrate the StateHarbor request-owned runtime](https://github.com/intellistream/vllm-hust-legacy-20260831/pull/253)
- [Core PR #239: request-owned linear DSpark verification](https://github.com/intellistream/vllm-hust-legacy-20260831/pull/239)

Migrated from PR #253:

| Legacy path | New path | Scope |
| --- | --- | --- |
| `vllm/v1/core/sched/ownership.py` | `src/vllm_hust_stateharbor/ownership.py` | Dependency-neutral protocol types and reference coordinator/worker state machines |
| `vllm/v1/core/sched/owner_window_policy.py` | `src/vllm_hust_stateharbor/window_policy.py` | Receipt-driven decode/prefill window policy; import rewritten only to the package-local protocol |
| `tests/v1/core/test_owner_window_policy.py` | `tests/test_window_policy.py` | Pure CPU policy tests; imports rewritten only |

The migrated files retain their Apache-2.0 SPDX headers and original vLLM
contributor copyright notice. They were authored in PR #253 by `@CubeLander`;
the exact commit history remains in the immutable archive.

PR #253 was closed rather than merged. Its TP8 evidence and paired Ascend work
are research evidence, not a release receipt for this new repository. No
scheduler, worker, KV, transport, Ascend, or DSpark integration source is
considered migrated. PR #239 remains provenance input until its upstream
compatibility fixes are separated from StateHarbor-owned behavior.
