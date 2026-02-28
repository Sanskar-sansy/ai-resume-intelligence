from embedder import get_embedding
from endee_client import search_vector

job_description = """
Looking for a Machine Learning Engineer skilled in Python and NLP.
"""

embedding = get_embedding(job_description)

results = search_vector("resumes", embedding, top_k=5)

print("\n🏆 Ranked Candidates:\n")

if results:
    for rank, candidate in enumerate(results, start=1):

        similarity = candidate["similarity"]
        score = round(similarity * 100)

        print(
            f"{rank}. {candidate['metadata'].get('name')} "
            f"— Resume Score: {score}/100"
        )
else:
    print("No candidates found.")
