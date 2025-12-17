import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# KPI CALCULATIONS
# ==========================
def get_kpis(df: pd.DataFrame) -> dict:
    total_customers = len(df)
    total_revenue = df["monthly_revenue"].sum()

    churn_rate = round(
        (df[df["churn_risk"] == "High"].shape[0] / total_customers) * 100, 2
    )

    avg_logins = round(df["logins_last_30_days"].mean(), 2)
    high_churn_users = df[df["churn_risk"] == "High"].shape[0]

    return {
        "customers": total_customers,
        "revenue": total_revenue,
        "churn_rate": churn_rate,
        "avg_logins": avg_logins,
        "high_churn": high_churn_users,
    }

# ==========================
# FUNNEL DATA
# ==========================
def get_funnel_data(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("stage")
        .size()
        .reset_index(name="users")
        .sort_values("users", ascending=False)
    )

def funnel_conversion(df: pd.DataFrame) -> pd.DataFrame:
    funnel = df.groupby("stage").size().reset_index(name="users")
    funnel["conversion_%"] = (funnel["users"] / funnel["users"].max() * 100).round(2)
    return funnel

# ==========================
# CHURN ANALYTICS
# ==========================
def get_churn_distribution(df: pd.DataFrame):
    churn_counts = df["churn_risk"].value_counts()

    fig, ax = plt.subplots()
    ax.pie(
        churn_counts.values,
        labels=churn_counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title("Churn Risk Distribution")
    return fig

def churn_by_plan(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df[df["churn_risk"] == "High"]
        .groupby("plan_type")
        .size()
        .reset_index(name="high_churn_users")
    )

# ==========================
# REVENUE ANALYTICS
# ==========================
def revenue_by_plan(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("plan_type")["monthly_revenue"]
        .sum()
        .reset_index()
    )
