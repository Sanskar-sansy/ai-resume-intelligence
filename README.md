AI Resume Intelligence Engine (Using Endee Vector Database)
Overview

This project implements a semantic resume screening system using vector embeddings and the Endee vector database.

The goal is to automate resume ranking by comparing job descriptions with candidate resumes using embedding similarity instead of keyword matching. The system ranks candidates based on how closely their resumes match the meaning of a job description.

This project demonstrates practical usage of:

Vector embeddings

Approximate Nearest Neighbor (ANN) search

HNSW indexing

REST API integration

MessagePack decoding

Endee vector database

Problem Statement

Manual resume screening is slow and often biased toward keyword matching. A better approach is to use semantic similarity so that resumes are matched based on meaning rather than exact words.

For example:

"NLP Engineer" should match "Natural Language Processing Developer"

"ML Specialist" should match "Machine Learning Engineer"

This project builds a system that performs that semantic matching.

System Architecture

The system follows this pipeline:

Resume Text
   ↓
SentenceTransformer Embedding (384-dim)
   ↓
Stored in Endee Dense Index (Cosine Similarity)
   ↓
Job Description Embedding
   ↓
ANN Search (HNSW)
   ↓
Ranked Candidate Results
How Endee Is Used

A dense index named resumes is created (dimension = 384, cosine similarity).

Resume embeddings are inserted using:

POST /api/v1/index/<index_name>/vector/insert

Semantic search is performed using:

POST /api/v1/index/<index_name>/search

The search response is returned in MessagePack format and decoded in Python.

Results are ranked based on cosine similarity.

This project uses Endee as the core vector search engine.

Project Structure
ai_resume_app/
│
├── embedder.py          # Generates embeddings using MiniLM
├── endee_client.py      # REST API client for Endee
├── ingest_resume.py     # Inserts resume embeddings into Endee
├── test_search.py       # CLI-based ranking test
├── app.py               # Futuristic Streamlit dashboard
├── README.md
└── .gitignore
Scoring Logic

The similarity score returned by Endee is cosine similarity in the range:

0 → 1

To make it more interpretable, it is converted to a Resume Score:

Resume Score = similarity × 100

Example:

0.86 → 86/100

0.72 → 72/100

This makes ranking more intuitive for recruiters.

Technologies Used

Python 3.12

SentenceTransformers (all-MiniLM-L6-v2)

Endee Vector Database

HNSW ANN Search

Streamlit (Dashboard UI)

Requests + MsgPack (API communication)

Setup Instructions
1. Start Endee

Inside the Endee directory:

./run.sh

Server runs at:

http://localhost:8080
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install sentence-transformers streamlit requests msgpack
3. Create Index

Using Endee dashboard:

Name: resumes

Dimension: 384

Space Type: Cosine

Precision: Float32

4. Insert Resumes
python ingest_resume.py
5. Run Dashboard
streamlit run app.py
Features

Semantic resume ranking

ANN-based similarity search

Clean modular architecture

MessagePack decoding

Futuristic AI dashboard interface

Scalable design for large resume collections

Possible Improvements

PDF resume upload support

Skill extraction pipeline

Hybrid (dense + sparse) search

Recruiter analytics dashboard

Candidate comparison mode

Author

Sanskar Saxena
CSE Student | AI/ML Enthusiast
