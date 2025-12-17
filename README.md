

# 🚀 AI-Powered CRM Analytics Platform

An **end-to-end CRM analytics dashboard** that enables businesses to analyze customer funnels, churn risk, revenue performance, and engagement metrics — enhanced with an **AI copilot** that generates executive insights and answers data-driven questions in natural language.

Built with **Python, Streamlit, Pandas, and Groq LLMs**, this project mirrors real-world SaaS analytics platforms used by companies like **LeadSquared, Salesforce, and HubSpot**.

---

## 📌 Key Features

### 🔐 Authentication

* Simple login system to simulate gated enterprise dashboards
* use admin@crm.com and admin123 as id and pass

### 📁 Data Ingestion

* Upload CRM data via CSV
* Safe schema validation (no crashes on bad data)
* Graceful handling when no data is provided

### 📊 Analytics Dashboard

* **KPIs**: Customers, Revenue, Churn Rate, Engagement
* **Funnel Analysis**: Stage-wise user drop-off & conversion rates
* **Churn Analysis**:

  * Churn risk distribution
  * High-churn segmentation by plan
* **Revenue Insights**:

  * Revenue contribution by plan type

### 🧠 AI Capabilities

* **AI Insights Tab**:

  * Automatically generates executive summaries, risks, and recommendations
* **AI Chatbot**:

  * Ask natural language questions like:

    * *“Why is churn high?”*
    * *“Which segment should sales focus on?”*
    * *“Summarize this for leadership”*
* **Production-safe LLM integration**:

  * Uses Groq LLMs
  * Automatic fallback if models are unavailable
  * App never crashes due to AI failures

### 📄 Executive Reporting

* One-click **PDF executive report generation**
* Includes dataset overview + AI-generated insights
* Ready to share with stakeholders

---

## 🧱 Architecture Overview

```
churn-analysis/
│
├── main.py                 # Streamlit application entry point
│
├── core/
│   ├── analytics.py        # KPI, funnel, churn, revenue analytics
│   ├── chatbot.py          # AI chatbot interface
│   ├── llm.py              # Groq LLM integration with fallback logic
│   └── report.py           # Executive PDF report generator
│
├── assets/
│   └── bg.jpg              # Background image (optional UI polish)
│
├── data/                   # Optional SQLite DB (future extension)
│
├── requirements.txt
└── README.md
```

**Design Principles**

* Modular & maintainable
* Defensive programming (no hard crashes)
* Clear separation of concerns
* Production-style error handling

---

## 📂 Expected Dataset Schema

Your CRM CSV should contain the following columns:

| Column Name           | Description                                     |
| --------------------- | ----------------------------------------------- |
| `customer_id`         | Unique customer identifier                      |
| `plan_type`           | Subscription plan (e.g., Free, Pro, Enterprise) |
| `monthly_revenue`     | Monthly revenue from customer                   |
| `logins_last_30_days` | Engagement metric                               |
| `churn_risk`          | Low / Medium / High                             |
| `stage`               | Funnel stage (Lead, Trial, Paid, etc.)          |

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend / Logic**: Python
* **Data Processing**: Pandas
* **Visualization**: Streamlit Charts + Matplotlib
* **AI / LLM**: Groq (Model-agnostic, fallback enabled)
* **Reporting**: ReportLab (PDF generation)

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone <repo-url>
cd churn-analysis
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Groq API Key (Optional but Recommended)

```bash
setx GROQ_API_KEY "your_groq_api_key"
```

> Restart VS Code / terminal after setting the key.

### 5️⃣ Run the App

```bash
streamlit run main.py
```

---

## 🧪 Sample Use Cases

* Product managers analyzing funnel drop-offs
* Sales teams identifying high-risk churn segments
* Founders generating executive summaries for board meetings
* Analysts practicing real-world SaaS analytics workflows

---

## 🧠 What This Project Demonstrates

* Real-world **SaaS analytics thinking**
* Strong **data analysis fundamentals**
* Responsible **AI integration** (fallbacks, safety)
* Clean **Python architecture**
* Ability to translate data → business insights

---

## 🎯 Resume-Ready Description

> Built an AI-powered CRM analytics platform featuring KPI dashboards, funnel and churn analysis, revenue segmentation, and an LLM-based analytics copilot. Implemented real-time CSV ingestion, executive PDF reporting, and production-safe AI integration using Python, Streamlit, Pandas, and Groq LLMs.

---

## 🚀 Future Enhancements (Optional)

* Cohort & retention analysis
* Forecasting & trend prediction
* User role-based access
* Cloud deployment (Streamlit Cloud / HuggingFace Spaces)

---

## 🙌 Author

**Devyansh Singh**
B.Tech (CSE) | Analytics & AI Enthusiast


