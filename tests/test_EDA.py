import unittest
import numpy as np
import pandas as pd
import sys 
sys.path.insert(0, '/Kiffya_10_acc/SolarStrategy-Insight/scripts/')
from scripts.Moonlight_EDA import DataPreprocessor


# test class for the DataPreprocessor class
class Test_DataPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = DataPreprocessor('../data/benin-malanville.csv')
        self.df_with_missing = pd.DataFrame({
            'A': [1, 2, None],
            'B': [4, None, 6],
            'C': [None, 8, 9]
        })
        self.df_without_missing = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        # self.preprocessor = DataPreprocessor(pd.DataFrame()) 
    def test_check_missing_values_with_missing(self):
        # Arrange
        self.preprocessor.data = self.df_with_missing  # Set the internal data
        expected_output = pd.Series([1, 1, 1], index=['A', 'B', 'C'])

        # Act
        result = self.preprocessor.check_missing_values()

        # Assert
        pd.testing.assert_series_equal(result, expected_output)

    def test_check_missing_values_without_missing(self):
        # Arrange
        self.preprocessor.data = self.df_without_missing  # Set the internal data
        expected_output = pd.Series([0, 0, 0], index=['A', 'B', 'C'])

        # Act
        result = self.preprocessor.check_missing_values()

        # Assert
        pd.testing.assert_series_equal(result, expected_output)
if __name__ == '__main__':
    unittest.main()