import streamlit as st
from embedder import get_embedding
from endee_client import search_vector

# ---------------- Page Setup ----------------
st.set_page_config(
    page_title="AI Resume Intelligence",
    page_icon="🧠",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
/* Background */
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

/* Hide Streamlit default header */
header {visibility: hidden;}
footer {visibility: hidden;}

/* Glass Card */
.glass-card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0,255,255,0.2);
    margin-bottom: 20px;
    border: 1px solid rgba(0,255,255,0.2);
}

/* Neon Title */
.neon-title {
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(90deg, #00f5ff, #ff00c8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Score Style */
.score {
    font-size: 40px;
    font-weight: bold;
    color: #00f5ff;
    text-shadow: 0 0 15px #00f5ff;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #00f5ff, #ff00c8);
    color: black;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown('<div class="neon-title">AI Resume Intelligence Engine</div>', unsafe_allow_html=True)
st.markdown("### Semantic Candidate Ranking Powered by Endee ANN Search")
st.write("")

# ---------------- Input ----------------
job_desc = st.text_area("Enter Job Description", height=150)

if st.button("Run AI Analysis"):

    if job_desc.strip() == "":
        st.warning("Please enter a valid job description.")
    else:
        with st.spinner("AI Engine Processing..."):
            embedding = get_embedding(job_desc)
            results = search_vector("resumes", embedding, top_k=5)

        st.write("")
        st.markdown("## Top Ranked Candidates among the selected")

        if results:
            for rank, r in enumerate(results, start=1):

                similarity = r["similarity"]
                score = round(similarity * 100)

                st.markdown(f"""
                <div class="glass-card">
                    <div style="display:flex; justify-content:space-between;">
                        <div>
                            <h3>#{rank} — {r['metadata'].get('name')}</h3>
                            <p><b>Role:</b> {r['metadata'].get('role','N/A')}</p>
                            <p><b>Skills:</b> {r['metadata'].get('skills','N/A')}</p>
                        </div>
                        <div class="score">{score}/100</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.progress(score / 100)

        else:
            st.error("No matching resumes found.")
