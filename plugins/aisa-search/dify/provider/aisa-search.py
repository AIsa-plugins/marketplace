from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class AisaSearchProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        api_key = credentials.get("aisa_api_key")
        if not isinstance(api_key, str) or not api_key.strip():
            raise ToolProviderCredentialValidationError("AIsa API key is required.")
        if "\n" in api_key or "\r" in api_key:
            raise ToolProviderCredentialValidationError("AIsa API key is invalid.")
