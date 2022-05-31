"""
Population Stability Index:

    Compares the distribution of the target variable in the test dataset to
    a training data set that was used to develop the model.



Steps:
    1) Divide the expected (test) dataset and the actual (training dataset) 
    into buckets and define the boundary values of the buckets based on the
    minimum and maximum values of that column in train data.

    2) Calculate the % of observations in each bucket for both expected and actual datasets.

    3) Calculate the PSI as given in the formula

        a) When PSI<=1
            This means there is no change or shift in the distributions of both datasets.

        b) 0.1< PSI<0.2
            This indicates a slight change or shift has occurred.

        c) PSI>0.2
            This indicates a large shift in the distribution has occurred between both datasets.
"""

import numpy as np

def calculate_psi(expected, actual, buckettype='bins', buckets=10, axis=0):


    def psi(expected_array, actual_array, buckets):
        def scale_range (input, min, max):
            input += -(np.min(input))
            input /= np.max(input) / (max - min)
            input += min
            return input
        
        breakpoints = np.arange(0, buckets + 1) / (buckets) * 100
        breakpoints = scale_range(breakpoints, np.min(expected_array), np.max(expected_array))
        expected_percents = np.histogram(expected_array, breakpoints)[0] / len(expected_array)
        actual_percents = np.histogram(actual_array, breakpoints)[0] / len(actual_array)
        def sub_psi(e_perc, a_perc):
            if a_perc == 0:
                a_perc = 0.0001
            if e_perc == 0:
                e_perc = 0.0001

            value = (e_perc - a_perc) * np.log(e_perc / a_perc)
            return(value)

        psi_value = np.sum(sub_psi(expected_percents[i], actual_percents[i])
        for i in range(0, len(expected_percents)))
        return(psi_value)
    


    if len(expected.shape) == 1:
      psi_values = np.empty(len(expected.shape))
    else:
      psi_values = np.empty(expected.shape[axis])
    
    for i in range(0, len(psi_values)):
      psi_values = psi(expected, actual, buckets)
    
    return(psi_values)


## Calculate psi for features
# psi_list = []
# top_feature_list=df_salary_high.columns
# for feature in top_feature_list:
#         # Assuming you have a validation and training set
#         psi_t = calculate_psi(df_salary_high[feature], df_salary_low[feature])
#         psi_list.append(psi_t)      
#         print('Stability index for column ',feature,'is',psi_t)

    