import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# 设置全局字体为中文（假设系统已安装相应中文字体，例如 SimHei 或 Microsoft YaHei）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 防止负号显示异常

# 假设已经读取了数据并进行了时间处理
data = pd.read_excel(r"jd.xlsx")
data['stime'] = pd.to_datetime(data['stime'])
data['etime'] = pd.to_datetime(data['etime'])

# 提取每小时的时间区间
data['start_hour'] = data['stime'].dt.floor('H')
data['end_hour'] = data['etime'].dt.floor('H')

# 统计每小时的订单数量（开始时间和结束时间分别计数）
start_counts = data.groupby('start_hour').size()
end_counts = data.groupby('end_hour').size()

# 合并两种统计，填充空值为0
time_range = pd.date_range(start=start_counts.index.min(), end=end_counts.index.max(), freq='H')
start_counts = start_counts.reindex(time_range, fill_value=0)
end_counts = end_counts.reindex(time_range, fill_value=0)

# 美化图形绘制
plt.figure(figsize=(14, 8), dpi=400)
plt.plot(
    start_counts.index, start_counts.values, label='开始订单数', 
    marker='o', linestyle='-', linewidth=2, markersize=8, color='blue'
)
plt.plot(
    end_counts.index, end_counts.values, label='结束订单数', 
    marker='s', linestyle='--', linewidth=2, markersize=8, color='orange'
)

# 设置时间格式和美化
time_format = DateFormatter('%H:%M')  # 显示小时:分钟
plt.gca().xaxis.set_major_formatter(time_format)  # 应用时间格式
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# 添加标题和坐标轴标签
plt.xlabel('时间', fontsize=18)
plt.ylabel('订单数量', fontsize=18)

# 设置网格线
plt.grid(alpha=0.3, linestyle='--')

# 添加图例并调整位置
plt.legend(fontsize=14, loc='upper left', frameon=True, shadow=True, facecolor='white', edgecolor='gray')

# 自动布局调整
plt.tight_layout()

# 显示图形
plt.show()
