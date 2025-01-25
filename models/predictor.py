import numpy as np

def predict_allocation(data):
    """
    Predict peak times and recommend bandwidth allocation strategies.
    """
    peak_times = data.groupby(data['timestamp'].dt.hour)['bandwidth_usage'].mean()
    recommendations = {
        "Peak Hours": peak_times.idxmax(),
        "Recommended Allocation": f"Allocate more resources between {peak_times.idxmax()} and {peak_times.idxmax()+1} hours"
    }
    return recommendations
