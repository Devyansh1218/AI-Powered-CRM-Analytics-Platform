GET_ALL_CUSTOMERS = """
SELECT *
FROM customers;
"""

FUNNEL_COUNTS = """
SELECT stage, COUNT(*) AS users
FROM customers
GROUP BY stage
ORDER BY users DESC;
"""

CHURN_DISTRIBUTION = """
SELECT churn_risk, COUNT(*) AS users
FROM customers
GROUP BY churn_risk;
"""

REVENUE_BY_PLAN = """
SELECT plan_type, SUM(monthly_revenue) AS revenue
FROM customers
GROUP BY plan_type;
"""
