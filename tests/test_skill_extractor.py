from src.skill_extractor import extract_skills, get_skill_gap


def test_extract_skills_finds_known_skills():
    text = "I use Python, SQL, Pandas, and machine learning."

    skills = extract_skills(text)

    assert {"python", "sql", "pandas", "machine learning"} <= skills


def test_get_skill_gap_separates_matching_and_missing_skills():
    resume = "Python and Pandas projects"
    job_description = "Python, SQL, and Pandas required"

    matching, missing = get_skill_gap(resume, job_description)

    assert matching == {"python", "pandas"}
    assert missing == {"sql"}
