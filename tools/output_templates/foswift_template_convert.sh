#!/bin/bash
# 将PNG模板转换为PSD（需要安装ImageMagick）
# 使用方法: bash foswift_template_convert.sh

convert foswift_template.png foswift_template.psd

echo "✓ PSD文件已生成: foswift_template.psd"
echo "✓ 可以用Photoshop打开编辑了"
