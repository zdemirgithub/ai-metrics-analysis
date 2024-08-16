# data_visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    plt.figure(figsize=(10, 6))

    sns.lineplot(data=data, x='date', y='churn_rate', label='Churn Rate')
    sns.lineplot(data=data, x='date', y='cpi', label='CPI')
    sns.lineplot(data=data, x='date', y='cpm', label='CPM')

    plt.title('Metrics Over Time')
    plt.xlabel('Date')
    plt.ylabel('Metrics')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('metrics_data.csv')
    visualize_data(data)
