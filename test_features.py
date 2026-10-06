from features.extractor import extract_features


def test_extract_features():
    url = "https://google.com"

    features = extract_features(url)

    assert features is not None
    assert isinstance(features, list)
    assert len(features) == 23