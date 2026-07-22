from src.matcher import calculate_tfidf_similarity


def test_tfidf_similarity_returns_percentage():
    score = calculate_tfidf_similarity(
        "Python data analysis project",
        "Python developer with data analysis skills"
    )

    assert 0 <= score <= 100
    assert score > 0
