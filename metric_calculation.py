# metric_calculation.py
import pandas as pd

def calculate_metrics(data):
    # Example calculations (these can be more complex depending on the data)
    churn_rate = data['churned_users'] / data['total_users']
    cpi = data['marketing_cost'] / data['installs']
    cpm = (data['ad_revenue'] / data['impressions']) * 1000

    data['churn_rate'] = churn_rate
    data['cpi'] = cpi
    data['cpm'] = cpm

    return data

if __name__ == "__main__":
    data = pd.read_csv('processed_data.csv')
    metrics_data = calculate_metrics(data)
    metrics_data.to_csv('metrics_data.csv', index=False)
