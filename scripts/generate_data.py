# =================== FIX IMPORT PATH (MUST BE FIRST) ===================
import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# =================== NOW SAFE TO IMPORT APP MODULES ===================
import random
import pandas as pd
from faker import Faker
from app.db import engine

fake = Faker()

# =================== GENERATE LEADS ===================
leads = []
NUM_LEADS = 800

for i in range(1, NUM_LEADS + 1):
    leads.append({
        "lead_id": i,
        "created_date": fake.date_between("-6M", "today"),
        "stage": random.choices(
            ["New", "Contacted", "Demo", "Paid"],
            weights=[45, 30, 15, 10]
        )[0],
        "source": random.choice(
            ["Website", "Ads", "Referral", "Outbound"]
        )
    })

df_leads = pd.DataFrame(leads)

# =================== GENERATE ACTIVITIES ===================
activities = []
activity_id = 1

for lead in leads:
    for _ in range(random.randint(0, 20)):
        activities.append({
            "activity_id": activity_id,
            "lead_id": lead["lead_id"],
            "activity_type": random.choice(
                ["Call", "Email", "Demo", "Meeting"]
            ),
            "activity_date": fake.date_between(
                lead["created_date"], "today"
            )
        })
        activity_id += 1

df_activities = pd.DataFrame(activities)

# =================== GENERATE SUBSCRIPTIONS ===================
subscriptions = []

for lead in leads:
    if lead["stage"] == "Paid":
        start_date = fake.date_between("-6M", "-1M")
        churned = random.choice([0, 1])

        subscriptions.append({
            "lead_id": lead["lead_id"],
            "start_date": start_date,
            "end_date": fake.date_between(start_date, "today")
                        if churned else None,
            "monthly_revenue": random.choice([1999, 2999, 4999])
        })

df_subs = pd.DataFrame(subscriptions)

# =================== WRITE TO DATABASE ===================
with engine.begin() as conn:
    df_leads.to_sql("leads", conn, if_exists="replace", index=False)
    df_activities.to_sql("activities", conn, if_exists="replace", index=False)
    df_subs.to_sql("subscriptions", conn, if_exists="replace", index=False)

print("✅ Database generated successfully")
print(f"Leads: {len(df_leads)}")
print(f"Activities: {len(df_activities)}")
print(f"Subscriptions: {len(df_subs)}")
