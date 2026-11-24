# Self-Assessment
#
# 1. Yes. The charts are clear enough that someone could identify the key finding quickly.
# The titles and labels make the comparisons easy to understand, and the custom return-rate
# chart is sorted from highest to lowest, which makes the main result obvious.
#
# 2. South generated $605,454.95 in revenue, about 28.61% above the average regional revenue.
# December generated $199,684.11 in revenue, about 26.48% above the average monthly revenue.
# The mean order size was about $409.32, while the median was $144.99, showing a strongly
# right-skewed distribution in which a small number of large orders pull the mean upward.
#
# 3. The most difficult part was deciding how to interpret the data rather than just creating
# the charts. I had to think carefully about what negative revenue represented and how to turn
# that observation into a meaningful business question about return rates.


# Exercise 1 - Q1: Revenue by region
# Business question: Which region generates the most total revenue?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/clean_sales.csv", parse_dates=["order_date"])

revenue_by_region = (
df.groupby("region")["revenue"]
.sum()
.reset_index()
.sort_values("revenue", ascending=False)
)

print(revenue_by_region)

plt.figure(figsize=(8, 5))
sns.barplot(
data=revenue_by_region,
x="region",
y="revenue"
)
plt.title("Total Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig("charts/q1_revenue_by_region.png")
plt.close()
# South generated the highest total revenue at $605,454.95.

# Exercise 2 - Q2: Monthly revenue trend
# Business question: How does total revenue change across the 12 months?

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

# Exercise 3 - Q3: Order size distribution
# Business question: What does the distribution of order sizes look like?

mean_order = df["revenue"].mean()
median_order = df["revenue"].median()

print("Mean order size:", mean_order)
print("Median order size:", median_order)

plt.figure(figsize=(8, 5))
plt.hist(df["revenue"], bins=20)
plt.title("Order Size Distribution")
plt.xlabel("Revenue ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/q3_order_distribution.png")
plt.close()
# The order-size distribution is right-skewed, so a few large orders pull the mean above the typical order size; the median is more representative for a business analyst.

# Exercise 4 - Q4: Custom business question
# Business question: Which product categories have the highest return rates?

df["is_return"] = df["revenue"] < 0

return_rate_by_category = (
df.groupby("product_category")["is_return"]
.mean()
.mul(100)
.reset_index(name="return_rate")
.sort_values("return_rate", ascending=False)
)

print(return_rate_by_category)

plt.figure(figsize=(9, 5))
plt.bar(
return_rate_by_category["product_category"],
return_rate_by_category["return_rate"]
)
plt.title("Return Rate by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Return Rate (%)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/q4_custom.png")
plt.close()
# Electronics had the highest return rate about 2.25%, while Appliances had the lowest at about 1.12%.

# Exercise 5 - Seaborn version

# Q1 was replaced with a Seaborn barplot.
# Compared with plt.bar(), Seaborn's barplot lets me specify the DataFrame
# and column names directly, which makes the chart code easier to read.

# Exercise 6 - Multiple aggregations

region_summary = (
df.groupby("region")
.agg(
total_revenue=("revenue", "sum"),
order_count=("revenue", "count")
)
.reset_index()
)

region_summary["average_order_value"] = (
region_summary["total_revenue"] / region_summary["order_count"]
)

print(region_summary)
# South has the most orders with 1,465.
# North has the highest average order value at about $454.00.

# Exercise 7 - Script tidy-up
# Added a clear section heading and business question before each chart block.