import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_histograms(df, columns=None):
    """
    Plots histograms for the specified columns of the dataframe.
    If no columns are specified, it will plot histograms for all numeric columns.
    """
    if columns:
        df[columns].hist()
    else:
        df.hist()  # Plot all numeric columns if no specific columns are provided
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Read the data from the files into a Pandas dataframe. Version includes error handling for the file read
    try:
        paralympics_prepared_excel = Path(__file__).parent.parent.parent.joinpath("src","tutorialpkg","data", "paralympics_events_prepared.xlsx")
        df = pd.read_excel(paralympics_prepared_excel)

    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

            # Filter data for summer events
    summer_df = df[df['type'] == 'summer']
    print("Summer data filtered successfully.")
    
    # Filter data for winter events
    winter_df = df[df['type'] == 'winter']
    print("Winter data filtered successfully.")
    
    # Plot histograms for summer events
    plot_histograms(summer_df)
    
    # Plot histograms for winter events
    plot_histograms(winter_df)
