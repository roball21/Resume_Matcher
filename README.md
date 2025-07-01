# Resume Matcher 

---

## Features

 - Extracts skills from your resume in .pdf format
 - Uses RapidAPI to extract job postings
 - Converts resume and job descriptions to embedding using OpenAI
 - Compares your resume to each job posting and ranks them by similarity
 - Caches embeddings to avoid repeated API calls and reduce cost

 ---

 ## Project Structure

```text

 .
├── getApplications.py     # Fetches job data from an API (e.g. ZipRecruiter)
├── readResume.py          # Extracts and processes skills from a PDF resume
├── openaiConnection.py        # Embeds resume & job data and compares similarity
├── userResume.json        # JSON file with processed resume text
├── st_louis_cs_jobs.json  # Sample job listings file
├── resume_embedding.npy   # Cached OpenAI embedding of your resume
├── job_embeddings.npy     # Cached OpenAI embeddings of jobs
├── main.py                # Orchestrates the full pipeline
├── your_resume.pdf        # Your resume must be placed in the project directory
├── .env                   # Where you place your OpenAI API key

```

---

## Requirements

 - Python 3.8+
 - OpenAI API key (set via .env)
 - RapidAPI
 - PyPDF2, openai, requests, numpy, python-dotenv, scikit-learn

---

## OpenAI API Setup

 1. Create an account at OpenAI
 2. Generate an API key
 3. Create a .env file:

 ```text
 
 OPEN_API_KEY=your_api_key_here

 ```

 ## How to Run

 ```bash

 python main.py

 ```

 ## Author

  - Robert Ballard - github.com/roball21
