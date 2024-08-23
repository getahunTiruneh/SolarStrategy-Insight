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
        
    # Calculate and return summary statistics for numeric columns
    def summary_statistics(self):
        stats=self.data.describe().T
        return stats
    
    #Perform data quality checks including missing values and negative values
    def data_quality_check(self):
        
        quality_report = pd.DataFrame()
        
        # Check for missing values
        missing_values = self.data.isna().sum()
        
        # Check for negative values in specific columns
        negative_values = (self.data[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']] < 0).sum()
        
        # Compile the report
        quality_report['Missing Values'] = missing_values
        quality_report['Negative Values'] = negative_values
        
        return quality_report
    def check_missing_values(self):
        self.missing_data = self.data.isnull().sum()
        return self.missing_data
        
    def correlation(self):
        # Select only numeric columns for correlation
        numeric_data = self.data.select_dtypes(include=['number'])
        corr_matrix = numeric_data.corr()
        return corr_matrix
