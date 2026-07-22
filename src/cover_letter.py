"""Create a truthful cover-letter draft from the match results."""


def format_skill(skill):
    """Display common technical acronyms in their usual form."""
    acronyms = {"sql", "nlp"}

    if skill.lower() in acronyms:
        return skill.upper()

    return skill.title()


def generate_cover_letter(matching_skills, job_title="", company_name=""):
    """Return an editable cover-letter draft without inventing experience."""
    role = job_title.strip() or "role"
    company = company_name.strip() or "your organization"

    if matching_skills:
        skills = ", ".join(
            format_skill(skill) for skill in sorted(matching_skills)
        )
        experience_sentence = (
            f"My resume highlights experience with {skills}, which aligns "
            "with the skills requested for this position."
        )
    else:
        experience_sentence = (
            "My resume highlights relevant skills and projects that I am "
            "ready to discuss further."
        )

    return (
        f"Dear Hiring Team at {company},\n\n"
        f"I am writing to apply for the {role}. {experience_sentence} "
        "I am eager to learn, contribute thoughtfully, and apply my skills "
        "to meaningful work.\n\n"
        "I would welcome the opportunity to discuss how my background and "
        "interests can support your team. Thank you for considering my "
        "application.\n\n"
        "Sincerely,\n"
        "[Your Name]"
    )
