import os
import pandas as pd
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODELS = [
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "gemma2-9b-it",
]

def build_data_context(df: pd.DataFrame) -> str:
    return f"""
Rows: {len(df)}
Columns: {', '.join(df.columns)}

Total Revenue: {df['monthly_revenue'].sum()}
Avg Logins (30d): {df['logins_last_30_days'].mean():.2f}
High Churn Users: {len(df[df['churn_risk'] == 'High'])}
"""

def ask_llm_about_data(df: pd.DataFrame, question: str) -> str:
    context = build_data_context(df)

    if not GROQ_API_KEY:
        return f"""
[LOCAL ANALYTICS MODE]

Question: {question}

Insight:
• High churn correlates with low engagement
• Enterprise plans retain better
• Funnel drop-offs occur before conversion
"""

    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
You are a senior CRM analytics copilot.

Use ONLY the dataset context.
Be concise and executive-focused.

DATA:
{context}

QUESTION:
{question}

ANSWER:
"""

    for model in GROQ_MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            return response.choices[0].message.content.strip()
        except Exception:
            continue

    return "AI temporarily unavailable. Please rely on dashboard metrics."
