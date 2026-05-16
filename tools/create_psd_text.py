#!/usr/bin/env python3
"""
使用GIMP创建带文本图层的PSD文件
文本使用思源黑体（Noto Sans CJK / Source Han Sans）
"""

import sys
import os

# 加载GIMP Python-Fu
import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp, GimpUi, Gegl, GLib, Gio
Gimp.init(sys.argv[1:])

from gimp import pdb, foreground, background
import math

# 画布尺寸
WIDTH = 750
HEIGHT = 5000

# 配色方案
COLORS = {
    "white": (255, 255, 255),
    "yellow": (255, 242, 0),
    "light_yellow": (255, 254, 244),
    "gray_light": (252, 252, 252),
    "gray": (245, 245, 245),
    "dark": (42, 41, 46),
    "text_dark": (50, 50, 50),
    "text_gray": (100, 100, 100),
}

# 创建新图像
print("创建图像...")
img = pdb.gimp_image_new(WIDTH, HEIGHT, 0)  # 0 = RGB
pdb.gimp_image_undo_disable(img)

# 创建背景图层
bg_layer = pdb.gimp_layer_new(img, "背景", WIDTH, HEIGHT, 1, 100, 0)
pdb.gimp_image_insert_layer(img, bg_layer, None, 0)
pdb.gimp_context_set_foreground(COLORS["white"])
pdb.gimp_drawable_fill(bg_layer, 0)  # 0 = foreground fill

# 辅助函数：添加矩形图层
def add_rect_layer(img, name, y, h, color):
    layer = pdb.gimp_layer_new(img, name, WIDTH, h, 1, 100, 0)
    pdb.gimp_image_insert_layer(img, layer, None, -1)
    pdb.gimp_layer_set_offsets(layer, 0, y)
    pdb.gimp_context_set_foreground(color)
    pdb.gimp_drawable_fill(layer, 0)
    return layer

# 辅助函数：添加文本图层（真正的文本！）
def add_text_layer(img, name, text, x, y, size, color, font="Sans"):
    # 创建文本图层
    text_layer = pdb.gimp_text_layer_new(img, text, font, size, 0)
    pdb.gimp_image_insert_layer(img, text_layer, None, -1)
    pdb.gimp_layer_set_offsets(text_layer, x, y)
    pdb.gimp_text_layer_set_color(text_layer, color)
    return text_layer

# 辅助函数：添加带边框的矩形
def add_card_with_text(img, name, x, y, w, h, bg_color, title, desc_lines, text_color, font="Sans"):
    # 卡片背景
    card = pdb.gimp_layer_new(img, name, w, h, 1, 100, 0)
    pdb.gimp_image_insert_layer(img, card, None, -1)
    pdb.gimp_layer_set_offsets(card, x, y)
    pdb.gimp_context_set_foreground(bg_color)
    pdb.gimp_drawable_fill(card, 0)
    
    # 标题
    title_layer = pdb.gimp_text_layer_new(img, title, font, 18, 0)
    pdb.gimp_image_insert_layer(img, title_layer, None, -1)
    pdb.gimp_layer_set_offsets(title_layer, x + 20, y + 20)
    pdb.gimp_text_layer_set_color(title_layer, text_color)
    
    # 描述行
    for i, line in enumerate(desc_lines):
        desc_layer = pdb.gimp_text_layer_new(img, f"• {line}", font, 14, 0)
        pdb.gimp_image_insert_layer(img, desc_layer, None, -1)
        pdb.gimp_layer_set_offsets(desc_layer, x + 20, y + 60 + i * 30)
        pdb.gimp_text_layer_set_color(desc_layer, COLORS["text_gray"])
    
    return card

# ===== 开始构建设计 =====

# 1. 首屏区 - 标题
title_layer = add_text_layer(img, "标题_产品名称", "PRODUCT NAME", 50, 80, 48, COLORS["text_dark"])
subtitle_layer = add_text_layer(img, "副标题", "Subtitle / Core Selling Point", 50, 150, 24, COLORS["text_gray"])

# 黄色装饰线
add_rect_layer(img, "装饰线", 220, 5, COLORS["yellow"])

# 2. 首屏区 - 产品图占位符（用矩形表示）
add_rect_layer(img, "产品图_可替换", 280, 350, COLORS["gray_light"])

# 3. 卖点区背景
add_rect_layer(img, "卖点区背景", 700, 500, COLORS["light_yellow"])

# 卖点标题
add_text_layer(img, "卖点标题", "CORE FEATURES", 50, 730, 32, COLORS["text_dark"])

# 4个功能卡片
card_width = 150
margin = 50
gap = 30
for i in range(4):
    x = margin + i * (card_width + gap)
    add_card_with_text(img, f"卖点{i+1}", x, 850, card_width, 250, 
                      COLORS["white"], f"Feature {i+1}",
                      ["Description", "text here"], COLORS["text_dark"])

# 4. 对比区背景
add_rect_layer(img, "对比区背景", 1250, 500, COLORS["yellow"])

# 对比标题
add_text_layer(img, "对比标题", "EFFICIENCY COMPARISON", 50, 1280, 32, COLORS["text_dark"])

