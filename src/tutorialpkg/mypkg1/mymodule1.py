# mypkg1/mymodule1.py
# from pathlib import Path
# import sys

# # 获取当前文件的路径并解析到绝对路径
# current_file = Path(__file__).resolve()

# # 获取'tutorialpkg'的路径（即项目结构中的tutorialpkg目录）
# tutorialpkg_dir = current_file.parents[1]

# # 将'tutorialpkg'路径添加到sys.path中
# sys.path.append(str(tutorialpkg_dir))

# 从'mypkg2.mymodule2_1'中导入'calculate_area_of_circle'
from tutorialpkg.mypkg2.mymodule2_1 import calculate_area_of_circle
from tutorialpkg.mypkg2.mymodule2_2 import fetch_user_data


mock_database = {
    1: {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    42: {'name': 'Bob', 'email': 'bob@example.com', 'age': 45},
}

if __name__ == '__main__':
    # The functions are in the modules in mypkg2. You will need to import them.

    # Calculate the area of a circle with a radius of 10. Print the result.
    area = calculate_area_of_circle(10)
    print(f"The area is {area}.")

    # Use the fetch_user_data(user_id, database) function to print the data for the user with ID 42 that is in `mock_database` variable.
    print(fetch_user_data(42, mock_database))

    # Locate the data file `paralmpics_raw.csv` relative to this file using pathlib.Path. Prove it exists.
