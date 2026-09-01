# StateHarbor

Owner-maintained research carrier for the request-owned runtime preserved in
the archived vLLM-HUST repository.

**Status: research migration scaffold (`import_only`). This repository is not
an installable runtime implementation and makes no current support claim.**

StateHarbor explored request-owned KV allocation, scheduler authority,
attention and sampling transport, deterministic output aggregation, background
D2H drain, and idle-bandwidth H2D restore. The legacy implementation crossed
most vLLM process boundaries; it must not be copied back as one import-time
plugin.

The migration should first separate neutral host seams from owner-maintained
policy and runtime components. Until those contracts are reviewed, the package
only supplies static metadata for provenance and architecture work.

```bash
pip install -e .
vllm-hust-ext extension inspect org.vllm-hust.stateharbor
```

See [PROVENANCE.md](PROVENANCE.md) and [MAINTAINERS.md](MAINTAINERS.md).
