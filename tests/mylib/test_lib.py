import unittest
from unittest.mock import patch
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from mylib.lib import create_save_visualization, read_dataset


class TestLibFunctions(unittest.TestCase):

    @patch("matplotlib.pyplot.savefig")
    def test_create_save_visualization_hist(self, mock_savefig):
        """Test create_save_visualization for histogram plot"""
        # Create a mock dataframe
        df = pd.DataFrame({"value": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

        # Call the function for histogram plot
        create_save_visualization(
            df,
            column_name="value",
            save_filename="test_hist.png",
            show=False,
            plot_type="hist",
        )

        # Ensure the file is saved
        mock_savefig.assert_called_once_with("test_hist.png", bbox_inches="tight")
        plt.close("all")

    @patch("matplotlib.pyplot.savefig")
    def test_create_save_visualization_bar(self, mock_savefig):
        """Test create_save_visualization for bar plot"""
        # Create a mock dataframe
        df = pd.DataFrame(
            {
                "city": [
                    "New York",
                    "Los Angeles",
                    "Chicago",
                    "New York",
                    "Chicago",
                    "New York",
                ]
            }
        )

        # Call the function for bar plot with top_n=2
        create_save_visualization(
            df,
            column_name="city",
            save_filename="test_bar.png",
            show=False,
            plot_type="bar",
            top_n=2,
        )

        # Ensure the file is saved
        mock_savefig.assert_called_once_with("test_bar.png", bbox_inches="tight")
        plt.close("all")

    def test_read_dataset(self):
        """Test read_dataset function"""
        # Mock CSV data using StringIO
        mock_file_data = StringIO(
            """city\tstate\tzip
New York\tNY\t10001
Los Angeles\tCA\t90001
Chicago\tIL\t60601
"""
        )

        # Call read_dataset with the mock CSV data
        with patch(
            "pandas.read_csv", return_value=pd.read_csv(mock_file_data, sep="\t")
        ) as mock_read_csv:
            df = read_dataset("mock_file_path.tsv")

            # Check if pandas.read_csv was called with the correct parameters
            mock_read_csv.assert_called_once_with(
                "mock_file_path.tsv", sep="\t", encoding="utf-16", on_bad_lines="skip"
            )

            # Check the DataFrame shape and columns
            self.assertEqual(df.shape, (3, 3))
            self.assertListEqual(list(df.columns), ["city", "state", "zip"])


if __name__ == "__main__":
    unittest.main()
