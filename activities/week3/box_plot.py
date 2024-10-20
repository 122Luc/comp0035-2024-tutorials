import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_box(df):
    df.boxplot()
    # df.plot.box()  # This syntax is also valid
    plt.show()

if __name__ == "__main__":
    # Read the data from the files into a Pandas dataframe. Version includes error handling for the file read
    try:
        paralympics_prepared_excel = Path(__file__).parent.parent.parent.joinpath("src","tutorialpkg","data", "paralympics_events_prepared.xlsx")
        df = pd.read_excel(paralympics_prepared_excel)

    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")
    plot_box(df)


