import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

def csv_to_df(input:str):
    df_data=pd.read_csv(input)
    return df_data

df_data=csv_to_df('StudentsPerformance.csv')