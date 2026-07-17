KNOWN_SKILLS = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "streamlit",
    "fastapi",
    "git",
    "github",
    "docker",
    "tensorflow",
    "pytorch",
    "nlp",
    "spacy",
    "excel",
    "power bi"
]


def extract_skills(text):
    lower_text = text.lower()
    found_skills = set()

    for skill in KNOWN_SKILLS:
        if skill in lower_text:
            found_skills.add(skill)

    return found_skills


def get_skill_gap(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    matching_skills = resume_skills.intersection(required_skills)
    missing_skills = required_skills - resume_skills

    return matching_skills, missing_skills