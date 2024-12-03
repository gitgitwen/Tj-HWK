import pandas as pd
import numpy as np
from math import sqrt

# 1. 导入数据
# 请将 'your_data.xlsx' 替换为您的Excel文件路径
df = pd.read_excel('q6_knn.xlsx')

# 2. 定义特征列
# 根据您的数据，特征列为除了“周期”和“目标检测器”之外的列
feature_cols = ['目标检测器前1天历史数据', '目标检测器前2天历史数据',
               '左侧检测器同日数据', '左侧检测器前1天历史数据', '左侧检测器前2天历史数据']

# 3. 分离有缺失和无缺失的行
missing_df = df[df['目标检测器'].isnull()].reset_index(drop=True)
non_missing_df = df.dropna(subset=['目标检测器']).reset_index(drop=True)

# 提取特征和目标变量
X_missing = missing_df[feature_cols].values
X_non_missing = non_missing_df[feature_cols].values
y_non_missing = non_missing_df['目标检测器'].values

# 4. 定义距离计算函数
def compute_distance(x, Y):
    """
    计算每个x与Y中所有样本的距离
    距离公式: sqrt((5/6) * Σ(x_i - y_i)^2)
    """
    # 计算 (Y - x) 的平方
    squared_diff = (Y - x) ** 2
    # 计算每行的和
    sum_squared_diff = np.sum(squared_diff, axis=1)
    # 乘以 (5/6) 并开方
    distances = np.sqrt((5/6) * sum_squared_diff)
    return distances

# 5. 定义KNN填补函数
def knn_impute(x, Y, y, k):
    """
    使用KNN算法填补缺失值
    x: 待填补的样本特征向量
    Y: 无缺失样本的特征矩阵
    y: 无缺失样本的目标变量
    k: 最近邻的数量
    """
    distances = compute_distance(x, Y)
    # 获取距离最小的k个样本的索引
    idx = np.argsort(distances)[:k]
    nearest_distances = distances[idx]
    nearest_values = y[idx]
    
    # 防止距离为0导致除以0错误
    nearest_distances = np.where(nearest_distances == 0, 1e-5, nearest_distances)
    
    # 计算权重（权重为1/距离）
    weights = 1 / nearest_distances
    # 计算加权平均
    weighted_average = np.sum(weights * nearest_values) / np.sum(weights)
    return weighted_average

# 6. 填补缺失值并创建两个不同的DataFrame

# 创建两个副本以分别填补k=1和k=3
df_k1 = df.copy()
df_k3 = df.copy()

# 填补k=1
imputed_k1 = []
for i in range(X_missing.shape[0]):
    imputed_value = knn_impute(X_missing[i], X_non_missing, y_non_missing, k=1)
    imputed_k1.append(imputed_value)

# 将填补后的值赋给原DataFrame的缺失位置
df_k1.loc[df_k1['目标检测器'].isnull(), '目标检测器'] = imputed_k1

# 填补k=3
imputed_k3 = []
for i in range(X_missing.shape[0]):
    imputed_value = knn_impute(X_missing[i], X_non_missing, y_non_missing, k=3)
    imputed_k3.append(imputed_value)

# 将填补后的值赋给另一个DataFrame的缺失位置
df_k3.loc[df_k3['目标检测器'].isnull(), '目标检测器'] = imputed_k3

# 7. 保存结果到不同的Excel文件
df_k1.to_excel('imputed_data_k1.xlsx', index=False)
df_k3.to_excel('imputed_data_k3.xlsx', index=False)

print("缺失值已使用KNN算法填补，并分别保存到 'imputed_data_k1.xlsx' 和 'imputed_data_k3.xlsx' 文件中。")
