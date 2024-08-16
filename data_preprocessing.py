# data_preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Handle missing values
    data = data.dropna()

    # Feature scaling
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[['churn_rate', 'cpi', 'cpm']])
    data[['churn_rate', 'cpi', 'cpm']] = scaled_data

    return data

if __name__ == "__main__":
    file_path = 'metrics_data.csv'
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    processed_data.to_csv('processed_data.csv', index=False)
