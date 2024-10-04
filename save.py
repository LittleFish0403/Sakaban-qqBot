import os
import json
import random
from datetime import datetime
from typing import Optional, Dict

# 示例默认内容
DEFAULT_JSON_CONTENT = '{"date": "", "member": ""}'

# 定义文件名
FILENAME = "xnn_data.json"

# 读取文件内容
def load_last_executed_info(filename: str) -> Optional[Dict]:
    with open(f"members_info/{filename}", "r") as file:
        try:
            info = json.load(file)
            if isinstance(info, dict):
                return info
            else:
                return json.loads(DEFAULT_JSON_CONTENT)
        except json.JSONDecodeError:
            return json.loads(DEFAULT_JSON_CONTENT)
        except FileNotFoundError:
            return json.loads(DEFAULT_JSON_CONTENT)

# 保存信息到文件
def save_last_executed_info(date: datetime.date, member: str, filename: str):
    info = {
        'date': date.strftime("%Y-%m-%d"),
        'member': member,
    }
    with open(f"members_info/{filename}", "w") as file:
        json.dump(info, file, ensure_ascii=False, indent=4)