# AI Resume Matcher

An AI-assisted web application that compares a resume with a job description and provides match scores, skill-gap analysis, learning suggestions, interview questions, and resume improvement advice.

## Features

- Upload resumes in PDF or DOCX format
- Paste resume text instead of uploading a file
- TF-IDF similarity score for important-word matching
- Semantic similarity score using sentence embeddings
- Matching and missing skill analysis
- Personalized learning suggestions for missing skills
- Practice interview questions based on skills
- Rule-based resume improvement suggestions

## Technologies Used

- Python
- Streamlit
- PyMuPDF
- python-docx
- scikit-learn
- sentence-transformers
- PyTorch

## Project Structure

```text
resume-matcher/
├── src/
│   ├── embedding_matcher.py
│   ├── file_reader.py
│   ├── interview_questions.py
│   ├── learning_suggestions.py
│   ├── matcher.py
│   ├── resume_advisor.py
│   └── skill_extractor.py
├── app.py
├── requirements.txt
└── README.md