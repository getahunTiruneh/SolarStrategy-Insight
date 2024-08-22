import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataPreprocessor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
         # Load the CSV file and store it in the data attribute
        self.data = pd.read_csv(self.file_path)

    def check_missing_values(self,df):
        self.missing_data = df.isnull().sum()
        return self.missing_data
        
    def correlation(self):
        # Select only numeric columns for correlation
        numeric_data = self.data.select_dtypes(include=['number'])
        corr_matrix = numeric_data.corr()
        return corr_matrix
