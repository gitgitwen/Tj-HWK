import pandas as pd

# 读取 Excel 文件
# 请将 'data.xlsx' 替换为您的 Excel 文件路径
excel_file = 'demoData.xlsx'
df = pd.read_excel(excel_file)

# 显示前几行数据以确认读取正确（可选）
print("数据预览：")
print(df.head())

# 定义条件 1:
# 如果速度为0，则流量必为0，占有率必须为0或100
cond1 = (df['FINT_SPEED'] == 0) & ((df['FINT_VOLUME'] != 0) | (~df['FINT_OCCUPY'].isin([0, 100])))

# 定义条件 2:
# 如果占有率为0，则流量和速度必为0
cond2 = (df['FINT_OCCUPY'] == 0) & ((df['FINT_VOLUME'] != 0) | (df['FINT_SPEED'] != 0))

# 定义条件 3:
# 如果占有率为100，则流量和速度必为0
cond3 = (df['FINT_OCCUPY'] == 100) & ((df['FINT_VOLUME'] != 0) | (df['FINT_SPEED'] != 0))

# 定义条件 4:
# 如果流量等于0，则速度必为0，占有率必须为0或100
cond4 = (df['FINT_VOLUME'] == 0) & ((df['FINT_SPEED'] != 0) | (~df['FINT_OCCUPY'].isin([0, 100])))

# 合并所有不符合条件的行
invalid_rows = df[cond1 | cond2 | cond3 | cond4]

# 统计不符合条件的数据行数
num_invalid = invalid_rows.shape[0]

print(f"\n不符合条件的数据行数: {num_invalid}")
print("\n不符合条件的具体数据：")
print(invalid_rows)


