import requests
import msgpack
import json

BASE_URL = "http://localhost:8080/api/v1"


def insert_vector(index_name, vector_id, vector, metadata=None):
    url = f"{BASE_URL}/index/{index_name}/vector/insert"

    payload = {
        "id": vector_id,
        "vector": vector
    }

    if metadata:
        payload["meta"] = json.dumps(metadata)

    try:
        response = requests.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        print("\n===== INSERT DEBUG =====")
        print("URL:", url)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        print("========================\n")

        return response.text

    except Exception as e:
        print("Request failed:", e)
        return None


def search_vector(index_name, query_vector, top_k=5):
    url = f"{BASE_URL}/index/{index_name}/search"

    payload = {
        "vector": query_vector,
        "k": top_k
    }

    response = requests.post(
        url,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=10
    )

    print("\n===== SEARCH DEBUG =====")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        decoded = msgpack.unpackb(response.content, raw=False)

        results = []
        for item in decoded:
            similarity, vec_id, meta, _, _, _ = item
            metadata = json.loads(meta.decode()) if meta else {}

            results.append({
                "id": vec_id,
                "similarity": round(similarity, 4),
                "metadata": metadata
            })

        print("Clean Results:", results)
        print("========================\n")
        return results

    else:
        print("Error:", response.text)
        return None
