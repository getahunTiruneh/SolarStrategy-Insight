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
        # Ensure data is sorted by timestamp
        self.data = self.data.sort_values(by='Timestamp')
        
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
        
    def correlation_numeric(self):
        # Select only numeric columns for correlation
        numeric_data = self.data.select_dtypes(include=['number'])
        corr_matrix = numeric_data.corr()
        return corr_matrix
    
    def correlation_of_columns(self, column1, column2):
        # Calculate the correlation between two specified columns
        correlation = self.data[column1].corr(self.data[column2])
        return correlation
    
    def detect_outliers(self, column):
        threshold=3
        # Detect outliers in a specified column using Z-score method.
        mean = self.data[column].mean()
        std_dev = self.data[column].std()
        z_scores = (self.data[column] - mean) / std_dev
        outliers = self.data[np.abs(z_scores) > threshold]
        return outliers
    def check_incorrect_values(self):
        # Check for incorrect values in specific columns
        incorrect_values = (self.data[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']] < 0).sum()
        return incorrect_values