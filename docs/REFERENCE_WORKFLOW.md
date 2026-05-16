# 佛手光详情页 - 参考案例工作流

## 🎯 核心思路

**参考案例 → 分析配色/结构 → 生成可编辑模板 → 用户微调完善**

这个工作流让你可以：
1. 给我一个优秀的电商详情页作为参考
2. 我自动分析它的配色和布局
3. 生成一个基于参考案例的可编辑模板
4. 你用PS/GIMP等工具微调，快速完成

---

## 📦 已安装工具

✅ **已安装：**
- Pillow (Python图像处理库)
- psd-tools (PSD文件处理库)
- ffmpeg (多媒体处理)
- numpy (数学计算)

✅ **已创建工具：**
- `reference_analyzer.py` - 参考案例分析器
- `psd_generator.py` - PSD模板生成器

---

## 🚀 快速开始（3步）

### 第1步：准备参考案例

找一个优秀的电商详情页截图或图片，例如：
- 同类产品的详情页
- 你喜欢的设计风格
- 行业标杆案例

### 第2步：分析参考案例

```bash
cd /workspace/projects/workspace/tools

python3 psd_generator.py /path/to/reference_image.png
```

**会自动生成：**
- 📊 配色方案分析
- 🎨 基于参考案例的模板布局
- 📋 图层信息文件
- 🔄 PSD转换脚本

### 第3步：编辑和微调

用你喜欢的工具打开生成的模板：
- **Photoshop** (推荐)
- **GIMP** (免费开源)
- **Photopea** (在线免费，类似PS)

---

## 📁 输出文件说明

### 1. 模板文件
```
output_templates/
├── foswift_template.png      # 可编辑的PNG模板（推荐）
├── foswift_template_layers.json  # 图层信息
├── foswift_template_convert.sh  # PSD转换脚本
└── color_palette.png         # 配色预览图
```

### 2. 图层信息JSON示例
```json
{
  "width": 750,
  "height": 3000,
  "colors": ["#ffffff", "#f5f5f5", "#e0e0e0", "#cccccc", "#333333"],
  "layers": [
    {
      "name": "标题区",
      "y": 0,
      "height": 400,
      "color": [255, 255, 255]
    },
    {
      "name": "产品主图区",
      "y": 400,
      "height": 800,
      "color": [51, 51, 51]
    }
  ]
}
```

---

## 🎨 支持的输出格式

| 格式 | 可编辑性 | 推荐工具 | 优点 |
|------|----------|----------|------|
| **PNG** | ✅ 高 | PS/GIMP/任何编辑器 | 通用性强，质量高 |
| **PSD** | ✅ 最高 | Photoshop | 图层管理强大 |
| **HTML/CSS** | ✅ 中 | 代码编辑器 | 网页友好，易于修改 |
| **SVG** | ✅ 高 | 矢量编辑器 | 无损缩放 |

---

## 💡 使用场景示例

### 场景1：参考淘宝某热门产品详情页

```bash
# 1. 截图淘宝详情页
# 2. 保存为 taobao_reference.png

# 3. 分析并生成模板
python3 psd_generator.py taobao_reference.png

# 4. 打开 foswift_template.png，替换产品图和文字
```

### 场景2：参考京东高端产品详情页

```bash
# 1. 找到参考图
python3 psd_generator.py jd_reference.png

# 2. 生成的模板会自动采用京东的配色方案
# 3. 微调后用于佛手光
```

### 场景3：参考行业标杆（Apple风格）

```bash
# 1. 参考极简风格设计
python3 psd_generator.py apple_reference.png

# 2. 生成极简风格模板
# 3. 添加佛手光产品元素
```

---

## 🛠️ 高级功能

### 自定义配色方案

如果你想手动指定配色，创建一个JSON文件：

```json
{
  "colors": [
    {"hex": "#ffffff", "name": "主背景"},
    {"hex": "#333333", "name": "主文字"},
    {"hex": "#ff6b6b", "name": "强调色"},
    {"hex": "#f0f0f0", "name": "次要背景"},
    {"hex": "#999999", "name": "次要文字"}
  ]
}
```

### 自定义布局结构

编辑生成的 `_layers.json` 文件，调整各个区域的大小和位置：

```json
{
  "layers": [
    {"name": "标题区", "y": 0, "height": 500},
    {"name": "产品主图区", "y": 500, "height": 1000},
    {"name": "功能特点区", "y": 1500, "height": 800}
  ]
}
```

### 批量处理多个参考案例

```bash
# 创建一个bash脚本批量处理
for file in reference_images/*.png; do
  python3 psd_generator.py "$file"
done
```

---

## 🎯 推荐工作流

### 标准流程（推荐）

```
1. 找参考案例
   ↓
2. 分析配色和结构
   ↓
3. 生成PNG模板
   ↓
4. 用Photoshop/GIMP编辑
   ↓
5. 导出为JPG/PNG
   ↓
6. 上传到电商平台
```

### 快速流程

```
1. 找参考案例
   ↓
2. 生成HTML模板
   ↓
3. 浏览器截图
   ↓
4. 直接使用
```

---

## 📊 详情页尺寸规范

| 平台 | 宽度 | 高度建议 | 输出格式 |
|------|------|----------|----------|
| 淘宝/天猫 | 750px | ≤3000px | JPG/PNG |
| 京东 | 750px | ≤3000px | JPG/PNG |
| 拼多多 | 750px | ≤3000px | JPG/PNG |
| Amazon | 1000px | 正方形 | JPG |

---

## ❓ 常见问题

### Q1: 生成的模板不是真正的PSD怎么办？
**A:** 运行转换脚本：
```bash
bash output_templates/foswift_template_convert.sh
```

### Q2: 我想用GIMP而不是PS怎么办？
**A:** 直接编辑 `foswift_template.png`，GIMP对PNG的图层支持很好。

### Q3: 如何调整模板的配色？
**A:** 编辑 `_layers.json` 文件中的 `colors` 数组。

### Q4: 可以添加更多区域吗？
**A:** 编辑 `_layers.json` 文件中的 `layers` 数组，添加新的区域。

---

## 🎬 下一步行动

### 立即可以做的：

1. **准备一个参考案例图片**
   - 哪怕是一个普通的详情页截图都可以

2. **测试工具**
   ```bash
   python3 psd_generator.py /path/to/your/reference.png
   ```

3. **查看输出结果**
   ```bash
   ls -lh output_templates/
   ```

### 短期目标：

1. 为T850生成详情页模板
2. 为MINI生成详情页模板
3. 建立佛手光的配色方案库

### 长期目标：

1. 积累多个优秀的参考案例
2. 建立佛手光专属的设计规范
3. 创建模板库，快速生成不同风格的详情页

---

## 📞 需要帮助？

准备好参考案例后，告诉我：
1. 参考案例的路径
2. 你想生成哪款产品的模板（T850/MINI）
3. 你希望的输出格式（PNG/PSD/HTML）

我立即帮你生成！👩‍💼🚀
