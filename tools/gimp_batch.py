#!/usr/bin/env python3
"""
使用GIMP创建带文本图层的PSD
"""

import subprocess
import os
import sys

# GIMP批处理脚本 (Scheme)
script = '''
(define (create-detail-page filename)
  (let* (
    (img (car (gimp-image-new 750 5000 RGB)))
    (bg-layer (car (gimp-layer-new img "背景" 750 5000 RGB-IMAGE 100 NORMAL-MODE)))
    (title-layer (car (gimp-text-layer-new img "PRODUCT NAME" "WenQuanYi Zen Hei" 48 0)))
    (subtitle-layer (car (gimp-text-layer-new img "Subtitle / Core Selling Point" "WenQuanYi Zen Hei" 24 0)))
  )
    ; 添加图层
    (gimp-image-insert-layer img bg-layer 0 0)
    (gimp-image-insert-layer img title-layer 0 0)
    (gimp-image-insert-layer img subtitle-layer 0 0)
    
    ; 设置位置
    (gimp-layer-set-offsets title-layer 50 80)
    (gimp-layer-set-offsets subtitle-layer 50 150)
    
    ; 设置颜色
    (gimp-text-layer-set-color title-layer '(50 50 50))
    (gimp-text-layer-set-color subtitle-layer '(100 100 100))
    
    ; 填充背景
    (gimp-context-set-foreground '(255 255 255))
    (gimp-drawable-fill bg-layer FILL-FOREGROUND)
    
    ; 保存
    (file-psd-save RUN-NONINTERACTIVE img bg-layer filename filename)
    (gimp-image-delete img)
  )
)

; 运行
(create-detail-page "''' + sys.argv[1] + '''")
'''

print("创建GIMP批处理脚本...")
with open('/tmp/create_psd.scm', 'w') as f:
    f.write(script)

print("运行GIMP批处理...")
result = subprocess.run([
    'gimp',
    '--no-interface',
    '--batch-interpreter', 'plug-in-script-fu-eval',
    '-b', f'(load "/tmp/create_psd.scm")',
    '-b', '(gimp-quit 0)'
], capture_output=True, text=True)

print("stdout:", result.stdout)
print("stderr:", result.stderr)
