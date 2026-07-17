def get_resume_improvement_suggestions(
    semantic_score,
    missing_skills
):
    suggestions = []

    if semantic_score < 40:
        suggestions.append(
            "Tailor your resume summary and projects more closely to "
            "the job description."
        )
    elif semantic_score < 70:
        suggestions.append(
            "Your resume is partly aligned. Strengthen the most relevant "
            "projects and skills."
        )
    else:
        suggestions.append(
            "Your resume aligns well with this role. Improve it by making "
            "your achievements more specific."
        )

    if missing_skills:
        skills = ", ".join(sorted(missing_skills))
        suggestions.append(
            f"Consider learning these relevant skills: {skills}."
        )
        suggestions.append(
            "Only add a skill to your resume after you have genuinely "
            "learned or used it."
        )

    suggestions.append(
        "Use action verbs and measurable outcomes in your project bullets."
    )
    suggestions.append(
        "Keep your resume focused on relevant skills, projects, and results."
    )

    return suggestions