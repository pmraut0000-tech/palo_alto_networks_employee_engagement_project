import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "employee_engagement_synthetic.csv"

if not any(k in os.environ for k in ("STREAMLIT_RUN_MAIN", "STREAMLIT_SERVER", "STREAMLIT_RUN", "STREAMLIT_ENV")):
    print("Please run this app with: streamlit run app.py")
    sys.exit(0)

import streamlit as st

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Employee Engagement Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# Title
# -------------------------------------------------
st.title("📊 Employee Engagement, Satisfaction & Burnout Analysis")
st.subheader("Palo Alto Networks — Illustrative HR Analytics Project")

st.info(
    "Note: This dashboard uses synthetic data created for academic/portfolio purposes. "
    "It does not contain real Palo Alto Networks employee data."
)

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.error(
        "Dataset not found. Make sure the following file exists:\n\n"
        "data/employee_engagement_synthetic.csv"
    )
    st.stop()

# -------------------------------------------------
# Sidebar Filters
# -------------------------------------------------
st.sidebar.header("🔎 Filters")

departments = ["All"] + sorted(df["Department"].unique().tolist())

selected_department = st.sidebar.selectbox(
    "Select Department",
    departments
)

if selected_department != "All":
    filtered_df = df[df["Department"] == selected_department].copy()
else:
    filtered_df = df.copy()

# -------------------------------------------------
# KPI Section
# -------------------------------------------------
st.header("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Engagement Score",
        f"{filtered_df['Engagement_Score'].mean():.2f} / 5"
    )

with col2:
    st.metric(
        "Satisfaction Score",
        f"{filtered_df['Satisfaction_Score'].mean():.2f} / 5"
    )

with col3:
    st.metric(
        "Burnout Score",
        f"{filtered_df['Burnout_Score'].mean():.2f} / 5"
    )

with col4:
    st.metric(
        "Intent to Stay",
        f"{filtered_df['Intent_to_Stay'].mean():.2f} / 5"
    )

# -------------------------------------------------
# Burnout Risk
# -------------------------------------------------
st.header("🔥 Burnout Risk")

burnout_counts = filtered_df["Burnout_Risk"].value_counts()

col1, col2 = st.columns(2)

with col1:
    st.dataframe(
        burnout_counts.rename("Employees"),
        width='stretch'
    )

with col2:
    fig, ax = plt.subplots()

    burnout_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Burnout Risk Distribution")
    ax.set_xlabel("Burnout Risk")
    ax.set_ylabel("Number of Employees")

    plt.xticks(rotation=0)
    st.pyplot(fig)

# -------------------------------------------------
# Department Analysis
# -------------------------------------------------
st.header("🏢 Department Analysis")

department_summary = (
    df.groupby("Department")[
        [
            "Engagement_Score",
            "Satisfaction_Score",
            "Burnout_Score",
            "Intent_to_Stay"
        ]
    ]
    .mean()
    .round(2)
)

st.dataframe(
    department_summary,
    width='stretch'
)

# -------------------------------------------------
# Burnout by Department
# -------------------------------------------------
st.subheader("Burnout Score by Department")

burnout_department = (
    df.groupby("Department")["Burnout_Score"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 5))

burnout_department.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Average Burnout Score by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Burnout Score")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# -------------------------------------------------
# Weekly Hours vs Burnout
# -------------------------------------------------
st.header("⏰ Workload and Burnout")

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(
    filtered_df["Weekly_Hours"],
    filtered_df["Burnout_Score"],
    alpha=0.5
)

ax.set_title("Weekly Working Hours vs Burnout")
ax.set_xlabel("Weekly Working Hours")
ax.set_ylabel("Burnout Score")

st.pyplot(fig)

# -------------------------------------------------
# Engagement vs Intent to Stay
# -------------------------------------------------
st.header("📈 Engagement and Retention")

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(
    filtered_df["Engagement_Score"],
    filtered_df["Intent_to_Stay"],
    alpha=0.5
)

ax.set_title("Engagement vs Intent to Stay")
ax.set_xlabel("Engagement Score")
ax.set_ylabel("Intent to Stay")

st.pyplot(fig)

# -------------------------------------------------
# Employee Experience Factors
# -------------------------------------------------
st.header("👥 Employee Experience Factors")

factor_columns = [
    "Manager_Support",
    "Recognition",
    "Career_Growth",
    "Work_Life_Balance",
    "Psychological_Safety",
    "Compensation_Satisfaction"
]

factor_means = filtered_df[factor_columns].mean().sort_values()

fig, ax = plt.subplots(figsize=(9, 5))

factor_means.plot(
    kind="barh",
    ax=ax
)

ax.set_title("Average Employee Experience Factors")
ax.set_xlabel("Average Score")
ax.set_ylabel("Factor")

st.pyplot(fig)

# -------------------------------------------------
# Correlation Analysis
# -------------------------------------------------
st.header("🔗 Correlation Analysis")

correlation_columns = [
    "Engagement_Score",
    "Satisfaction_Score",
    "Burnout_Score",
    "Intent_to_Stay",
    "Manager_Support",
    "Recognition",
    "Career_Growth",
    "Work_Life_Balance",
    "Psychological_Safety",
    "Compensation_Satisfaction",
    "Weekly_Hours"
]

correlation_matrix = (
    filtered_df[correlation_columns]
    .corr()
    .round(2)
)

st.dataframe(
    correlation_matrix,
    width='stretch'
)

# -------------------------------------------------
# Recommendations
# -------------------------------------------------
st.header("💡 HR Diagnostic Recommendations")

st.markdown("""
### Recommended Actions

1. **Monitor burnout**
   - Track burnout risk regularly across departments.
   - Review workload where working hours remain consistently high.

2. **Improve manager support**
   - Encourage regular one-to-one meetings.
   - Provide manager coaching and feedback training.

3. **Strengthen recognition**
   - Introduce consistent employee recognition practices.
   - Recognize both individual and team contributions.

4. **Improve career development**
   - Provide clear career paths.
   - Increase access to learning and development programs.

5. **Support work-life balance**
   - Monitor excessive working hours.
   - Encourage sustainable workload planning.

6. **Build psychological safety**
   - Use anonymous pulse surveys.
   - Encourage employees to raise concerns without fear of negative consequences.
""")

# -------------------------------------------------
# Raw Data
# -------------------------------------------------
st.header("📄 Employee Data")

st.dataframe(
    filtered_df,
    width='stretch'
)

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")

st.caption(
    "Employee Engagement, Satisfaction & Burnout Diagnostic Analysis | "
    "Synthetic academic dataset"
)