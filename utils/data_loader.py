import pandas as pd

def load_data(file):
    """
    Load and preprocess the bandwidth usage log from an uploaded file.
    """
    data = pd.read_csv(file)
    # Add any necessary preprocessing steps
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    return data
