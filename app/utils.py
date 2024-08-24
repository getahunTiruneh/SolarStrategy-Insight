import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

class ExploratoryDataAnalysis:
    def __init__(self, data):
        self.data = data
        self._convert_dates()
    
    def _convert_dates(self):
        # Convert columns with date strings to datetime
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                try:
                    self.data[column] = pd.to_datetime(self.data[column], errors='ignore')
                except Exception as e:
                    pass  # Skip columns that cannot be converted
    
    def check_missing_values(self):
        return self.data.isnull().sum()

    def describe_data(self):
        return self.data.describe(include='all')

    def box_plot(self, column):
        if self.data[column].dtype in [np.float64, np.int64]:
            self.data.boxplot(column=column)
            plt.title(f'Box Plot of {column}')
        else:
            plt.text(0.5, 0.5, 'Column is not numeric', horizontalalignment='center', verticalalignment='center')
        plt.show()

    def histogram(self, column):
        if self.data[column].dtype in [np.float64, np.int64]:
            self.data[column].hist()
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
        else:
            plt.text(0.5, 0.5, 'Column is not numeric', horizontalalignment='center', verticalalignment='center')
        plt.show()

    def scatter_plot(self, x, y):
        if (self.data[x].dtype in [np.float64, np.int64]) and (self.data[y].dtype in [np.float64, np.int64]):
            self.data.plot.scatter(x=x, y=y)
            plt.title(f'Scatter Plot of {x} vs {y}')
            plt.xlabel(x)
            plt.ylabel(y)
        else:
            plt.text(0.5, 0.5, 'One or both columns are not numeric', horizontalalignment='center', verticalalignment='center')
        plt.show()

    def correlation_matrix(self):
        # Only include numeric columns for correlation matrix
        numeric_data = self.data.select_dtypes(include=[np.number])
        return numeric_data.corr()
