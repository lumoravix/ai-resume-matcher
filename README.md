
# AI Resume Matcher
### NLP-Based Resume Screening & Skill Gap Analysis

An AI-powered web application that analyzes resumes against job descriptions using Natural Language Processing (NLP), TF-IDF, and semantic similarity.

The platform helps users evaluate resume relevance, identify missing skills, receive improvement recommendations, prepare for interviews, and generate personalized cover-letter drafts.

## Live Application

🚀 [Launch AI Resume Matcher](https://ai-resume-matcher-fmvvtzuv4eheefxjhw3v8x.streamlit.app/)

## Project Overview

AI Resume Matcher is designed to simplify resume evaluation and provide actionable feedback.

Traditional keyword matching can overlook relevant experience expressed in different words. This project combines keyword-based similarity and semantic analysis to provide a broader assessment of resume compatibility with job requirements.

## Key Features

- **Resume Upload:** Supports PDF and DOCX files.
- **Text Input:** Allows users to paste resume content directly.
- **Keyword Matching:** Calculates TF-IDF-based similarity scores.
- **Semantic Matching:** Uses Sentence Transformers to evaluate contextual similarity.
- **Skill Gap Analysis:** Identifies matching and missing skills.
- **Match Classification:** Categorizes results as Strong, Partial, or Low Match.
- **Learning Recommendations:** Suggests areas for skill development.
- **Interview Preparation:** Generates practice questions based on relevant skills.
- **Resume Improvement:** Provides recommendations for improving resume content.
- **Cover Letter Generator:** Creates editable, personalized cover-letter drafts.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| Natural Language Processing | NLP, TF-IDF |
| Machine Learning | Scikit-learn |
| Semantic Analysis | Sentence Transformers |
| Data Processing | Pandas, NumPy |
| Deployment | Streamlit Community Cloud |
| Version Control | Git, GitHub |

## How It Works

1. **Resume Input:** Upload a PDF/DOCX resume or paste resume text.
2. **Job Description Input:** Provide the target job description.
3. **Text Processing:** Extract and preprocess the text.
4. **Similarity Analysis:** Calculate keyword-based and semantic similarity scores.
5. **Skill Gap Identification:** Identify matching and missing skills.
6. **Results & Recommendations:** Display matching insights and improvement suggestions.
7. **Additional Assistance:** Generate interview questions and personalized cover-letter drafts.

## Application Workflow

```text
Resume (PDF / DOCX / Text)
            |
            v
     Text Extraction
            |
            v
      Preprocessing
            |
            v
      Job Description
            |
            v
  TF-IDF + Semantic Analysis
            |
            v
     Similarity Scoring
            |
            v
      Skill Gap Analysis
            |
            v
  Recommendations & Insights
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/lumoravix/ai-resume-matcher.git
cd ai-resume-matcher
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## Project Structure

```text
ai-resume-matcher/
|
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- src/
|-- tests/
```

- `app.py` — Streamlit application entry point
- `src/` — Supporting application modules
- `tests/` — Automated tests
- `requirements.txt` — Python dependencies

## Testing

The repository includes a `tests/` directory for checking application functionality.

Run the test suite using:

```bash
python -m pytest
```

## Future Improvements

- Improved skill extraction and normalization
- More detailed resume-to-job compatibility explanations
- Support for additional resume formats
- Enhanced personalized recommendations
- Expanded automated testing

## Disclaimer

Resume matching scores are estimates intended to support resume review and improvement. They do not guarantee recruitment outcomes or represent an employer's actual applicant tracking system.

---

**Developed with Python, Streamlit, and Natural Language Processing.**
