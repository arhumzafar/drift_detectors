"""
Page-Hinkley Test:

    This method calculates the mean of the observed values and keeps updating the mean as and 
    when new data arrives. A drift is detected if the observed mean at some instant is greater 
    than a threshold value lambda

"""
import numpy as np
from river.drift import PageHinkley

np.random.seed(123)
ph = PageHinkley(threshold=10, min_instances=10)

# Update the drift detector and verify if changes is detected
for col in df_numerical.columns:
    data_stream = []
    a = np.array(df_salary_low[col])
    b = np.array(df_salary_high[col])
    data_stream = np.concatenate((a,b))
    for i, val in enumerate(data_stream):
        in_drift, in_warning = ph.update(val)
        if in_drift:
            print(f"Change detected at index {i} for column: {col} with input value: {val}")