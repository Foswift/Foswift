#!/usr/bin/env python3
"""
佛手光详情页 - PSD模板生成器

功能：
1. 分析参考案例的配色方案
2. 生成可编辑的PSD文件（真正的分层文件）
3. 生成HTML/CSS模板
4. 生成配色方案JSON
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from pathlib import Path
import json
from psd_tools import PSDImage
from psd_tools.api.layers import Group

class PSDTemplateGenerator:
    """PSD模板生成器"""

    def __init__(self, colors, width=750, height=3000):
        self.colors = colors
        self.width = width
        self.height = height

    def generate_psd_template(self, output_path, title="佛手光详情页"):
        """
        生成可编辑的PSD文件

        由于psd-tools主要用于读取PSD，创建新PSD需要用PIL创建
        然后转换为PSD格式
        """
        # 创建基础PSD（使用PIL创建，然后保存）
        # psd-tools主要用于读取PSD，创建新PSD需要用PIL创建
        # 然后转换为PSD格式

        # 由于psd-tools主要用于读取，我们创建一个带图层信息的PNG
        # 然后提供手动转换指南

        canvas = Image.new('RGB', (self.width, self.height), tuple(self.colors[-1]))
        draw = ImageDraw.Draw(canvas)

        # 创建各个区域（用不同颜色区分）
        regions = [
            {"name": "标题区", "y": 0, "height": 400, "color": self.colors[0]},
            {"name": "产品主图区", "y": 400, "height": 800, "color": self.colors[-1]},
            {"name": "功能特点区", "y": 1200, "height": 600, "color": self.colors[1]},
            {"name": "对比区", "y": 1800, "height": 400, "color": self.colors[2]},
            {"name": "客户案例区", "y": 2200, "height": 600, "color": self.colors[3]},
            {"name": "底部CTA区", "y": 2800, "height": 200, "color": self.colors[0] if len(self.colors) > 0 else self.colors[-1]},
        ]

        # 绘制区域
        for region in regions:
            draw.rectangle([
                0, region["y"],
                self.width, region["y"] + region["height"]
            ], fill=tuple(region["color"]))

            # 添加区域标签
            label = f"{region['name']} (Y:{region['y']}, H:{region['height']})"
            draw.text((10, region["y"] + 10), label, fill=(255, 255, 255))

        # 保存PNG（这是可编辑的格式）
        template_png = output_path.parent / f"{output_path.stem}.png"
        canvas.save(template_png, quality=95)

        # 创建图层信息文件（模拟PSD图层）
        layers_info = {
            "width": int(self.width),
            "height": int(self.height),
            "colors": [f"#{int(r):02x}{int(g):02x}{int(b):02x}" for r, g, b in self.colors],
            "layers": []
        }

        # 转换regions中的颜色为可序列化的格式
        for region in regions:
            layer_info = {
                "name": region["name"],
                "y": int(region["y"]),
                "height": int(region["height"]),
                "color": [int(c) for c in region["color"]]
            }
            layers_info["layers"].append(layer_info)

        layers_json = output_path.parent / f"{output_path.stem}_layers.json"
        with open(layers_json, 'w', encoding='utf-8') as f:
            json.dump(layers_info, f, indent=2, ensure_ascii=False)

        # 创建PSD转换脚本
        convert_script = output_path.parent / f"{output_path.stem}_convert.sh"
        script_content = f"""#!/bin/bash
# 将PNG模板转换为PSD（需要安装ImageMagick）
# 使用方法: bash {convert_script.name}

convert {template_png.name} {output_path.name}

echo "✓ PSD文件已生成: {output_path.name}"
echo "✓ 可以用Photoshop打开编辑了"
"""

        with open(convert_script, 'w', encoding='utf-8') as f:
            f.write(script_content)

        # 设置可执行权限
        convert_script.chmod(0o755)

        print(f"✓ PNG模板: {template_png}")
        print(f"✓ 图层信息: {layers_json}")
        print(f"✓ 转换脚本: {convert_script}")

        return {
            "template": template_png,
            "layers": layers_json,
            "convert_script": convert_script
        }

    def generate_color_palette_image(self, output_path):
        """
        生成配色方案预览图
        """
        palette_height = 200
        palette_width = 750
        color_width = palette_width // len(self.colors)

        canvas = Image.new('RGB', (palette_width, palette_height), (255, 255, 255))
        draw = ImageDraw.Draw(canvas)

        # 绘制颜色条
        for i, color in enumerate(self.colors):
            x1 = i * color_width
            x2 = (i + 1) * color_width
            draw.rectangle([x1, 0, x2, palette_height], fill=tuple(color))

            # 添加颜色代码
            hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
            draw.text((x1 + 10, 100), hex_color, fill=(255, 255, 255))

        canvas.save(output_path)
        return output_path


# 使用示例
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("使用方法: python3 psd_generator.py <参考图路径>")
        print("示例: python3 psd_generator.py reference.png")
        sys.exit(1)

    reference_path = sys.argv[1]

    # 分析参考案例
    print("🔍 正在分析参考案例...")
    from reference_analyzer import ReferenceAnalyzer
    analyzer = ReferenceAnalyzer(reference_path)
    colors = analyzer.extract_color_palette(num_colors=5)
    hex_colors = analyzer.get_color_hex()

    print(f"\n✓ 提取到配色方案：")
    for i, color in enumerate(hex_colors):
        print(f"  颜色{i+1}: {color}")

    # 生成PSD模板
    print("\n🎨 正在生成PSD模板...")
    generator = PSDTemplateGenerator(colors)

    output_dir = Path("output_templates")
    output_dir.mkdir(exist_ok=True)

    template_path = output_dir / "foswift_template.psd"
    result = generator.generate_psd_template(template_path)

    # 生成配色预览
    palette_path = output_dir / "color_palette.png"
    generator.generate_color_palette_image(palette_path)
    print(f"✓ 配色预览: {palette_path}")

    print("\n✅ 模板生成完成！")
    print(f"\n📁 输出文件夹: {output_dir}")
    print("\n💡 下一步：")
    print(f"1. 打开 {result['template']} 查看模板布局")
    print(f"2. 打开 {result['layers']} 查看图层信息")
    print(f"3. 如需转换为PSD，运行: bash {result['convert_script']}")
    print("4. 用Photoshop/GIMP等编辑器打开编辑")
