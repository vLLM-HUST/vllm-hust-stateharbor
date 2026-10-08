# StateHarbor

Owner-maintained research carrier for the request-owned runtime preserved in
the archived vLLM-HUST repository.

**Status: installable contract/reference package (`import_only`). It contains
no vLLM activation hook and makes no current runtime support claim.**

StateHarbor explored request-owned KV allocation, scheduler authority,
attention and sampling transport, deterministic output aggregation, background
D2H drain, and idle-bandwidth H2D restore. The legacy implementation crossed
most vLLM process boundaries; it must not be copied back as one import-time
plugin.

The package now preserves the dependency-neutral request-owner protocol,
reference coordinator/worker state machines, and receipt-driven window policy
from the legacy work. Scheduler, worker, KV allocation, transport, and device
integration remain outside this package until public host contracts exist.

Importing `vllm_hust_stateharbor` has no side effects. The reference layer can
be tested on CPU without installing vLLM or torch.

```bash
pip install -e .
vllm-hust-ext extension inspect org.vllm-hust.stateharbor
```

See [PROVENANCE.md](PROVENANCE.md) and [MAINTAINERS.md](MAINTAINERS.md).

## Canonical MOD metadata

Repository identity, directly responsible maintainers, advisor status, default-off
activation, rollback, scope, and evidence qualification are recorded in
[`MOD_METADATA.json`](MOD_METADATA.json). `advisor_status: unknown` is not the
same as confirmed `none`. Performance statements remain limited to the workloads
and evidence labels recorded there; they are not general online claims.
