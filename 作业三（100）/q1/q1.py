import pandas as pd
data = pd.read_excel("HWK3_data.xlsx",sheet_name='线圈数据',index_col='列1')
df = pd.DataFrame(data) #导入数据
df_duplicated = df[df.duplicated('FDT_TIME',keep=False)] #查找时间重复的数据
print('冗余数据:',df_duplicated)
df = df.drop_duplicates('FDT_TIME') #两个冗余数据相同，平均处理就相当于删除一个
df = df.reset_index(drop=True) #对数据重新编号
print(df)
df.to_excel('HWK3_data(1).xlsx') #保存到新文件
 
