LEARNING_SUGGESTIONS = {
    "python": "Practice Python basics, functions, and small projects.",
    "sql": "Learn SELECT, WHERE, JOIN, GROUP BY, and database basics.",
    "machine learning": "Learn supervised learning, model evaluation, and scikit-learn.",
    "data analysis": "Practice cleaning, exploring, and visualizing data with pandas.",
    "pandas": "Practice DataFrames, filtering, grouping, and missing-value handling.",
    "numpy": "Learn arrays, indexing, and numerical operations.",
    "scikit-learn": "Build small classification and regression projects.",
    "streamlit": "Practice forms, file upload, buttons, and displaying results.",
    "fastapi": "Learn how to create simple Python APIs.",
    "git": "Practice commits, branches, and pushing projects to GitHub.",
    "docker": "Learn containers after your app is stable.",
    "tensorflow": "Learn neural-network fundamentals and Keras.",
    "pytorch": "Learn tensors, datasets, and neural-network training.",
    "nlp": "Practice text cleaning, TF-IDF, embeddings, and similarity.",
    "excel": "Practice formulas, tables, pivot tables, and charts."
}


def get_learning_suggestions(missing_skills):
    suggestions = []

    for skill in sorted(missing_skills):
        suggestion = LEARNING_SUGGESTIONS.get(
            skill,
            f"Find a beginner course and build a small project using {skill}."
        )
        suggestions.append(f"**{skill.title()}**: {suggestion}")

    return suggestions