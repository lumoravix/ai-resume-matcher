from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_tfidf_similarity(resume_text, job_description):
    vectorizer = TfidfVectorizer(stop_words="english")

    text_matrix = vectorizer.fit_transform(
        [resume_text, job_description]
    )

    similarity = cosine_similarity(
        text_matrix[0:1],
        text_matrix[1:2]
    )[0][0]

    return similarity * 100