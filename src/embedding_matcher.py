import re

from sentence_transformers import SentenceTransformer, util


MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)


def calculate_embedding_similarity(resume_text, job_description):
    embeddings = model.encode(
        [resume_text, job_description],
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        embeddings[0],
        embeddings[1]
    ).item()

    return similarity * 100


def get_relevant_resume_points(resume_text, job_description, limit=3):
    sentences = re.split(r"(?<=[.!?])\s+|\n+", resume_text)

    clean_sentences = [
        sentence.strip("•- \t")
        for sentence in sentences
        if len(sentence.strip()) >= 30
    ]

    if not clean_sentences:
        return []

    job_embedding = model.encode(
        job_description,
        convert_to_tensor=True
    )

    sentence_embeddings = model.encode(
        clean_sentences,
        convert_to_tensor=True
    )

    scores = util.cos_sim(
        sentence_embeddings,
        job_embedding
    ).flatten().tolist()

    ranked_points = sorted(
        zip(clean_sentences, scores),
        key=lambda item: item[1],
        reverse=True
    )

    return ranked_points[:limit]