"""
Adaptive Windowing (ADWIN):

    ADWIN uses a sliding window approach to detect concept drift. 
    Window size is fixed and ADWIN slides the fixed window for detecting any change on the newly arriving data.
    When two sub-windows show distinct means in the new observations the older sub-window is dropped.

"""
import numpy as np
from skmultflow.drift_detection import ADWIN

adwin = ADWIN()

for col in df_numerical.columns:
    data_stream = []
    a = np.array(df_salary_low[col])
    b = np.array(df_salary_high[col])
    data_stream = np.concatenate((a,b))
# Adding stream elements to ADWIN and verifying if drift occurred
    for i in range(len(data_stream)):
        adwin.add_element(data_stream[i])
        if adwin.detected_change():
            print('Change detected in data: ' + str(data_stream[i]) + ' - at index: ' + str(i) +'for column:' + col)