# 左侧卡片 - 传统方式
add_rect_layer(img, "左侧卡片", 50, 1380, 300, 340, COLORS["gray_light"])
add_text_layer(img, "左侧标题", "Traditional", 70, 1400, 24, COLORS["text_gray"])
add_text_layer(img, "左侧内容1", "X 40 minutes", 70, 1460, 18, COLORS["text_gray"])
add_text_layer(img, "左侧内容2", "X Complex setup", 70, 1500, 18, COLORS["text_gray"])
add_text_layer(img, "左侧内容3", "X Needs editing", 70, 1540, 18, COLORS["text_gray"])
add_text_layer(img, "左侧内容4", "X High cost", 70, 1580, 18, COLORS["text_gray"])

# VS 圆圈
vs_circle = add_rect_layer(img, "VS标识", 310, 1500, 100, 100, COLORS["dark"])
add_text_layer(img, "VS文字", "VS", 340, 1525, 24, (255, 255, 255))

# 右侧卡片 - 升级方案
add_rect_layer(img, "右侧卡片", 400, 1380, 300, 340, COLORS["dark"])
add_text_layer(img, "右侧标题", "Upgrade", 420, 1400, 24, COLORS["yellow"])
add_text_layer(img, "右侧内容1", "+ 5-10 seconds", 420, 1460, 18, (255, 255, 255))
add_text_layer(img, "右侧内容2", "+ One step", 420, 1500, 18, (255, 255, 255))
add_text_layer(img, "右侧内容3", "+ No editing", 420, 1540, 18, (255, 255, 255))
add_text_layer(img, "右侧内容4", "+ Cost control", 420, 1580, 18, (255, 255, 255))

# 5. 产品展示区
add_rect_layer(img, "产品展示背景", 1800, 600, COLORS["white"])
add_text_layer(img, "产品展示标题", "PRODUCT SHOWCASE", 50, 1830, 32, COLORS["text_dark"])

# 3个产品图占位符
for i in range(3):
    add_rect_layer(img, f"产品图{i+1}", 1950 + i * 120, 100, COLORS["gray_light"])

# 6. 场景区
add_rect_layer(img, "场景区背景", 2500, 550, COLORS["gray_light"])
add_text_layer(img, "场景标题", "APPLICATION SCENES", 50, 2530, 32, COLORS["text_dark"])

# 3个场景卡片
scene_width = 200
for i in range(3):
    x = 50 + i * (scene_width + 30)
    add_card_with_text(img, f"场景{i+1}", x, 2650, scene_width, 300,
                      COLORS["white"], f"Scene {i+1}",
                      ["Description", "text here"], COLORS["text_dark"])

# 7. 案例区
add_rect_layer(img, "案例区背景", 3200, 450, COLORS["white"])
add_text_layer(img, "案例标题", "CUSTOMER CASES", 50, 3130, 32, COLORS["text_dark"])

# 案例引用卡片
add_rect_layer(img, "引用卡片", 50, 3230, 650, 290, COLORS["gray_light"])
add_text_layer(img, "引用文字", '"200x efficiency improvement!"', 70, 3250, 24, COLORS["text_dark"])
add_text_layer(img, "引用来源", "- Taobao store owner", 70, 3310, 18, COLORS["text_gray"])

# 8. 参数区
add_rect_layer(img, "参数区背景", 3750, 400, COLORS["white"])
add_text_layer(img, "参数标题", "TECHNICAL SPECS", 50, 3780, 32, COLORS["text_dark"])

# 参数表格
specs = [
    ("Model:", "T850 / MINI"),
    ("Space:", "2.5 x 2.5m"),
    ("Features:", "White background / 360 rotation"),
    ("Warranty:", "1 year technical support"),
]
for i, (label, value) in enumerate(specs):
    y = 3850 + i * 70
    add_rect_layer(img, f"参数行{i}", 100, y, 550, 60, COLORS["gray_light"])
    add_text_layer(img, f"参数标签{i}", label, 120, y + 15, 18, COLORS["text_gray"])
    add_text_layer(img, f"参数值{i}", value, 300, y + 15, 18, COLORS["text_dark"])

# 9. CTA区
add_rect_layer(img, "CTA背景", 4250, 450, COLORS["dark"])
add_text_layer(img, "CTA标题", "START PROFESSIONAL PHOTOGRAPHY", 50, 4280, 32, (255, 255, 255))

# CTA按钮
add_rect_layer(img, "CTA按钮", 200, 4380, 350, 80, COLORS["yellow"])
add_text_layer(img, "CTA按钮文字", "CONTACT US", 280, 4400, 24, COLORS["text_dark"])

# 联系信息
add_text_layer(img, "联系信息", "Douyin: @懂点摄影的老刘  |  WeChat: contact", 50, 4500, 18, (180, 180, 180))

# ===== 保存PSD =====
print("保存PSD...")
output_path = "/workspace/projects/workspace/tools/output_templates/专业分层模板_文本图层.psd"
pdb.gimp_file_save(img, output_path)
print(f"PSD已保存: {output_path}")

# 清理
pdb.gimp_image_delete(img)
print("完成!")
