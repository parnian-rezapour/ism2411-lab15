# Exercise 1 - Q1: Revenue by region

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean_sales.csv", parse_dates=["order_date"])

revenue_by_region = (
df.groupby("region")["revenue"]
.sum()
.reset_index()
.sort_values("revenue", ascending=False)
)

print(revenue_by_region)

plt.figure(figsize=(8, 5))
plt.bar(revenue_by_region["region"], revenue_by_region["revenue"])
plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig("charts/q1_revenue_by_region.png")
plt.close()
# South generated the highest total revenue at $605,454.95.

# Exercise 2 - Q2: Monthly revenue trend

df["month"] = df["order_date"].dt.month

monthly_revenue = (
df.groupby("month")["revenue"]
.sum()
.reset_index()
)

print(monthly_revenue)

plt.figure(figsize=(8, 5))
plt.plot(
monthly_revenue["month"],
monthly_revenue["revenue"],
marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue ($)")
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig("charts/q2_monthly_trend.png")
plt.close()
# December had the highest revenue at $199,684.11, about 26.48% above the monthly average.