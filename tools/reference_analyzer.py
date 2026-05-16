#!/usr/bin/env python3
"""
佛手光详情页 - 参考案例分析和模板生成器

功能：
1. 分析参考案例的配色方案
2. 提取布局结构
3. 生成可编辑的PSD文件
4. 生成HTML/CSS模板
5. 生成SVG矢量模板
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path
import json

class ReferenceAnalyzer:
    """参考案例分析器"""

    def __init__(self, reference_image_path):
        self.reference_path = Path(reference_image_path)
        self.image = Image.open(reference_image_path)
        self.colors = []
        self.layout = {}

    def extract_color_palette(self, num_colors=5):
        """
        提取图片的主要配色方案
        """
        # 将图片缩小以加快处理速度
        small_img = self.image.resize((150, 150))

        # 转换为numpy数组
        img_array = np.array(small_img)

        # 重塑为像素列表
        pixels = img_array.reshape(-1, 3)

        # 计算颜色直方图，找出出现频率最高的颜色
        from collections import Counter
        pixel_counts = Counter([tuple(pixel) for pixel in pixels])

        # 提取最常用的颜色
        self.colors = [list(color) for color, count in pixel_counts.most_common(num_colors)]

        return self.colors

    def get_color_hex(self):
        """
        返回十六进制颜色值
        """
        return [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in self.colors]


class TemplateGenerator:
    """模板生成器"""

    def __init__(self, colors, width=750, height=3000):
        self.colors = colors
        self.width = width
        self.height = height

    def generate_psd_like_template(self, output_path):
        """
        生成类似PSD的可编辑图片（实际为PNG格式，但包含分层信息）
        注意：真正的PSD需要专门的库，这里生成带有标注的模板
        """
        # 创建画布
        canvas = Image.new('RGB', (self.width, self.height), self.colors[-1])

        draw = ImageDraw.Draw(canvas)

        # 添加标题区域
        header_height = 400
        draw.rectangle([0, 0, self.width, header_height], fill=self.colors[0])

        # 添加产品展示区域
        product_y = header_height
        product_height = 800
        draw.rectangle([0, product_y, self.width, product_y + product_height],
                      fill=tuple(self.colors[-1]))

        # 添加功能区
        feature_y = product_y + product_height
        feature_height = 600
        draw.rectangle([0, feature_y, self.width, feature_y + feature_height],
                      fill=self.colors[1])

        # 添加对比区
        comparison_y = feature_y + feature_height
        comparison_height = 400
        draw.rectangle([0, comparison_y, self.width, comparison_y + comparison_height],
                      fill=self.colors[2])

        # 添加案例区
        case_y = comparison_y + comparison_height
        case_height = 600
        draw.rectangle([0, case_y, self.width, case_y + case_height],
                      fill=self.colors[3])

        # 保存图片
        canvas.save(output_path)

        # 保存配色方案和布局信息
        info_path = output_path.parent / f"{output_path.stem}_info.json"
        info = {
            "colors": [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in self.colors],
            "layout": {
                "header": {"y": 0, "height": 400, "color": 0},
                "product": {"y": 400, "height": 800, "color": -1},
                "feature": {"y": 1200, "height": 600, "color": 1},
                "comparison": {"y": 1800, "height": 400, "color": 2},
                "case": {"y": 2200, "height": 600, "color": 3}
            }
        }

        with open(info_path, 'w', encoding='utf-8') as f:
            json.dump(info, f, indent=2, ensure_ascii=False)

        return output_path, info_path

    def generate_html_template(self, output_path):
        """
        生成HTML/CSS模板
        """
        css_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in self.colors]

        html_template = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>佛手光详情页模板</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
            max-width: 750px;
            margin: 0 auto;
            background: {css_colors[-1]};
        }}

        .header {{
            height: 400px;
            background: {css_colors[0]};
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
        }}

        .product {{
            height: 800px;
            background: {css_colors[-1]};
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}

        .feature {{
            height: 600px;
            background: {css_colors[1]};
            padding: 40px;
        }}

        .comparison {{
            height: 400px;
            background: {css_colors[2]};
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 20px;
        }}

        .case {{
            height: 600px;
            background: {css_colors[3]};
            padding: 40px;
        }}

        h1 {{
            font-size: 36px;
            margin-bottom: 20px;
        }}

        h2 {{
            font-size: 28px;
            margin-bottom: 15px;
        }}

        p {{
            font-size: 16px;
            line-height: 1.8;
            color: #333;
        }}

        .placeholder {{
            border: 2px dashed rgba(0,0,0,0.2);
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: rgba(0,0,0,0.4);
            font-size: 18px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>【这里是标题区域】</h1>
        <p>产品副标题/核心卖点</p>
    </div>

    <div class="product">
        <div class="placeholder" style="width: 100%; height: 100%;">
            【产品主图区域】
        </div>
    </div>

    <div class="feature">
        <h2>【功能特点区域】</h2>
        <p>这里是功能特点的详细介绍...</p>
    </div>

    <div class="comparison">
        <div class="placeholder" style="width: 45%; height: 80%;">
            【传统方式】
        </div>
        <div class="placeholder" style="width: 45%; height: 80%;">
            【佛手光】
        </div>
    </div>

    <div class="case">
        <h2>【客户案例区域】</h2>
        <p>这里展示真实的客户反馈和案例...</p>
    </div>
</body>
</html>
"""

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_template)

        return output_path


# 使用示例
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("使用方法: python3 reference_analyzer.py <参考图路径>")
        print("示例: python3 reference_analyzer.py reference.png")
        sys.exit(1)

    reference_path = sys.argv[1]

    # 1. 分析参考案例
    print("🔍 正在分析参考案例...")
    analyzer = ReferenceAnalyzer(reference_path)
    colors = analyzer.extract_color_palette(num_colors=5)
    hex_colors = analyzer.get_color_hex()

    print(f"\n✓ 提取到配色方案：")
    for i, color in enumerate(hex_colors):
        print(f"  颜色{i+1}: {color}")

    # 2. 生成模板
    print("\n🎨 正在生成模板...")
    generator = TemplateGenerator(colors)

    # 生成图片模板
    template_path = Path("foswift_template.png")
    info_path = generator.generate_psd_like_template(template_path)
    print(f"✓ 图片模板: {template_path}")
    print(f"✓ 模板信息: {info_path}")

    # 生成HTML模板
    html_path = Path("foswift_template.html")
    generator.generate_html_template(html_path)
    print(f"✓ HTML模板: {html_path}")

    print("\n✅ 模板生成完成！")
    print("\n💡 下一步：")
    print("1. 打开 foswift_template.png 查看布局")
    print("2. 用图片编辑器（Photoshop、GIMP等）编辑")
    print("3. 或打开 foswift_template.html 在浏览器中查看")
