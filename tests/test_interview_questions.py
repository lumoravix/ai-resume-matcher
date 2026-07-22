from src.interview_questions import generate_interview_questions


def test_interview_questions_are_created_for_matching_skills():
    questions = generate_interview_questions({"python"}, set())

    assert len(questions) == 1
    assert "Python" in questions[0]


def test_interview_questions_are_created_for_missing_skills():
    questions = generate_interview_questions(set(), {"sql"})

    assert questions == ["How would you begin learning sql for this role?"]
