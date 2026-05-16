#!/bin/bash
# 竞品研究数据收集脚本

DATE=$(date +%Y-%m-%d)
OUTPUT_DIR="/workspace/projects/workspace/竞品研究"
mkdir -p "$OUTPUT_DIR"

# 搜索关键词（随机选择不同类目）
CATEGORIES=("女装" "男装" "美食" "美妆" "家居" "数码" "母婴" "户外" "宠物" "文具")

echo "开始收集今日竞品数据: $DATE"

# 使用Python脚本抓取数据
python3 << PYEOF
import urllib.request
import json
import random
from datetime import datetime, timedelta

output_file = "$OUTPUT_DIR/竞品数据_{$DATE}.json"

# 搜索关键词
keywords = ["女装 新品", "美食 爆款", "数码 新品", "家居 热门", "美妆 新品", "男装 热销", "母婴 好物", "户外 爆款", "宠物用品", "文具 新品"]

products = []

for kw in keywords:
    try:
        # 淘宝搜索API
        url = f"https://suggest.taobao.com/sug?q={kw}&code=utf-8"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if data and len(data) > 0 and len(data[0]) > 0:
                for item in data[0][:2]:  # 每个类目取2个
                    if isinstance(item, list) and len(item) >= 2:
                        products.append({
                            "keyword": kw,
                            "suggestion": item[0],
                            "sales_index": item[1] if len(item) > 1 else 0
                        })
    except Exception as e:
        print(f"Error fetching {kw}: {e}")
        continue

# 保存数据
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump({
        "date": "$DATE",
        "count": len(products),
        "products": products
    }, f, ensure_ascii=False, indent=2)

print(f"收集到 {len(products)} 个竞品数据")
PYEOF
