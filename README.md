# Employee Engagement, Satisfaction, and Burnout Diagnostic Analysis at Palo Alto Networks

## Project Purpose
This project demonstrates an HR/People Analytics diagnostic workflow focused on three major employee experience outcomes:

1. Employee Engagement
2. Employee Satisfaction
3. Burnout Risk

The case is framed around Palo Alto Networks for academic and portfolio purposes.

> **Data disclaimer:** The dataset in this project is fully synthetic and does not represent real, confidential, or internal Palo Alto Networks employee information.

## Business Questions
- What is the overall level of employee engagement and satisfaction?
- Which departments show elevated burnout risk?
- What employee-experience factors are most strongly associated with engagement?
- How are workload and burnout related?
- Which factors appear most connected to employees' intent to stay?
- What practical HR interventions should be prioritized?

## Dataset
`data/employee_engagement_synthetic.csv`

The dataset contains 500 synthetic employee records with:
- Department
- Role level
- Tenure
- Work mode
- Weekly hours
- Manager support
- Recognition
- Career growth
- Work-life balance
- Psychological safety
- Compensation satisfaction
- Engagement
- Satisfaction
- Burnout
- Absence days
- Intent to stay

## Project Structure
```text
palo_alto_networks_employee_engagement_project/
├── data/
│   └── employee_engagement_synthetic.csv
├── notebooks/
│   └── employee_engagement_diagnostic.ipynb
├── outputs/
├── report/
│   └── diagnostic_summary.md
├── src/
│   └── analysis.py
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
python src/analysis.py
```

The script generates:
- KPI averages
- Department summary
- Correlation matrix
- Burnout-by-department chart
- Weekly-hours vs burnout chart
- Engagement vs intent-to-stay chart

## Suggested Tools
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Learning Outcomes
This project demonstrates:
- HR analytics
- exploratory data analysis
- KPI design
- burnout-risk segmentation
- retention diagnostics
- correlation analysis
- data visualization
- business recommendations
