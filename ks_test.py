"""
Kolmogorov-Smirnov tests: 

    Nonparametric test that compares the cumulative distributions of two data sets, in this case, the training data and the
    post-training data. The null hypothesis for this test states that the data distributions from both the datasets are same. 
    If the null is rejected then we can conclude that there is adrift in the model.

"""

import numpy as np
import pandas as pd

from scipy import stats

# Import your data here
df = pd.read_csv('Churn_Modelling.csv')
df.head()
df.drop(['RowNumber','CustomerId','Surname'],axis=1,inplace=True)
df_numerical=df.iloc[:,[3,4,5,9]]
df_numerical.head()
df_salary_low=df_numerical[df_numerical['EstimatedSalary']<=10000] 
df_salary_high=df_numerical[df_numerical['EstimatedSalary']>10000]

#splitting the data to analyze the difference in both the datasets

p_value = 0.05

rejected = 0

for col in df_numerical.columns:

    test = stats.ks_2samp(df_salary_low[col], df_salary_high[col])

    if test[1] < p_value:

        rejected += 1
        print("Column rejected, col")

print("We rejected", rejected, "columns in total")