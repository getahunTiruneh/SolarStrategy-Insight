import pandas as pd
import numpy as np

class ExploretaryDataAnalysis:
    def __init__(self, data):
        self.data = data
    # df=pd.read_csv("../data/togo-dapaong_qc.csv")
    # Exploretary data analysis methods
    def check_missing_value(df):
        return df.isnull().sum()
    def describe_data(df):
        return df.describe()
    def box_plot(df, column):
        return df.boxplot(column=column)
    def histogram(df, column):
        return df[column].hist()
    def scatter_plot(df, x, y):
        return df.plot.scatter(x=x, y=y)
    def correlation_matrix(df):
        return df.corr()
    
    
