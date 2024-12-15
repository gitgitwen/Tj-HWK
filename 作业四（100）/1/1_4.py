import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# 加载数据
file_path = 'jd.xlsx'
data = pd.read_excel(file_path)

# 更新字体设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
rcParams['axes.unicode_minus'] = False  # 确保负号正常显示

# 统计每辆出租车的订单数量
order_counts = data['carID'].value_counts()

# 统计订单数频率
bins = range(1, order_counts.max() + 2)
hist, bin_edges = np.histogram(order_counts, bins=bins)

# 设置颜色渐变（根据频数分配颜色）
cmap = plt.cm.Greens  # 选择渐变色
norm = plt.Normalize(vmin=min(hist), vmax=max(hist))  # 归一化
colors = [cmap(norm(value)) for value in hist]  # 根据频数分配颜色

# 手动绘制柱状图
plt.figure(figsize=(14, 10), dpi=400)
for i in range(len(hist)):
    plt.bar(
        bin_edges[i], hist[i], color=colors[i], edgecolor='black', width=0.8, alpha=0.9
    )

# 添加柱形顶部数值标注
for i in range(len(hist)):
    if hist[i] > 0:  # 仅标注非零频数
        plt.text(
            bin_edges[i] + 0.4,  # x 坐标
            hist[i] + 5,         # y 坐标（避免重叠）
            str(hist[i]),
            ha='center',
            fontsize=10,
            color='black'
        )

# 添加标题和轴标签
plt.xlabel('订单数量', fontsize=16, labelpad=15)
plt.ylabel('频数', fontsize=16, labelpad=15)


# 调整x轴刻度
plt.xticks(range(1, order_counts.max() + 1, max(1, order_counts.max() // 10)), fontsize=14)
plt.yticks(fontsize=14)

# 设置背景为白色
plt.gca().set_facecolor('white')  # 设置背景为白色
plt.grid(axis='y', linestyle='--', alpha=0.6)  # 仅显示y轴网格线

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
