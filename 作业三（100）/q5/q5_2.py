import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取平滑后的数据
input_file = 'exponential_smoothing.xlsx'  # 输入文件名
df = pd.read_excel(input_file)

# 确保数据按照时间排序
df = df.sort_values('FDT_TIME')

# 将 FDT_TIME 转换为 datetime 格式，并只保留小时和分钟
# 假设时间格式为 'H:MM:SS'，例如 '6:30:00'
df['FDT_TIME'] = pd.to_datetime(df['FDT_TIME'], format='%H:%M:%S')

# 创建一个新的列，仅包含小时和分钟
df['FDT_HM'] = df['FDT_TIME'].dt.strftime('%H:%M')

# 创建图形和轴
plt.figure(figsize=(14, 7))

# 绘制原始速度数据
plt.plot(df['FDT_TIME'], df['FINT_SPEED'], label='FINT_SPEED', color='#36A2EB', linewidth=1.2)

# 绘制移动平均数据
plt.plot(df['FDT_TIME'], df['alpha=0.1'], label='alpha=0.1', color='#FF6347', linewidth=1)
plt.plot(df['FDT_TIME'], df['alpha=0.2'], label='alpha=0.2', color='#66CDAA', linewidth=1)
plt.plot(df['FDT_TIME'], df['alpha=0.5'], label='alpha=0.5', color='#FFD700', linewidth=1)

# 设置标题和标签
plt.xlabel('time')
plt.ylabel('speed')

# 设置日期格式化
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# 设置主刻度定位器为每30分钟一个刻度
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=30))

# 显示图例
plt.legend()

# 优化时间显示，旋转刻度标签以防止重叠
plt.xticks(rotation=0)

# 调整布局以防止标签被遮挡
plt.tight_layout()

# 保存图表为 PNG 图片
output_image = 'speed_time_series_hm1.png'
plt.savefig(output_image, dpi=600)
plt.close()

print(f"时序图已保存为 '{output_image}'。")
