import pandas as pd
import matplotlib.pyplot as plt
from mylib.lib import read_dataset


def generate_descriptive_stats(df):
    """Generates descriptive statistics for numeric and categorical columns."""
    stats_numeric = df.describe()  # Statistics for numeric data
    stats_categorical = df.describe(
        include=["object"]
    )  # Statistics for categorical data
    return stats_numeric, stats_categorical


def generate_visualizations(df):
    """Creates multiple visualizations for the report."""

    # Visualization 1: Display the number of polling places in the top 20 cities
    if "city" in df.columns:
        city_counts = df["city"].dropna().value_counts().head(20)
        plt.figure(figsize=(12, 6))
        city_counts.plot(kind="bar")
        plt.title("Top 20 Cities by Number of Polling Places")
        plt.xlabel("City")
        plt.ylabel("Number of Polling Places")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("top20_city_polling_places.png")
        plt.close()

    # Visualization 2: Distribution of polling places by state
    if "state" in df.columns:
        state_counts = df["state"].dropna().value_counts()
        plt.figure(figsize=(12, 6))
        state_counts.plot(kind="bar", color="green")
        plt.title("Number of Polling Places by State")
        plt.xlabel("State")
        plt.ylabel("Number of Polling Places")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("polling_places_by_state.png")
        plt.close()

    # Visualization 3: Distribution of polling places by ZIP code area
    if "zip" in df.columns:
        zip_counts = df["zip"].dropna().value_counts().head(20)
        plt.figure(figsize=(12, 6))
        zip_counts.plot(kind="bar", color="purple")
        plt.title("Top 20 ZIP Codes by Number of Polling Places")
        plt.xlabel("ZIP Code")
        plt.ylabel("Number of Polling Places")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("top20_zip_polling_places.png")
        plt.close()


def generate_markdown_report():
    """Generates a markdown report with descriptive statistics and multiple visualizations."""
    # Read descriptive statistics data
    stats_numeric = pd.read_csv("descriptive_statistics_numeric.csv", index_col=0)
    stats_categorical = pd.read_csv(
        "descriptive_statistics_categorical.csv", index_col=0
    )

    # Start writing the Markdown report
    with open("report.md", "w") as f:
        f.write("# Polling Places Analysis Report\n\n")

        # Add descriptive statistics
        f.write("## Descriptive Statistics\n\n")
        f.write("### Numeric Columns\n\n")
        f.write(stats_numeric.to_markdown())
        f.write("\n\n### Categorical Columns\n\n")
        f.write(stats_categorical.to_markdown())

        # Add explanatory text
        f.write(
            "\n\nThis section provides the summary statistics for both numeric and categorical columns in the dataset. The numeric columns provide insights into the distribution of the data, while the categorical columns reveal the distinct values for non-numeric data, such as city and state.\n\n"
        )

        # Add visualization results
        f.write("## Visualizations\n\n")
        f.write("### Top 20 Cities by Number of Polling Places\n\n")
        f.write("![Top 20 Polling Places by City](top20_city_polling_places.png)\n\n")

        f.write("### Polling Places by State\n\n")
        f.write("![Polling Places by State](polling_places_by_state.png)\n\n")

        f.write("### Top 20 ZIP Codes by Number of Polling Places\n\n")
        f.write(
            "![Top 20 Polling Places by ZIP Code](top20_zip_polling_places.png)\n\n"
        )

        # Add analysis conclusion
        f.write("## Conclusion\n\n")
        f.write(
            "From the data and visualizations, we can see that the majority of polling places are concentrated in a few major cities and states. The distribution by ZIP code also highlights areas with more significant polling place activity. Further analysis could include trends over time or comparisons with voter population data.\n"
        )


def main():
    # Step 1: Read the dataset
    df = read_dataset("polling_place_20240514.csv")

    # Step 2: Generate descriptive statistics
    stats_numeric, stats_categorical = generate_descriptive_stats(df)

    # Save statistics data to CSV files
    stats_numeric.to_csv("descriptive_statistics_numeric.csv", encoding="utf-8")
    stats_categorical.to_csv("descriptive_statistics_categorical.csv", encoding="utf-8")

    # Step 3: Generate multiple visualizations
    generate_visualizations(df)

    # Step 4: Generate Markdown report
    generate_markdown_report()


if __name__ == "__main__":
    main()
