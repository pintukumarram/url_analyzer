import pytest
from utils.url_parser import parse_url_details, is_valid_url, mask_sensitive_params


def test_valid_url():
    assert is_valid_url("https://example.com") is True


def test_invalid_url():
    assert is_valid_url("example.com") is False


def test_parse_url_basic():
    url = "https://example.com/path?user=admin"
    result = parse_url_details(url)

    assert result["Scheme"]["value"] == "https"
    assert result["Domain"]["value"] == "example.com"
    assert result["Path"]["value"] == "/path"


def test_query_parameters_parsed():
    url = "https://example.com/?id=10&role=admin"
    result = parse_url_details(url)

    assert result["Query Parameters"]["value"]["id"] == "10"
    assert result["Query Parameters"]["value"]["role"] == "admin"


def test_sensitive_parameter_masking():
    params = {
        "username": "pintu",
        "password": "secret123",
        "token": "abcd"
    }

    masked = mask_sensitive_params(params)

    assert masked["password"] == "********"
    assert masked["token"] == "********"
    assert masked["username"] == "pintu"
    


def test_invalid_url_returns_error():
    result = parse_url_details("invalid-url")
    assert "error" in result
