"""Import-only descriptor for the owner-led StateHarbor migration."""


class StateHarborDescriptor:
    """Metadata anchor; no runtime hooks are installed by this package."""

    extension_id = "org.vllm-hust.stateharbor"
    activation_status = "import_only"
