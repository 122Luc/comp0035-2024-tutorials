import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.dates as mdates  


def plot_time_series(df, x_column, y_column):

    fig, ax = plt.subplots()
    
    # Plot the data
    df.plot(x=x_column, y=y_column, ax=ax)
    
    # Set x-axis label format and ticks
    ax.xaxis.set_major_locator(mdates.YearLocator(4))  # 每隔4年显示一个刻度
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 日期格式为 年-月-日
    plt.xticks(rotation=45)  # 旋转x轴刻度标签
    
    # Set plot labels and title
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} over time")
    
    # Show the plot
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Read the data from the files into a Pandas dataframe. Version includes error handling for the file read
    try:
        paralympics_prepared_excel = Path(__file__).parent.parent.parent.joinpath("src","tutorialpkg","data", "paralympics_events_prepared.xlsx")
        df = pd.read_excel(paralympics_prepared_excel)
        df['start'] = pd.to_datetime(df['start'])  # 确保 'start' 列是日期格式

    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")
    
    df = df.sort_values(by='start')

    # Plot time series for participants over time
    print("Plotting time series for participants...")
    plot_time_series(df, x_column='start', y_column='participants')


