import pandas as pd
from core.llm import ask_llm_about_data

def answer_question(df: pd.DataFrame, question: str) -> str:
    if df is None or df.empty:
        return "No data available. Please upload a dataset."

    if not question.strip():
        return "Please enter a valid question."

    return ask_llm_about_data(df, question)
