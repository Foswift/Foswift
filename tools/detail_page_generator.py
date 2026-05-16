#!/usr/bin/env python3
"""
佛手光详情页自动化生成器
功能：
1. 批量处理产品图（调整大小、裁剪、格式转换）
2. 自动添加水印和文字标注
3. 生成详情页标准尺寸图片
4. 创建对比图和功能演示图
"""

import subprocess
import os
import glob
from pathlib import Path

class DetailPageGenerator:
    def __init__(self, input_dir, output_dir, watermark_path=None):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.watermark_path = watermark_path
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # 详情页标准尺寸
        self.WIDTH_750 = 750  # 淘宝标准宽度
        self.WIDTH_800 = 800  # 通用详情页宽度
        self.WIDTH_1200 = 1200  # 高清详情页宽度

    def process_image(self, input_path, output_path, width=750):
        """
        调整图片宽度，保持比例
        """
        cmd = [
            'ffmpeg', '-i', str(input_path),
            '-vf', f'scale={width}:-1',
            '-q:v', '2',  # 高质量
            '-y',  # 覆盖输出
            str(output_path)
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✓ 已处理: {input_path.name} → {output_path.name}")

    def batch_process(self, width=750):
        """
        批量处理文件夹中的所有图片
        """
        image_files = list(self.input_dir.glob('*.jpg')) + \
                     list(self.input_dir.glob('*.png')) + \
                     list(self.input_dir.glob('*.jpeg'))

        print(f"📁 找到 {len(image_files)} 张图片")

        for img_file in image_files:
            output_path = self.output_dir / img_file.name
            self.process_image(img_file, output_path, width)

    def create_comparison_image(self, before_img, after_img, output_path):
        """
        创建对比图：左边传统方式，右边佛手光
        """
        # 将两张图片水平拼接
        cmd = [
            'ffmpeg', '-i', str(before_img), '-i', str(after_img),
            '-filter_complex', '[0:v]scale=800:-1[left];[1:v]scale=800:-1[right];[left][right]hstack',
            '-y', str(output_path)
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✓ 已创建对比图: {output_path.name}")

    def create_feature_diagram(self, product_img, output_path, features):
        """
        创建功能特点标注图
        features = [{"x": 100, "y": 100, "text": "纯白底技术"}, ...]
        """
        # 这里需要用ImageMagick或其他工具添加文字标注
        pass  # 需要安装ImageMagick后实现

    def add_watermark(self, img_path, watermark_path, output_path):
        """
        添加水印
        """
        if watermark_path and Path(watermark_path).exists():
            cmd = [
                'ffmpeg', '-i', str(img_path), '-i', watermark_path,
                '-filter_complex', 'overlay=W-w-10:H-h-10',
                '-y', str(output_path)
            ]
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✓ 已添加水印: {output_path.name}")

# 使用示例
if __name__ == "__main__":
    generator = DetailPageGenerator(
        input_dir="/path/to/product/images",
        output_dir="/path/to/output/detail_page_images"
    )

    # 1. 批量处理图片
    generator.batch_process(width=750)

    # 2. 创建对比图
    # generator.create_comparison_image(
    #     before_img="traditional.jpg",
    #     after_img="foswift.jpg",
    #     output_path="comparison.jpg"
    # )

    print("\n✅ 详情页图片处理完成！")
