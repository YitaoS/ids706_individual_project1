import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_save_visualization(
    df, column_name, save_filename=None, show=False, plot_type="hist", top_n=None
):
    """
    A general visualization function that creates and saves a plot.
    """
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 6))

    if plot_type == "hist":
        sns.histplot(df[column_name], kde=True, color="skyblue", bins=30)
    elif plot_type == "bar":
        if top_n:
            data = df[column_name].value_counts().head(top_n)
        else:
            data = df[column_name].value_counts()
        sns.barplot(
            x=data.index, y=data.values, palette="Blues_d", hue=data.index, legend=False
        )

        plt.xticks(rotation=45, ha="right")

    plt.title(f"{column_name} Distribution", fontsize=16)
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel("Frequency", fontsize=12)

    plt.show()
    if save_filename:
        plt.savefig(save_filename, bbox_inches="tight")
        plt.close()

    if show:
        plt.show()


def read_dataset(file_path):
    """Reads the CSV file into a Pandas DataFrame, skipping bad lines."""
    df = pd.read_csv(file_path, sep="\t", encoding="utf-16", on_bad_lines="skip")
    df.columns = df.columns.str.strip()
    return df
