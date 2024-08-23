import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    def __init__(self, data):
        self.data = data
    # Data visualization methods
    
    def plot_correlation_heatmap(self,columns):
        # Create a correlation heatmap
        corr = self.data[columns].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()
        
    def plot_pairplot(self,columns):
        """
        Plots a pairplot for the specified columns in the dataframe to visualize pairwise relationships.
        
        Parameters:
        columns (list): List of columns to include in the pairplot.
        """
        sns.pairplot(self.data[columns], kind='reg', plot_kws={'line_kws':{'color':'red'}})
        plt.suptitle('Pair Plot of Selected Features', y=1.02)
        plt.show()
    def plot_scatter_matrix(self, columns):
        """
        Plots a scatter matrix for the specified columns in the dataframe to visualize relationships.
        
        Parameters:
        columns (list): List of columns to include in the scatter matrix.
        """
        pd.plotting.scatter_matrix(self.data[columns], figsize=(12, 12), diagonal='kde', marker='o', alpha=0.8)
        plt.suptitle('Scatter Matrix of Selected Features', y=1.02)
        plt.show()

    def polar_plot(self, column):
        # Create a polar plot for a specified column
        values = self.data[column]
        angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)
        plt.polar(angles, values)
        plt.title(f"Polar Plot for {column}")
        plt.show()
        
    def histogram(self, columns,bins=30):
        """
        Plots histograms for the specified variables in the DataFrame.
        
        Parameters:
        - columns: List of column names to plot histograms for
        - bins: Number of bins for the histograms (default is 30)
        """
        plt.figure(figsize=(10, 6))

        for i, var in enumerate(columns, 1):
            plt.subplot(2, (len(columns) + 1) // 2, i)
            plt.hist(self.data[var], bins=bins, color='skyblue', edgecolor='black')
            plt.title(f'Histogram of {var}')
            plt.xlabel(var)
            plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()
    
    def bubble_chart(self, x_column, y_column, size_column):
        # Create a bubble chart for two specified columns
        plt.scatter(self.data[x_column], self.data[y_column], s=self.data[size_column] * 10, alpha=0.5)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"Bubble Chart for {x_column} vs {y_column}")
        plt.show()
    
    # Define the Polar Plot Function
    def plot_wind_polar(self, wind_speed_col, wind_direction_col):
        """
        Plots a polar plot for wind speed and direction to identify trends and significant wind events.
        
        Parameters:
        df (DataFrame): The dataframe containing the data.
        wind_speed_col (str): The column name for wind speed.
        wind_direction_col (str): The column name for wind direction.
        """
        # Convert wind direction from degrees to radians for the polar plot
        wind_direction_radians = np.deg2rad(self.data[wind_direction_col])
        
        # Create the polar plot
        plt.figure(figsize=(8, 8))
        ax = plt.subplot(111, polar=True)
        
        # Plot wind speed as a function of wind direction
        sc = ax.scatter(wind_direction_radians, self.data[wind_speed_col], 
                        c=self.data[wind_speed_col], cmap='viridis', alpha=0.75, s=10)
        
        # Add color bar to indicate wind speed intensity
        plt.colorbar(sc, label='Wind Speed (m/s)')
        
        # Set labels and title
        ax.set_theta_zero_location('N')  # North at the top
        ax.set_theta_direction(-1)  # Clockwise direction
        ax.set_title('Wind Speed and Direction Polar Plot')
        ax.set_rlabel_position(90)  # Position the radial labels
        
        plt.show()
