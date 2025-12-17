from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from pathlib import Path
import pandas as pd

def generate_executive_report(df: pd.DataFrame, insights: str) -> str:
    """
    Generates an executive PDF report and returns
    the file path as a STRING (required by ReportLab & Streamlit)
    """

    output_path = Path("executive_report.pdf").resolve()

    doc = SimpleDocTemplate(
        str(output_path),  # ✅ IMPORTANT FIX
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    elements = []

    # ======================
    # TITLE
    # ======================
    elements.append(
        Paragraph("<b>AI CRM Analytics – Executive Report</b>", styles["Title"])
    )
    elements.append(Spacer(1, 16))

    # ======================
    # DATASET OVERVIEW
    # ======================
    elements.append(Paragraph("<b>Dataset Overview</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Total Customers: {len(df)}", styles["Normal"]))
    elements.append(
        Paragraph(f"Total Revenue: {df['monthly_revenue'].sum()}", styles["Normal"])
    )
    elements.append(Spacer(1, 12))

    # ======================
    # AI INSIGHTS
    # ======================
    elements.append(Paragraph("<b>AI-Generated Insights</b>", styles["Heading2"]))
    for line in insights.split("\n"):
        if line.strip():
            elements.append(Paragraph(line, styles["Normal"]))

    # ======================
    # BUILD PDF
    # ======================
    doc.build(elements)

    return str(output_path)  # ✅ Return STRING
