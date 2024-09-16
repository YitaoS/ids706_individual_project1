import unittest
import pandas as pd
from io import StringIO
from script import (
    read_dataset,
    generate_descriptive_stats,
    generate_visualizations,
    generate_markdown_report,
)
from unittest.mock import mock_open, patch


class TestPollingPlaceAnalysis(unittest.TestCase):

    def setUp(self):
        """Sets up a mock dataset to use for testing."""
        self.data = """city\tstate\tzip
        New York\tNY\t10001
        Los Angeles\tCA\t90001
        Chicago\tIL\t60601
        Houston\tTX\t77001
        Phoenix\tAZ\t85001
        """
        # Create a DataFrame to simulate data being read from a file
        self.df = pd.read_csv(StringIO(self.data), sep="\t")

    def test_read_dataset(self):
        """Test the read_dataset function."""
        df = read_dataset(StringIO(self.data))  # Simulate reading from a file
        self.assertEqual(len(df), 5)  # Check if the number of rows is correct
        self.assertListEqual(
            list(df.columns), ["city", "state", "zip"]
        )  # Check if column names are correct

    def test_generate_descriptive_stats(self):
        """Test the generate_descriptive_stats function."""
        stats_numeric, stats_categorical = generate_descriptive_stats(self.df)

        # Check if categorical data statistics are correctly generated
        self.assertIn("city", stats_categorical.columns)  # 'city' column should exist
        self.assertIn("state", stats_categorical.columns)  # 'state' column should exist

    def test_generate_visualizations(self):
        """Test the generate_visualizations function."""
        # Check if visualizations are generated without errors (no need to check actual plots)
        try:
            generate_visualizations(self.df)
        except Exception as e:
            self.fail(f"generate_visualizations raised an exception: {e}")


class TestGenerateMarkdownReport(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("pandas.read_csv")
    def test_generate_markdown_report(self, mock_read_csv, mock_file):
        """Test generate_markdown_report function"""

        # Mocking pandas DataFrame for descriptive statistics
        mock_numeric_df = pd.DataFrame(
            {"mean": [10, 20], "std": [1, 2], "min": [1, 10], "max": [100, 200]},
            index=["Column1", "Column2"],
        )

        mock_categorical_df = pd.DataFrame(
            {"unique": [5, 10], "top": ["A", "B"], "freq": [100, 200]},
            index=["Column1", "Column2"],
        )

        # Mock the return values of pd.read_csv
        mock_read_csv.side_effect = [mock_numeric_df, mock_categorical_df]

        # Call the function
        generate_markdown_report()

        # Ensure that the file was opened
        mock_file.assert_called_once_with("report.md", "w")

        # Get the file handle from the mock
        handle = mock_file()

        # Check the content written to the file
        written_content = "".join(
            call.args[0] for call in handle.write.mock_calls if call.args
        )

        # Ensure specific sections were written correctly
        self.assertIn("# Polling Places Analysis Report\n\n", written_content)
        self.assertIn("## Descriptive Statistics\n\n", written_content)
        self.assertIn("### Numeric Columns\n\n", written_content)
        self.assertIn("### Categorical Columns\n\n", written_content)
        self.assertIn(
            "![Top 20 Polling Places by City](top20_city_polling_places.png)",
            written_content,
        )
        self.assertIn(
            "![Polling Places by State](polling_places_by_state.png)", written_content
        )
        self.assertIn(
            "![Top 20 Polling Places by ZIP Code](top20_zip_polling_places.png)",
            written_content,
        )
        self.assertIn("## Conclusion\n\n", written_content)


if __name__ == "__main__":
    unittest.main()
