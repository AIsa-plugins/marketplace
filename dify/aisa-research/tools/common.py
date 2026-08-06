from typing import Any

from client import AisaClientError, invoke


def invoke_aisa(operation: str, parameters: dict[str, Any], api_key: str) -> dict[str, Any]:
    try:
        return invoke(operation, parameters, api_key)
    except AisaClientError as exc:
        error: dict[str, Any] = {"type": exc.error_type, "message": exc.message}
        if exc.http_status is not None:
            error["http_status"] = exc.http_status
        if exc.details is not None:
            error["details"] = exc.details
        return {"ok": False, "operation": operation, "error": error}
