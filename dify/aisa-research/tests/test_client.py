import json
import unittest
from io import BytesIO
from unittest import mock
from urllib import error

from client import AisaClientError, build_request, execute, parse_extract_urls


class FakeResponse:
    def __init__(self, body: bytes, request_id: str = "request-1") -> None:
        self._body = BytesIO(body)
        self.headers = {"X-Request-ID": request_id}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self, size: int = -1) -> bytes:
        return self._body.read(size)


class ClientTests(unittest.TestCase):
    def test_builds_search_request_without_key_in_url(self) -> None:
        request_value = build_request(
            "tavily_search", {"query": "dify plugins"}, "fake-key"
        )
        self.assertEqual(
            request_value.full_url, "https://api.aisa.one/apis/v1/tavily/search"
        )
        self.assertEqual(request_value.get_header("Authorization"), "Bearer fake-key")
        self.assertEqual(json.loads(request_value.data), {"query": "dify plugins"})

    def test_parses_one_to_three_public_urls(self) -> None:
        self.assertEqual(
            parse_extract_urls("https://example.com/a\nhttps://example.org/b"),
            ["https://example.com/a", "https://example.org/b"],
        )

    def test_rejects_private_extract_url(self) -> None:
        with self.assertRaises(AisaClientError):
            parse_extract_urls("http://127.0.0.1/private")

    def test_execute_sanitizes_api_key(self) -> None:
        response = FakeResponse(b'{"message":"token fake-key was accepted"}')
        request_value = build_request("tavily_search", {"query": "q"}, "fake-key")
        with mock.patch("client.request.urlopen", return_value=response):
            data, request_id = execute(request_value, "fake-key")
        self.assertEqual(data["message"], "token [REDACTED] was accepted")
        self.assertEqual(request_id, "request-1")

    def test_http_error_does_not_leak_key(self) -> None:
        http_error = error.HTTPError(
            "https://api.aisa.one/test",
            401,
            "Unauthorized",
            {},
            BytesIO(b'{"message":"bad fake-key"}'),
        )
        request_value = build_request("tavily_search", {"query": "q"}, "fake-key")
        with mock.patch("client.request.urlopen", side_effect=http_error):
            with self.assertRaises(AisaClientError) as context:
                execute(request_value, "fake-key")
        self.assertNotIn("fake-key", str(context.exception.details))


if __name__ == "__main__":
    unittest.main()
