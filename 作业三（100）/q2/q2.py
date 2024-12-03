import pandas as pd
import warnings
warnings.filterwarnings("ignore")
data = pd.read_excel("HWK3_data(1).xlsx") 
df = pd.DataFrame(data)

## 查找缺失数据
# 确保 `FDT_TIME` 列转换为 datetime 类型
df['FDT_TIME'] = pd.to_datetime(df['FDT_TIME'])

# 计算相邻行的时间差（以秒为单位）
df['time_diff'] = df['FDT_TIME'].diff().dt.total_seconds()

# 查找不等于 20 秒的时间间隔，即缺失的数据段
missing_data = df[df['time_diff'] != 20]

# 输出缺失数据的时间段
if not missing_data.empty:
    print("缺失数据时间段：")
    for i, row in missing_data.iterrows():
        prev_time = df.loc[i - 1, 'FDT_TIME'] if i > 0 else None
        curr_time = row['FDT_TIME']
        print(f"缺失时间段从 {prev_time} 到 {curr_time}")
else:
    print("没有发现缺失的时间段。")
    
## 填充缺失值
# 创建预期的时间序列
start_time = df['FDT_TIME'].min()
end_time = df['FDT_TIME'].max()
expected_time_range = pd.date_range(start=start_time, end=end_time, freq='20S')

# 创建一个新的 DataFrame，包含预期的时间序列
expected_df = pd.DataFrame({'FDT_TIME': expected_time_range})

# 合并原始数据和预期时间序列
merged_df = pd.merge(expected_df, df, on='FDT_TIME', how='left')

# 缺失的 FINT_VOLUME, FINT_SPEED 和 FINT_OCCUPY 可以用 -1 填充
merged_df['FINT_VOLUME'].fillna(-1, inplace=True)
merged_df['FINT_SPEED'].fillna(-1, inplace=True)
merged_df['FINT_OCCUPY'].fillna(-1, inplace=True)
df = merged_df.drop(['time_diff','Unnamed: 0'],axis=1)
df['FSTR_LOOPGROUPID'].fillna('NHNX39(2)',inplace=True)

def update_sample_data(df, sample_index):
    # 检查索引是否有效
    if sample_index < 3 or sample_index >= len(df):
        raise ValueError("索引必须大于等于3并且小于数据的长度")
    
    # 计算前三个样本的平均值
    avg_volume = df['FINT_VOLUME'].iloc[sample_index-3:sample_index].mean()
    avg_speed = df['FINT_SPEED'].iloc[sample_index-3:sample_index].mean()
    avg_occupy = df['FINT_OCCUPY'].iloc[sample_index-3:sample_index].mean()
    
    # 更新指定样本的数据
    df.at[df.index[sample_index], 'FINT_VOLUME'] = avg_volume
    df.at[df.index[sample_index], 'FINT_SPEED'] = avg_speed
    df.at[df.index[sample_index], 'FINT_OCCUPY'] = avg_occupy

    return df

def update_samples_with_iterator(df):
    for i in range(len(df)):
        if df['FINT_VOLUME'].iloc[i] == -1 or df['FINT_SPEED'].iloc[i] == -1 or df['FINT_OCCUPY'].iloc[i] == -1:
            # 更新样本数据
            df = update_sample_data(df, i)
    return df

df_updated_with_iterator = update_samples_with_iterator(df) # 使用迭代器更新 DataFrame
df_updated_with_iterator = df_updated_with_iterator.round(0)
df_updated_with_iterator.to_excel('HWK3_data(2).xlsx') 