from predicition_engine import predict_url


def test_google_prediction():
    result = predict_url("https://google.com")

    assert result["url"] == "https://google.com"
    assert result["normalized_url"] == "google.com"
    assert result["prediction"] in [0, 1]
    assert 0 <= result["legitimate_probability"] <= 100
    assert 0 <= result["phishing_probability"] <= 100
    assert result["risk_level"] in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]


def test_ip_address_prediction():
    result = predict_url("http://192.168.1.10/login")

    assert result["prediction"] in [0, 1]
    assert 0 <= result["legitimate_probability"] <= 100
    assert 0 <= result["phishing_probability"] <= 100


def test_suspicious_url_prediction():
    result = predict_url(
        "https://secure-login.com/verify/account123"
    )

    assert result["prediction"] in [0, 1]
    assert 0 <= result["legitimate_probability"] <= 100
    assert 0 <= result["phishing_probability"] <= 100