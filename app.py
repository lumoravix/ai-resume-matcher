import streamlit as st

from src.file_reader import (
    extract_text_from_docx,
    extract_text_from_pdf,
)

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
        resume_keywords = get_keywords(resume_text)
        job_keywords = get_keywords(job_description)

        if job_keywords:
            matching_keywords = resume_keywords.intersection(job_keywords)
            missing_keywords = job_keywords - resume_keywords
            match_score = len(matching_keywords) / len(job_keywords) * 100

            st.metric("Basic Match Score", f"{match_score:.0f}%")
            st.write(
                "**Matching keywords:**",
                ", ".join(sorted(matching_keywords))
            )

            if missing_keywords:
                st.write(
                    "**Missing keywords:**",
                    ", ".join(sorted(missing_keywords))
                )
            else:
                st.success("Excellent! No keywords are missing.")
        else:
            st.warning("Add meaningful keywords to the job description.")
    else:
        st.warning("Please upload/paste a resume and enter a job description.")