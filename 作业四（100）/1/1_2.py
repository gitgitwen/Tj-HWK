import pandas as pd
import matplotlib.pyplot as plt

# 读取 Excel 文件
file_path = 'jd.xlsx'  # 替换为实际文件路径
data = pd.read_excel(file_path)

# 将时间列转换为 datetime 类型
data['stime'] = pd.to_datetime(data['stime'])
data['etime'] = pd.to_datetime(data['etime'])

# 计算订单持续时长（分钟）
data['duration_min'] = (data['etime'] - data['stime']).dt.total_seconds() / 60

# 绘制持续时长的直方图（优化版）
plt.figure(figsize=(14, 8), dpi=400)
plt.hist(
    data['duration_min'], 
    bins=50,  # 优化分箱数量，根据数据分布调整
    edgecolor='black', 
    alpha=0.85, 
    color="#ffd500",  # 更柔和的蓝色
    linewidth=1.2  # 边框更清晰
)

# 添加平均值和中位数标注线
mean_duration = data['duration_min'].mean()
median_duration = data['duration_min'].median()

plt.axvline(mean_duration, color='red', linestyle='--', linewidth=1.5, label=f'平均值: {mean_duration:.2f} 分钟')
plt.axvline(median_duration, color='green', linestyle='--', linewidth=1.5, label=f'中位数: {median_duration:.2f} 分钟')

# 设置标题和坐标轴

plt.xlabel('持续时长（分钟）', fontsize=16)
plt.ylabel('频数', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# 设置网格线和图例
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(fontsize=14, loc='upper right', frameon=True, shadow=True)

# 自动调整布局
plt.tight_layout()

# 显示图表
plt.show()

# 查看订单持续时长的统计描述
print(data['duration_min'].describe())
