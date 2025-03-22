import pandas as pd

# 读取原始Excel文件
test_name = 'data2.xlsx'
data = pd.read_excel(test_name)

# 保留前10000行数据
if data.shape[0] > 10000:
    data = data.iloc[50000:60000]

# 将截取的前10000行数据写回原始Excel文件，覆盖原文件
data.to_excel(test_name, index=False)

print(f"保留了前10000行数据并覆盖了文件：{test_name}")