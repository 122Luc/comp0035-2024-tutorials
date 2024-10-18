from pathlib import Path
import pandas as pd


def prepare_data(df):
    # 定义要转换为整数的列
    columns_to_change = ['countries', 'events', 'participants_m', 'participants_f', 'participants', 'Rank']

    # 对这些列进行转换，填充 NaN 值为 0，然后转换为 int 类型
    for col in columns_to_change:
        if col in df.columns:  # 检查列是否存在
            print(f"Converting column: {col}")  # 调试输出
            print(df[col].head())  # 查看前5行数据
            try:
                df[col] = df[col].fillna(0).astype('int')  # 转换为整数类型
            except ValueError as e:
                print(f"Error converting column '{col}' to int: {e}")
        else:
            print(f"Column '{col}' not found in the DataFrame, skipping conversion.")  # 如果列不存在，跳过

    # 将 'start' 和 'end' 列转换为 datetime 类型
    if 'start' in df.columns:
        df['start'] = pd.to_datetime(df['start'], format='%d/%m/%Y', errors='coerce')
    if 'end' in df.columns:
        df['end'] = pd.to_datetime(df['end'], format='%d/%m/%Y', errors='coerce')

    # 计算 'duration' 列，并插入到 'end' 列之后
    if 'start' in df.columns and 'end' in df.columns:
        df.insert(df.columns.get_loc('end') + 1, 'duration', (df['end'] - df['start']).dt.days.astype(int))


    # 处理 'type' 列中的数据
    if 'type' in df.columns:
        print("Unique values in 'type' column before processing:")
        print(df['type'].unique())  # 打印 'type' 列中的唯一值
        
        df['type'] = df['type'].str.strip()  # 去除前后的空格
        df['type'] = df['type'].str.lower()  # 转换为小写
        
        print("Unique values in 'type' column after processing:")
        print(df['type'].unique())  # 再次打印唯一值，检查是否一致

    # 删除不需要的列，确保列存在才删除
    cols_to_drop = ['URL', 'disabilities_included', 'highlights', 'name']
    cols_to_drop = [col for col in cols_to_drop if col in df.columns]
    df_prepared = df.drop(columns=cols_to_drop)

    # 删除特定的行
    df_prepared = df_prepared.drop(index=[0, 17, 31], errors='ignore')
    df_prepared = df_prepared.reset_index(drop=True)
    
    replacement_names = {
    'UK': 'Great Britain',
    'USA': 'United States of America',
    'Korea': 'Republic of Korea',
    'Russia': 'Russian Federation',
    'China': "People's Republic of China"
    }
    # 替换国家名称
    df_prepared['country'] = df_prepared['country'].replace(replacement_names)
    print(replacement_names)

    # 保存准备好的 DataFrame 到 CSV 文件
    output_path = Path(__file__).parent.joinpath("data", "paralympics_events_prepared_2.csv")
    df_prepared.to_csv(output_path, index=False)
    print(f"\nSaved prepared DataFrame to '{output_path}'.")

    return df_prepared
    # 定义替换字典，同样使用大写的键
 



# 假设这里有一个 prepare_data 函数的定义

# 定义描述 DataFrame 的函数
def describe_dataframe(df):
    # 打印 DataFrame 的形状
    print(f"DataFrame shape: {df.shape}")

    # 打印前5行和后5行
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nLast 5 rows:")
    print(df.tail())

    # 打印列标签
    print("\nColumn labels:")
    print(df.columns)

    # 打印列的数据类型
    print("\nColumn data types:")
    print(df.dtypes)

    # 打印 DataFrame 的概述信息
    print("\nDataFrame info:")
    print(df.info())

    # 打印描述性统计
    print("\nStatistical summary:")
    print(df.describe())


