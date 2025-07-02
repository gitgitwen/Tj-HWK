import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from mpl_toolkits.mplot3d import Axes3D

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 加载数据
file_path = 'Drivers_risk_avoidance_behavior.xlsx'  # 请确保文件路径正确
data = pd.read_excel(file_path)

# 提取特征数据
X = data[['range_x', 'long_accel', 'reaction_time']].values

# 2. 计算层次聚类（使用中心链接法）
Z = sch.linkage(X, method='centroid')  # 使用中心链接法

# 3. 绘制树状图（Dendrogram）
plt.figure(figsize=(12, 8))
sch.dendrogram(Z)
plt.xlabel("驾驶员编号", fontsize=15)
plt.ylabel("距离", fontsize=15)
plt.xticks(fontsize=13.5)
plt.yticks(fontsize=13.5)
plt.show()

# 4. 计算并绘制簇数与轮廓系数的关系图
silhouette_scores = []  # 存储每个簇数对应的轮廓系数
k_range = range(2, 15)  # 假设聚类数目范围从2到15

for k in k_range:
    # 使用AgglomerativeClustering进行聚类
    model = AgglomerativeClustering(n_clusters=k, linkage='ward')
    model.fit(X)
    
    # 计算轮廓系数
    labels = model.labels_
    score = silhouette_score(X, labels)
    silhouette_scores.append(score)

# 绘制簇类数目与轮廓系数折线图
plt.figure(figsize=(12, 8))
plt.plot(k_range, silhouette_scores, marker='o', color='b')
plt.xlabel("簇类数目", fontsize=15)
plt.ylabel("轮廓系数", fontsize=15)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid(True)
plt.show()

# 5. 使用5簇进行聚类
optimal_k = 4
model = AgglomerativeClustering(n_clusters=optimal_k, linkage='ward')
model.fit(X)
labels = model.labels_

# 绘制3D散点图
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维散点图
scatter = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, cmap='viridis', s=50)

# 显示图例
legend1 = ax.legend(*scatter.legend_elements(), title="聚类编号")
ax.add_artist(legend1)

plt.show()
