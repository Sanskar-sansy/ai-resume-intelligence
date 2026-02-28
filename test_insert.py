from embedder import get_embedding
from endee_client import insert_vector

text = "Machine Learning Engineer skilled in Python, NLP, Deep Learning"

embedding = get_embedding(text)

response = insert_vector(
    index_name="resumes",
    vector_id="resume_1",
    vector=embedding,
    metadata={"name": "Test Candidate"}
)

print(response)
