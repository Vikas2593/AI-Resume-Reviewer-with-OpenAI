import streamlit as st
from core.Resume_Reviewer import review_resume
from reports.html_report import generate_html_report

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Resume Reviewer",
    layout="wide"
)

# -------------------------------
# CSS
# -------------------------------
st.markdown("""
<style>
.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #1f2933;
}
.metric {
    font-size: 24px;
    font-weight: bold;
    color: #38bdf8;
}
.badge-hire { background:#16a34a;color:white;padding:6px 14px;border-radius:20px;}
.badge-reject { background:#dc2626;color:white;padding:6px 14px;border-radius:20px;}
.badge-maybe { background:#f59e0b;color:black;padding:6px 14px;border-radius:20px;}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Session State
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "input"

# ===============================
# PAGE 1: INPUT
# ===============================
if st.session_state.page == "input":

    st.title("📄 AI Resume Reviewer")
    st.caption("Paste resume and job description to evaluate")

    col1, col2 = st.columns(2)

    with col1:
        resume_text = st.text_area("Resume Text", height=300)

    with col2:
        job_description = st.text_area("Job Description", height=300)

    if st.button("🚀 Analyze Resume", use_container_width=True):
        if not resume_text or not job_description:
            st.warning("Please provide both Resume and Job Description")
        else:
            with st.spinner("Analyzing..."):
                result = review_resume(resume_text, job_description)

            st.session_state.result = result
            st.session_state.page = "report"
            st.rerun()

# ===============================
# PAGE 2: REPORT
# ===============================
elif st.session_state.page == "report":

    result = st.session_state.result

    st.title("📊 Resume Review Report")

    st.markdown(f"""
    <div class="card">
        <p><b>Name:</b> {result['candidate_name']}</p>
        <p><b>City:</b> {result['city']}</p>
        <p><b>Experience:</b> {result['total_experience']} years</p>
        <p class="metric">Score: {result['suitability_score']}%</p>
    </div>
    """, unsafe_allow_html=True)

    # Recommendation badge
    rec = result["recommendation"]
    badge_class = "badge-hire" if rec in ["Hire", "StrongHire"] else "badge-maybe" if rec == "Maybe" else "badge-reject"

    st.markdown(f"""
    <div class="{badge_class}">{rec}</div>
    """, unsafe_allow_html=True)

    st.progress(result["suitability_score"] / 100)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'><h4>✅ Matched Skills</h4></div>", unsafe_allow_html=True)
        for s in result["skill_matching"]:
            st.write(f"- {s}")

    with col2:
        st.markdown("<div class='card'><h4>❌ Missing Skills</h4></div>", unsafe_allow_html=True)
        for s in result["skill_unmatched"]:
            st.write(f"- {s}")

    st.markdown("<div class='card'><h4>📝 Summary</h4></div>", unsafe_allow_html=True)
    st.write(result["short_summary"])

    html_report = generate_html_report(result)

    st.download_button(
        "⬇️ Download HTML Report",
        html_report,
        file_name="resume_report.html",
        mime="text/html"
    )

    if st.button("🔁 Analyze Another Resume"):
        st.session_state.page = "input"
        st.rerun()
