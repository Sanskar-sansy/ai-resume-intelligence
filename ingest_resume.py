from embedder import get_embedding
from endee_client import insert_vector

# ---------- Resume Dataset ----------
resumes = [
    {
        "id": "john_ml",
        "text": """
        John Doe
        Machine Learning Engineer
        Skills: Python, NLP, Deep Learning, Transformers
        Experience: 3 years building ML models.
        """,
        "metadata": {
            "name": "John Doe",
            "role": "Machine Learning Engineer",
            "skills": "Python, NLP, Deep Learning"
        }
    },
    {
        "id": "alice_backend",
        "text": """
        Alice Smith
        Backend Engineer
        Skills: Java, Spring Boot, Microservices
        Experience: 4 years building backend systems.
        """,
        "metadata": {
            "name": "Alice Smith",
            "role": "Backend Engineer",
            "skills": "Java, Microservices"
        }
    },
    {
        "id": "rahul_ds",
        "text": """
        Rahul Sharma
        Data Scientist
        Skills: Python, Pandas, Machine Learning, SQL
        Experience: 2 years in data analytics.
        """,
        "metadata": {
            "name": "Rahul Sharma",
            "role": "Data Scientist",
            "skills": "Python, ML, SQL"
        }
    }
]

for resume in resumes:
    print(f"Inserting: {resume['metadata']['name']}")

    embedding = get_embedding(resume["text"])

    insert_vector(
        index_name="resumes",
        vector_id=resume["id"],
        vector=embedding,
        metadata=resume["metadata"]
    )

print("\n✅ All resumes inserted successfully.")
