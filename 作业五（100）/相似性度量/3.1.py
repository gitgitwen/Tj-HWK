import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
plt.rcParams['font.sans-serif'] = ['SimHei']
# 1. 加载Excel文件
file_path = 'Drivers_risk_avoidance_behavior.xlsx'  # 请确保文件路径正确
data = pd.read_excel(file_path)

# 2. 提取需要的特征数据（range_x, long_accel, reaction_time）
features = data[['range_x', 'long_accel', 'reaction_time']].values

# 3. 计算欧氏距离矩阵
distance_matrix = squareform(pdist(features, metric='euclidean'))

# 4. 获取下半角矩阵（包括对角线）
lower_triangle_matrix = np.tril(distance_matrix)

# 5. 将下半角矩阵转换为DataFrame格式，便于查看和保存
lower_triangle_df = pd.DataFrame(lower_triangle_matrix, index=data['Driver ID'], columns=data['Driver ID'])

# 6. 绘制热力图（只显示左下半区域）
plt.figure(figsize=(10, 8),dpi=400)

# 使用 seaborn 画热力图
mask = np.triu(np.ones_like(lower_triangle_matrix, dtype=bool))  # 生成上三角区域的掩码
sns.heatmap(lower_triangle_df, cmap='Blues', annot=False, square=True, 
            cbar_kws={'label': 'L2范数', 'shrink': 0.8},  # 设置色柱标签
            mask=mask, vmin=0,
            linewidths=0.1,
            linecolor='white')  # 显示色柱范围为正数，vmin=0确保色柱最小值为0

# 添加标题和标签
plt.xlabel("驾驶员编号", fontsize=12)
plt.ylabel("驾驶员编号", fontsize=12)

# 显示热力图
plt.show()
