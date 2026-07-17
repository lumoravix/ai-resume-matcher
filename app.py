import streamlit as st

from src.file_reader import (
    extract_text_from_docx,
    extract_text_from_pdf,
)
from src.matcher import calculate_tfidf_similarity
from src.embedding_matcher import calculate_embedding_similarity
from src.skill_extractor import get_skill_gap

STOP_WORDS = {
    "i", "know", "looking", "for", "a", "an", "the",
    "with", "and", "of", "to", "candidate"
}


def get_keywords(text):
    punctuation = ",.!?:;()[]"
    clean_text = text.lower()

    for character in punctuation:
        clean_text = clean_text.replace(character, " ")

    words = clean_text.split()
    keywords = set(words) - STOP_WORDS
    return keywords


st.title("AI Resume Matcher")
st.write(
    "Upload a PDF/DOCX resume or paste resume text to compare it "
    "with a job description."
)

uploaded_resume = st.file_uploader(
    "Upload your resume as a PDF or DOCX file",
    type=["pdf", "docx"]
)

if uploaded_resume is not None:
    if uploaded_resume.name.lower().endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_resume)
    else:
        resume_text = extract_text_from_docx(uploaded_resume)

    st.success("Resume uploaded and text extracted.")

    with st.expander("View extracted resume text"):
        st.write(resume_text)
else:
    resume_text = st.text_area(
        "Or paste your resume here",
        height=200,
        placeholder="Example: I know Python, SQL, and Machine Learning..."
    )

job_description = st.text_area(
    "Paste the job description here",
    height=200,
    placeholder="Example: Looking for a candidate with Python and SQL..."
)

if st.button("Check Match"):
    if resume_text and job_description:
        job_keywords = get_keywords(job_description)

        if job_keywords:
            tfidf_score = calculate_tfidf_similarity(
                resume_text,
                job_description
            )

            embedding_score = calculate_embedding_similarity(
                resume_text,
                job_description
            )

            matching_skills, missing_skills = get_skill_gap(
                resume_text,
                job_description
            )

            tfidf_column, embedding_column = st.columns(2)

            with tfidf_column:
                st.metric("TF-IDF Score", f"{tfidf_score:.0f}%")

            with embedding_column:
                st.metric(
                    "Semantic Match Score",
                    f"{embedding_score:.0f}%"
                )

            st.caption(
                "TF-IDF compares important words. Semantic matching uses "
                "sentence embeddings to compare context."
            )

            if matching_skills:
                st.write(
                    "**Matching skills:**",
                    ", ".join(sorted(matching_skills))
                )
            else:
                st.info("No known matching skills were found.")

            if missing_skills:
                st.write(
                    "**Missing skills:**",
                    ", ".join(sorted(missing_skills))
                )
            else:
                st.success("No known required skills are missing.")
        else:
            st.warning("Add meaningful keywords to the job description.")
    else:
        st.warning("Please upload/paste a resume and enter a job description.")