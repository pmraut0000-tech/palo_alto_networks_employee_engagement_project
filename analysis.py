
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "employee_engagement_synthetic.csv"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

print("\n=== DATASET OVERVIEW ===")
print(df.head())
print("\nShape:", df.shape)

print("\n=== KEY KPI AVERAGES ===")
kpis = ["Engagement_Score", "Satisfaction_Score", "Burnout_Score", "Intent_to_Stay"]
print(df[kpis].mean().round(2))

print("\n=== BURNOUT RISK DISTRIBUTION ===")
print(df["Burnout_Risk"].value_counts(normalize=True).mul(100).round(1).astype(str) + "%")

print("\n=== DEPARTMENT SUMMARY ===")
dept = df.groupby("Department")[kpis].mean().round(2).sort_values("Burnout_Score", ascending=False)
print(dept)
dept.to_csv(OUT / "department_summary.csv")

print("\n=== CORRELATIONS ===")
corr_cols = [
    "Engagement_Score","Satisfaction_Score","Burnout_Score","Intent_to_Stay",
    "Manager_Support","Recognition","Career_Growth","Work_Life_Balance",
    "Psychological_Safety","Compensation_Satisfaction","Weekly_Hours"
]
corr = df[corr_cols].corr().round(2)
print(corr)
corr.to_csv(OUT / "correlation_matrix.csv")

# Chart 1: KPI averages
avg = df[kpis].mean()
plt.figure(figsize=(8,5))
avg.plot(kind="bar")
plt.title("Average Employee Experience KPIs")
plt.ylabel("Score (1-5)")
plt.ylim(0,5)
plt.tight_layout()
plt.savefig(OUT / "kpi_averages.png", dpi=160)
plt.close()

# Chart 2: Burnout by department
burnout_dept = df.groupby("Department")["Burnout_Score"].mean().sort_values(ascending=False)
plt.figure(figsize=(9,5))
burnout_dept.plot(kind="bar")
plt.title("Average Burnout Score by Department")
plt.ylabel("Burnout Score (1-5)")
plt.tight_layout()
plt.savefig(OUT / "burnout_by_department.png", dpi=160)
plt.close()

# Chart 3: Weekly hours vs burnout
plt.figure(figsize=(8,5))
plt.scatter(df["Weekly_Hours"], df["Burnout_Score"], alpha=0.45)
plt.title("Weekly Hours vs Burnout")
plt.xlabel("Weekly Hours")
plt.ylabel("Burnout Score")
plt.tight_layout()
plt.savefig(OUT / "weekly_hours_vs_burnout.png", dpi=160)
plt.close()

# Chart 4: Engagement vs intent to stay
plt.figure(figsize=(8,5))
plt.scatter(df["Engagement_Score"], df["Intent_to_Stay"], alpha=0.45)
plt.title("Engagement vs Intent to Stay")
plt.xlabel("Engagement Score")
plt.ylabel("Intent to Stay")
plt.tight_layout()
plt.savefig(OUT / "engagement_vs_intent_to_stay.png", dpi=160)
plt.close()

print("\nOutputs saved in:", OUT)
