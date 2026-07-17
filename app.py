import streamlit as st

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
st.write("Paste your resume and a job description to check keyword overlap.")

resume_text = st.text_area(
    "Paste your resume here",
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

        matching_keywords = resume_keywords.intersection(job_keywords)
        missing_keywords = job_keywords - resume_keywords

        match_score = len(matching_keywords) / len(job_keywords) * 100

        st.metric("Basic Match Score", f"{match_score:.0f}%")
        st.write("**Matching keywords:**", ", ".join(matching_keywords))

        if missing_keywords:
            st.write("**Missing keywords:**", ", ".join(missing_keywords))
        else:
            st.success("Excellent! No keywords are missing.")

    else:
        st.warning("Please fill in both boxes first.")