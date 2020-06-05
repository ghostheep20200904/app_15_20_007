import yaml

# [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")]

# 存储测试数据
data_list = []
# 打开文件
with open("./search.yml", "r") as f:
    # 解析数据
    data = yaml.safe_load(f)

    # print(data.values())
    # 结果 [{'input': '1', 'exp': '休眠'}, {'input': 'i', 'exp': 'IP地址'}, {'input': 'm', 'exp': 'MAC地址'}]

    for i in data.values():
        data_list.append((i.get("input"), i.get("exp")))

print(data_list)
"""
data={
    'test_001': {'input': '1', 'exp': '休眠'}, 
    'test_002': {'input': 'i', 'exp': 'IP地址'}, 
    'test_003': {'input': 'm', 'exp': 'MAC地址'}
    }


"""
