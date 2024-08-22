import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self, data):
        self.data = data
    # Data visualization methods
    def plot_heatmap(self):
        plt.imshow(self.data.select_dtypes(include=['float64', 'int64']).corr(), cmap='viridis', interpolation='nearest')
        plt.colorbar()
        plt.title("Heatmap of Correlation Matrix")
        plt.show()
    def plot_scatter(self, x, y):
        plt.scatter(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f"Scatter plot for {x} vs {y}")
        plt.show()
    def plot_boxplot(self, column):
        plt.boxplot(self.data[column])
        plt.title(f"Boxplot for {column}")
        plt.xlabel(column)
        plt.show()
    def plot_histogram(self, column):
        plt.hist(self.data[column], bins=20)
        plt.title(f"Histogram for {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()