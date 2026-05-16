# PSD文件使用说明

## 📁 已生成的PSD文件

### 1. 基础PSD（单图层）
- **文件名**: `foswift_template.psd`
- **大小**: 148KB
- **说明**: 完整的详情页模板，所有内容合并为单图层
- **用途**: 快速查看效果，不需要编辑结构

### 2. 分层PSD（推荐⭐）
- **文件名**: `foswift_template_layers.psd`
- **大小**: 186KB
- **说明**: 带有6个图层的PSD，每个区域独立成层
- **用途**: 可编辑图层，调整区域大小、颜色、位置

---

## 🎨 分层结构

`foswift_template_layers.psd` 包含6个图层：

| 图层名称 | Y坐标 | 高度 | 颜色 | 说明 |
|---------|-------|------|------|------|
| 标题区 | 0 | 400px | ⚪ #ffffff | 品牌标题、核心卖点、CTA |
| 产品主图区 | 400 | 800px | 🟡 #fffef4 | 产品展示、视觉冲击 |
| 功能特点区 | 1200 | 600px | 🟡 #fff200 | 核心功能、优势展示 |
| 对比区 | 1800 | 400px | ⚪ #fcfcfc | 传统vs佛手光对比 |
| 客户案例区 | 2200 | 600px | ⚪ #fefefe | 客户反馈、案例 |
| 底部CTA区 | 2800 | 200px | ⚪ #ffffff | 行动号召 |

---

## 🚀 如何使用PSD文件

### 方法1：使用Photoshop（推荐）

1. **打开PSD文件**
   ```
   打开 output_templates/foswift_template_layers.psd
   ```

2. **查看图层**
   - 打开图层面板（Window → Layers）
   - 你会看到6个图层（从下到上）

3. **编辑图层**
   - 双击图层可以解锁
   - 可以调整图层的不透明度
   - 可以改变图层混合模式
   - 可以删除或隐藏图层

4. **修改内容**
   - 选择文字工具，替换文字内容
   - 使用形状工具，调整区域大小
   - 添加新的图层，放置产品图片
   - 调整颜色和样式

5. **导出**
   - File → Export → Export As
   - 选择JPG或PNG格式
   - 导出为详情页图片

### 方法2：使用GIMP（免费）

1. **安装GIMP**
   ```bash
   # Ubuntu/Debian
   sudo apt install gimp

   # macOS
   brew install gimp

   # Windows
   # 从官网下载: https://www.gimp.org/downloads/
   ```

2. **打开PSD文件**
   ```
   File → Open
   选择 foswift_template_layers.psd
   ```

3. **编辑和导出**
   - 操作与Photoshop类似
   - File → Export As
   - 选择JPG或PNG格式

### 方法3：使用Photopea（在线免费）

1. **打开网站**
   ```
   https://www.photopea.com/
   ```

2. **打开PSD文件**
   ```
   File → Open
   选择 foswift_template_layers.psd
   ```

3. **编辑和导出**
   - 完全免费，无需安装
   - 支持PSD所有功能
   - File → Export As → JPG/PNG

---

## 💡 编辑建议

### 修改配色
1. 选择需要修改的图层
2. 双击图层填充色
3. 选择新的颜色
4. 点击OK

### 调整区域大小
1. 使用移动工具（V）
2. 选择需要调整的图层
3. 使用自由变换（Ctrl+T）
4. 调整大小和位置

### 添加产品图片
1. File → Open → 选择产品图片
2. 使用移动工具拖拽到详情页PSD中
3. 调整大小和位置
4. 修改图层混合模式为"正常"

### 替换文字
1. 选择文字工具（T）
2. 点击现有文字
3. 修改文字内容
4. 调整字体大小和颜色

### 添加新区域
1. 使用矩形工具（U）
2. 在合适的位置绘制矩形
3. 设置填充色和描边
4. 添加文字说明

---

## 📐 尺寸规范

- **画布宽度**: 750px
- **画布高度**: 3000px
- **DPI**: 72（Web标准）
- **色彩模式**: RGB
- **颜色深度**: 8位

---

## 🎯 适配电商平台

### 淘宝/天猫/拼多多
- 图片宽度：750px
- 图片高度：≤3000px
- 文件格式：JPG/PNG
- 文件大小：≤2MB

### 京东
- 图片宽度：750px
- 图片高度：≤3000px
- 文件格式：JPG/PNG
- 文件大小：≤2MB

### Amazon
- 图片宽度：1000-3000px
- 图片高度：1000-3000px
- 建议正方形
- 文件格式：JPG
- 文件大小：≤10MB

---

## 🔧 常见问题

### Q1: 为什么PSD打开后是单图层？
A: 你可能打开的是 `foswift_template.psd`，请使用 `foswift_template_layers.psd`。

### Q2: 为什么图层是锁定的？
A: 这是正常现象。双击图层可以解锁，解锁后可以编辑。

### Q3: 如何调整整个画布的高度？
A: Image → Canvas Size，修改Height值，注意不要裁剪内容。

### Q4: 可以导出为其他格式吗？
A: 可以。支持导出为JPG、PNG、GIF、TIFF等格式。

### Q5: 为什么颜色和网站预览不一样？
A: 可能是色彩空间问题。建议使用RGB模式，不要使用CMYK。

---

## 📞 需要帮助？

如果遇到任何问题，可以：

1. **查看其他文件**
   - `foswift_template_layers.json` - 图层详细配置
   - `foswift_template_zcool.html` - HTML版本，可浏览器预览

2. **查看分析报告**
   - `/workspace/projects/workspace/docs/ZCOOL_DESIGN_ANALYSIS.md`
   - `/workspace/projects/workspace/docs/CAPABILITY_CHECKLIST.md`

3. **重新生成**
   - 如需重新生成PSD，运行：
     ```bash
     bash output_templates/foswift_template_convert.sh
     ```

---

## ✅ 检查清单

使用PSD文件前，请确认：

- [ ] 已安装Photoshop、GIMP或使用Photopea
- [ ] 选择 `foswift_template_layers.psd`（分层版本）
- [ ] 画布尺寸为750×3000px
- [ ] 可以看到6个图层
- [ ] 可以编辑和修改图层

---

**祝你编辑顺利！👩‍💼🚀**
