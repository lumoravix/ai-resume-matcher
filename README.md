# AI Resume Matcher

A Streamlit web application that compares a resume with a job description and provides skill-gap analysis, similarity scores, interview questions, learning suggestions, and resume-improvement advice.

## Live Demo
[Open the live AI Resume Matcher](https://ai-resume-matcher-fmvvtzuv4eheefxjhw3v8x.streamlit.app/)


## Features

- Upload resumes in PDF or DOCX format
- Paste resume text directly
- TF-IDF similarity score for keyword matching
- Semantic similarity score using Sentence Transformers
- Matching and missing-skill analysis
- Match summary: Strong, Partial, or Low match
- Learning suggestions for missing skills
- Practice interview questions based on skills
- Resume-improvement suggestions
- Personalized, editable cover-letter draft based on matching skills and optional job/company details

## Technologies Used

- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- PyMuPDF
- python-docx
- PyTorch

## How It Works

1. Upload or paste a resume.
2. Paste a job description.
3. Click **Check Match**.
4. The app extracts text and compares the resume with the role using:
   - TF-IDF for important-word similarity
   - Sentence embeddings for meaning-based similarity
   - Skill matching from a known skills list
5. View the match summary, skills, suggestions, and interview questions.

## Run Locally

```bash
git clone https://github.com/lumoravix/ai-resume-matcher.git
cd ai-resume-matcher
pip install -r requirements.txt
streamlit run app.py
