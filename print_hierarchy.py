from pymongo import MongoClient

def print_hierarchy(client, collection_name, target_id, level=0):
    # 查询指定ID的文档
    doc = client.your_database[collection_name].find_one({"_id": target_id})
    
    if doc is None:
        print(f"No document found with _id: {target_id}")
        return
    
    # 打印当前文档的_id
    print("  " * level + f"ID: {doc['_id']}, Childrens: {doc.get('childrens', [])}")
    
    # 如果有childrens字段，则递归打印子文档
    if 'childrens' in doc:
        for child in doc['childrens']:
            # 假设child是以字典形式直接列出子元素，如{'b': 1, 'c': 1}
            # 这里简化处理，直接打印child的内容，实际应用中可能需要根据child的结构调整
            print_hierarchy(client, collection_name, list(child.keys())[0], level+1)  # 假设child的key即为其ID

# 连接到MongoDB
client = MongoClient('mongodb://localhost:27017/')  # 使用你的MongoDB地址和端口
db_name = 'your_database_name'  # 替换为你的数据库名
collection_name = 'nested_collection'  # 替换为你的collection名
target_id = 'a'  # 指定要查询的ID

print_hierarchy(client, db_name, target_id)
