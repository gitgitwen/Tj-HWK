import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体为中文（适配中文标注）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False  # 修复负号显示问题

# 读取上传的 Excel 文件
file_path = 'jd.xlsx'
data = pd.read_excel(file_path)

# 检查 dis 列是否存在
if 'dis' in data.columns:
    # 绘制距离分布的直方图
    plt.figure(figsize=(14, 8), dpi=400)
    plt.hist(
        data['dis'], 
        bins=50,  # 分箱数量
        edgecolor='black', 
        alpha=0.85, 
        color="#5DADE2",  # 柔和的蓝色
        linewidth=1.2  # 边框更清晰
    )

    # 计算平均值和中位数
    mean_distance = data['dis'].mean()
    median_distance = data['dis'].median()

    # 添加平均值和中位数标注线
    plt.axvline(mean_distance, color='red', linestyle='--', linewidth=1.5, label=f'平均值: {mean_distance:.2f} 公里')
    plt.axvline(median_distance, color='green', linestyle='--', linewidth=1.5, label=f'中位数: {median_distance:.2f} 公里')

    # 设置标题和坐标轴
    plt.xlabel('行驶距离（公里）', fontsize=16)
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

    # 返回统计描述
    distance_description = data['dis'].describe()
    import ace_tools as tools; tools.display_dataframe_to_user(name="行驶距离统计描述", dataframe=distance_description)
else:
    print("表中不包含 'dis' 列。")
