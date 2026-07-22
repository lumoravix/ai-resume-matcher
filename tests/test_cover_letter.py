from src.cover_letter import generate_cover_letter


def test_cover_letter_uses_provided_role_company_and_skills():
    letter = generate_cover_letter(
        {"python", "sql"},
        "Data Analyst",
        "Acme Technologies"
    )

    assert "Data Analyst" in letter
    assert "Acme Technologies" in letter
    assert "Python, SQL" in letter


def test_cover_letter_uses_safe_defaults_when_details_are_missing():
    letter = generate_cover_letter(set())

    assert "the role" in letter
    assert "your organization" in letter
