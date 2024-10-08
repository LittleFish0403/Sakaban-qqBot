import os
import json
import random
from datetime import datetime
from typing import Optional
from pathlib import Path

# 默认内容
DEFAULT_JSON_CONTENT = '{"date": "", "member": ""}'

# 默认文件名
FILENAME = "xnn_data.json"

# 读取文件内容
def load_last_executed_info(filename: str) -> dict:
    # 定义文件路径
    filepath = os.path.join("members_info", filename)
    
    # 尝试打开文件
    try:
        with open(filepath, "r") as file:
            info = json.load(file)
            if isinstance(info, dict):
                return info
            else:
                return json.loads(DEFAULT_JSON_CONTENT)
    
    # 如果文件不存在，创建并写入默认内容
    except FileNotFoundError:
        # 创建父目录（如果不存在）
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
            print("父目录已创建。")
        # 创建文件并写入默认内容
        with open(filepath, "w") as file:
            file.write(DEFAULT_JSON_CONTENT)
            print("默认内容已写入文件。")
        
        # 读取默认内容并返回
        return json.loads(DEFAULT_JSON_CONTENT)
    
    # 如果文件存在但无法解析JSON格式
    except json.JSONDecodeError:
        return json.loads(DEFAULT_JSON_CONTENT)


# 保存信息到文件
def save_last_executed_info(date: datetime.date, member: str, filename: str):
    info = {
        'date': date.strftime("%Y-%m-%d"),
        'member': member,
    }
    with open(f"/members_info/{filename}", "w") as file:
        json.dump(info, file, ensure_ascii=False, indent=4)

def select_random_file(folder_path):
    try:
        # 获取指定文件夹下的所有文件
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # 检查文件夹是否为空
        if not files:
            print("该文件夹为空。")
            return None
        
        # 随机选择一个文件
        random_file = random.choice(files)
        return os.path.join(folder_path, random_file)
    
    except Exception as e:
        print(f"发生错误: {e}")
        return None