# 主函数，负责读取 CSV 和 Excel 文件，并调用 describe_dataframe 函数
def main():
    # 读取 CSV 文件
    try:
        paralympics_datafile_csv = Path(__file__).parent.joinpath(
            "data", "paralympics_events_raw.csv"
        )
        events_csv_df = pd.read_csv(paralympics_datafile_csv)

        # 先打印 'start' 和 'end' 列的值 (处理前)
        print("\nStart and End Dates (Before Processing):")
        print(events_csv_df[['start', 'end']].head())

        # 打印 'start' 和 'end' 列的缺失值情况
        print("\nMissing values in 'start' column:")
        print(events_csv_df['start'].isnull().sum())

        print("Missing values in 'end' column:")
        print(events_csv_df['end'].isnull().sum())

        # 处理数据
        events_csv_df = prepare_data(events_csv_df)

        # 打印处理后的 DataFrame
        print("\nCSV Data after preparation:")
        describe_dataframe(events_csv_df)
    except FileNotFoundError as e:
        print(f"CSV file not found. Please check the file path. Error: {e}")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")

    # 读取 Excel 文件的第一个工作表
    try:
        excel_file = Path(__file__).parent.joinpath(
            "data", "paralympics_all_raw.xlsx"
        )
        df_excel = pd.read_excel(excel_file, sheet_name=0)

        # 先打印 'start' 和 'end' 列的值 (处理前)
        print("\nStart and End Dates (Before Processing - First Sheet):")
        print(df_excel[['start', 'end']].head())

        # 打印 'start' 和 'end' 列的缺失值情况
        print("\nMissing values in 'start' column (First Sheet):")
        print(df_excel['start'].isnull().sum())

        print("Missing values in 'end' column (First Sheet):")
        print(df_excel['end'].isnull().sum())

        # 处理数据
        df_excel = prepare_data(df_excel)

        # 打印处理后的 DataFrame
        print("\nExcel file content (first sheet) after preparation:")
        describe_dataframe(df_excel)
    except FileNotFoundError as e:
        print(f"Excel file (first sheet) not found. Please check the file path. Error: {e}")
    except Exception as e:
        print(f"An error occurred while reading the first sheet of the Excel file: {e}")

    # 读取 Excel 文件的第二个工作表
    try:
        df_excel_medals = pd.read_excel(excel_file, sheet_name=1)

        # 先检查 'start' 和 'end' 列是否存在
        if 'start' in df_excel_medals.columns and 'end' in df_excel_medals.columns:
            # 打印 'start' 和 'end' 列的值 (处理前)
            print("\nStart and End Dates (Before Processing - Second Sheet):")
            print(df_excel_medals[['start', 'end']].head())

            # 打印 'start' 和 'end' 列的缺失值情况
            print("\nMissing values in 'start' column (Second Sheet):")
            print(df_excel_medals['start'].isnull().sum())

            print("Missing values in 'end' column (Second Sheet):")
            print(df_excel_medals['end'].isnull().sum())
        else:
            print("\nThe 'start' and 'end' columns are not present in the second sheet.")

        # 处理数据
        df_excel_medals = prepare_data(df_excel_medals)

        # 打印处理后的 DataFrame
        print("\nExcel file content (second sheet) after preparation:")
        describe_dataframe(df_excel_medals)
    except FileNotFoundError as e:
        print(f"Excel file (second sheet) not found. Please check the file path. Error: {e}")
    except Exception as e:
        print(f"An error occurred while reading the second sheet of the Excel file: {e}")
    
      # 读取并合并 npc_codes.csv 文件
    # 读取并合并 npc_codes.csv 文件
    try:
        npc_codes_file = Path(__file__).parent.joinpath("data", "npc_codes.csv")
        npc_codes_df = pd.read_csv(npc_codes_file,encoding='utf-8', encoding_errors='ignore',)

        # 确保 npc_codes.csv 中的列名为 'Name' 和 'Code'
        print("\nNPC Codes Data:")
        print(npc_codes_df.head())

        # 将 'events_csv_df' 与 'npc_codes_df' 合并，基于 'country' 和 'Name' 列
        merged_df = events_csv_df.merge(npc_codes_df[['Name', 'Code']], how='left', left_on='country', right_on='Name')

        # 打印合并后的 DataFrame
        print("\nMerged DataFrame with NPC Codes:")
        print(merged_df[['country', 'Code', 'Name']])

    except FileNotFoundError as e:
        print(f"NPC codes CSV file not found. Please check the file path. Error: {e}")
    except Exception as e:
        print(f"An error occurred while reading the NPC codes CSV file: {e}")



# 调用主函数
if __name__ == "__main__":
    main()
