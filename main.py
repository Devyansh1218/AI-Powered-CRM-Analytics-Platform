import streamlit as st
import pandas as pd
import base64
from pathlib import Path

from core.analytics import (
    get_kpis,
    get_funnel_data,
    funnel_conversion,
    get_churn_distribution,
    churn_by_plan,
    revenue_by_plan,
)
from core.chatbot import answer_question
from core.report import generate_executive_report

ROOT_DIR = Path(__file__).resolve().parent

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="AI CRM Analytics",
    layout="wide",
)

# ==========================
# LOGIN
# ==========================
st.session_state.setdefault("logged_in", False)
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center'>AI CRM Analytics</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center'>Login</h3>", unsafe_allow_html=True)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login") and email and password:
        st.session_state.logged_in = True
        st.rerun()
    st.stop()

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "",
    ["Overview", "Funnel Analysis", "Churn Analysis", "AI Insights", "Chatbot", "Executive Report"],
)

uploaded = st.sidebar.file_uploader("Upload CRM CSV", type=["csv"])

# ==========================
# DATA
# ==========================
df = pd.read_csv(uploaded) if uploaded else None
if df is None or df.empty:
    st.info("⬅️ Upload a CRM CSV file to begin analysis.")
    st.stop()

# ==========================
# PREVIEW
# ==========================
with st.expander("🔍 Data Preview"):
    st.dataframe(df.head(20))

# ==========================
# OVERVIEW
# ==========================
if page == "Overview":
    st.title("📈 Overview")
    kpis = get_kpis(df)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Customers", kpis["customers"])
    c2.metric("Revenue", f"${kpis['revenue']:,.0f}")
    c3.metric("Churn Rate", f"{kpis['churn_rate']}%")
    c4.metric("Avg Logins", kpis["avg_logins"])

    st.subheader("💰 Revenue by Plan")
    st.bar_chart(revenue_by_plan(df).set_index("plan_type"))

# ==========================
# FUNNEL
# ==========================
elif page == "Funnel Analysis":
    st.title("🔻 Funnel Analysis")
    st.bar_chart(get_funnel_data(df).set_index("stage"))
    st.subheader("Conversion Rates")
    st.dataframe(funnel_conversion(df))

# ==========================
# CHURN
# ==========================
elif page == "Churn Analysis":
    st.title("⚠️ Churn Analysis")
    st.pyplot(get_churn_distribution(df))
    st.subheader("High Churn by Plan")
    st.bar_chart(churn_by_plan(df).set_index("plan_type"))

# ==========================
# AI INSIGHTS
# ==========================
elif page == "AI Insights":
    st.title("🧠 AI Insights")
    insights = answer_question(
        df,
        "Summarize key business insights, risks, and recommendations",
    )
    st.success(insights)

# ==========================
# CHATBOT
# ==========================
elif page == "Chatbot":
    st.title("💬 Ask Your Data")
    q = st.text_input("Ask a question")
    if q:
        st.success(answer_question(df, q))

# ==========================
# EXECUTIVE REPORT
# ==========================
elif page == "Executive Report":
    st.title("📄 Executive PDF Report")

    insights = answer_question(
        df,
        "Provide executive summary and action items",
    )

    if st.button("Generate PDF Report"):
        path = generate_executive_report(df, insights)
        with open(path, "rb") as f:
            st.download_button(
                "Download Executive Report",
                f,
                file_name="AI_CRM_Executive_Report.pdf",
            )
