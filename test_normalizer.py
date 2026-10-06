from features.urls_utils import normalize_url


def test_google_domain():
    assert normalize_url("google.com") == "google.com"


def test_http_google():
    assert normalize_url("http://google.com") == "google.com"


def test_https_google():
    assert normalize_url("https://google.com") == "google.com"


def test_www_google():
    assert normalize_url("www.google.com") == "google.com"


def test_www_google_with_slash():
    assert normalize_url("https://www.google.com/") == "google.com"


def test_google_login():
    assert normalize_url("https://google.com/login") == "google.com/login"