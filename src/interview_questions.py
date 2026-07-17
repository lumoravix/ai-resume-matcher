QUESTION_TEMPLATES = {
    "python": "Explain Python lists, dictionaries, and when you would use each.",
    "sql": "What is the difference between an INNER JOIN and a LEFT JOIN?",
    "machine learning": "Explain the difference between training data and test data.",
    "data analysis": "How would you clean a dataset with missing values?",
    "pandas": "How do you filter rows and group data in a pandas DataFrame?",
    "numpy": "Why are NumPy arrays useful for numerical work?",
    "scikit-learn": "How would you evaluate a classification model?",
    "streamlit": "How would you build a file-upload feature in Streamlit?",
    "fastapi": "What is an API endpoint, and how would you create one in FastAPI?",
    "git": "What is the difference between git commit and git push?",
    "docker": "What problem does Docker solve for application deployment?",
    "tensorflow": "What is a neural network, in simple words?",
    "pytorch": "What is a tensor in PyTorch?",
    "nlp": "What is the difference between TF-IDF and sentence embeddings?",
    "excel": "How would you use a pivot table to summarize data?"
}


def generate_interview_questions(matching_skills, missing_skills):
    questions = []

    for skill in sorted(matching_skills):
        question = QUESTION_TEMPLATES.get(
            skill,
            f"Explain how you have used {skill} in a project."
        )
        questions.append(question)

    for skill in sorted(missing_skills):
        questions.append(
            f"How would you begin learning {skill} for this role?"
        )

    return questions