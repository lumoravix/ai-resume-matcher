import streamlit as st

from src.embedding_matcher import calculate_embedding_similarity
from src.file_reader import (
    extract_text_from_docx,
    extract_text_from_pdf,
)
from src.interview_questions import generate_interview_questions
from src.learning_suggestions import get_learning_suggestions
from src.matcher import calculate_tfidf_similarity
from src.skill_extractor import get_skill_gap
from src.resume_advisor import get_resume_improvement_suggestions
st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)
with st.sidebar:
    st.header("About this app")
    st.write(
        "Compare a resume with a job description using keyword, "
        "TF-IDF, and semantic similarity."
    )

    st.subheader("Features")
    st.markdown(
        "- PDF and DOCX upload\n"
        "- Skill-gap analysis\n"
        "- Learning suggestions\n"
        "- Interview questions\n"
        "- Resume improvement advice"
    )

    st.caption("Educational portfolio project.")

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
    return set(words) - STOP_WORDS


st.title("AI Resume Matcher")
st.caption(
    "Upload your resume, add a job description, and receive "
    "AI-assisted matching insights."
)
st.divider()


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
            st.subheader("Match summary")

            if embedding_score >= 70:
                st.success(
                    "Strong match: your resume is broadly aligned with this role."
                )
            elif embedding_score >= 40:
                st.warning(
                    "Partial match: you have some relevant strengths, but important "
                    "requirements may be missing."
                )
            else:
                st.error(
                    "Low match: tailor your resume more closely to this job description."
                )

            st.write(
                f"**Skills matched:** {len(matching_skills)} | "
                f"**Skills missing:** {len(missing_skills)}"
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

                suggestions = get_learning_suggestions(missing_skills)

                st.subheader("Learning suggestions")

                for suggestion in suggestions:
                    st.markdown(f"- {suggestion}")
            else:
                st.success("No known required skills are missing.")

            questions = generate_interview_questions(
                matching_skills,
                missing_skills
            )

            if questions:
                st.subheader("Practice interview questions")

                for question in questions:
                    st.markdown(f"- {question}")

            advice = get_resume_improvement_suggestions(
                embedding_score,
                missing_skills
            )

            if advice:
                st.subheader("Resume improvement suggestions")

                for item in advice:
                    st.markdown(f"- {item}")   