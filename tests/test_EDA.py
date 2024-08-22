import unittest
import numpy as np
import pandas as pd
from scripts.Moonlight_EDA import DataPreprocessor

# test class for the DataPreprocessor class
class Test_DataPreprocessor(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        self.preprocessor = DataPreprocessor(self.data)
    
    def test_load_data(self):
        # Define
        expected_data = self.data
        # Act
        actual_data = self.preprocessor.data
        # Assert
        self.assertTrue(np.array_equal(actual_data, expected_data))

    def test_check_missing_values(self):
        self.assertFalse(self.preprocessor.check_missing_values().any())
if __name__ == '__main__':
    unittest.main()