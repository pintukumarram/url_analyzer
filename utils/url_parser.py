from urllib.parse import urlparse, parse_qs
import re

SENSITIVE_KEYS = {"password", "pwd", "pass", "token", "secret", "apikey", "api_key"}

def is_valid_url(url):
    regex = re.compile(
        r'^(https?|ftp)://'
        r'(\S+)$'
    )
    return re.match(regex, url) is not None

def mask_sensitive_params(params):
    masked = {}
    for key, value in params.items():
        if key.lower() in SENSITIVE_KEYS:
            masked[key] = "********"
        else:
            masked[key] = value
    return masked

def parse_url_details(url):
    if not is_valid_url(url):
        return {"error": "Invalid URL format. Please include http:// or https://"}

    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    clean_params = {k: v[0] for k, v in query_params.items()}
    masked_params = mask_sensitive_params(clean_params)

    return {
        "Scheme": {
            "value": parsed.scheme,
            "description": "Protocol used to access the resource"
        },
        "Domain": {
            "value": parsed.hostname,
            "description": "Domain name of the website"
        },
        "Port": {
            "value": parsed.port or "Default",
            "description": "Network port (default depends on protocol)"
        },
        "Path": {
            "value": parsed.path or "/",
            "description": "Path to the resource"
        },
        "Query Parameters": {
            "value": masked_params,
            "description": "Query parameters (sensitive values masked)"
        },
        "Fragment": {
            "value": parsed.fragment or "None",
            "description": "Anchor or section in the page"
        }
    }
