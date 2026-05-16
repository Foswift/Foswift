# 佛手光详情页模板 - Photoshop制作指南

## 📐 基本信息
- **画布尺寸**：750 x 5000 px
- **颜色模式**：RGB
- **字体**：思源黑体（Noto Sans SC / Source Han Sans CN）

---

## 🎨 颜色规范

| 颜色名称 | HEX色值 | 用途 |
|---------|---------|------|
| 纯白 | #FFFFFF | 主背景 |
| 亮黄色 | #FFF200 | CTA按钮、装饰 |
| 淡黄色 | #FFFEF4 | 卖点区背景 |
| 浅灰色 | #FCFCFC | 内容卡片背景 |
| 深灰色 | #F5F5F5 | 参数行背景 |
| 主文字 | #323232 | 标题文字 |
| 次文字 | #646464 | 副标题、描述 |
| 深色背景 | #2A292E | CTA区背景 |
| 白色文字 | #FFFFFF | 深色背景上的文字 |
| 黄色文字 | #FFF200 | 深色背景上的强调 |

---

## 📝 文字规范（按图层顺序）

### 第1区：首屏标题
```
位置：Y = 80
字体：思源黑体 Bold
字号：48px
颜色：#323232
内容：PRODUCT NAME

位置：Y = 150
字体：思源黑体 Regular
字号：24px
颜色：#646464
内容：Subtitle / Core Selling Point
```

### 第2区：装饰线
```
位置：X=50, Y=220
尺寸：宽150px x 高5px
颜色：#FFF200
```

### 第3区：产品图占位符
```
位置：X=50, Y=280
尺寸：宽650px x 高350px
背景色：#FCFCFC
边框：2px #B4B4B4
```

### 第4区：卖点区
```
位置：Y=700，高度500px
背景色：#FFFEF4

位置：Y=730
字体：思源黑体 Bold
字号：32px
颜色：#323232
内容：CORE FEATURES

4个卡片：X=[50,230,410,590]，Y=850
尺寸：宽150px x 高250px
背景色：#FFFFFF
边框：1px #E0E0E0
```

**卡片内文字：**
```
标题位置：Y=940
字体：思源黑体 Bold
字号：14px
颜色：#323232
内容：Feature 1/2/3/4

描述位置：Y=980
字体：思源黑体 Regular
字号：12px
颜色：#646464
内容：Description text here
```

### 第5区：效率对比
```
位置：Y=1250，高度500px
背景色：#FFF200

位置：Y=1280
字体：思源黑体 Bold
字号：32px
颜色：#323232
内容：EFFICIENCY COMPARISON

左侧卡片：X=50, Y=1380
尺寸：宽300px x 高340px
背景色：#FCFCFC

右侧卡片：X=400, Y=1380
尺寸：宽300px x 高340px
背景色：#2A292E
```

**左侧卡片文字：**
```
位置：Y=1400
字体：思源黑体 Bold
字号：20px
颜色：#505050
内容：Traditional

位置：Y=1460, 1500, 1540, 1580
字体：思源黑体 Regular
字号：16px
颜色：#787878
内容：
X 40 minutes
X Complex setup
X Needs editing
X High cost
```

**VS圆：**
```
位置：X=310, Y=1500
尺寸：100x100px
背景色：#2A292E
内容：VS（白色，18px Bold）
```

**右侧卡片文字：**
```
位置：Y=1400
字体：思源黑体 Bold
字号：20px
颜色：#FFF200
内容：Upgrade

位置：Y=1460, 1500, 1540, 1580
字体：思源黑体 Regular
字号：16px
颜色：#FFFFFF
内容：
+ 5-10 seconds
+ One step
+ No editing
+ Cost control
```

### 第6区：产品展示
```
位置：Y=1830
字体：思源黑体 Bold
字号：32px
颜色：#323232
内容：PRODUCT SHOWCASE

产品图占位符（3个）：
X=[50, 250, 450]，Y=1950
尺寸：宽180px x 高100px
背景色：#FCFCFC
边框：2px #B4B4B4
```

### 第7区：场景应用
```
位置：Y=2530
字体：思源黑体 Bold
字号：32px
颜色：#323232
内容：APPLICATION SCENES

3个场景卡片：
X=[50, 280, 510]，Y=2650
尺寸：宽200px x 高300px
背景色：#FFFFFF
边框：1px #E0E0E0

卡片内容：
位置：Y=2730
字体：思源黑体 Bold
字号：14px
颜色：#323232
内容：Scene 1/2/3

位置：Y=2770
字体：思源黑体 Regular
字号：11px
颜色：#787878
内容：
Description
text here
```

### 第8区：客户案例
```
位置：Y=3130
字体：思源黑体 Bold
字号：32px
颜色：#323232
内容：CUSTOMER CASES

引用卡片：
位置：X=50, Y=3230
尺寸：宽650px x 高290px
背景色：#FCFCFC

引用文字：
位置：Y=3250
字体：思源黑体 Bold
字号：20px
颜色：#505050
内容："200x efficiency improvement!"

来源：
位置：Y=3310
字体：思源黑体 Regular
字号：14px
颜色：#787878
内容：- Taobao store owner
```

### 第9区：技术参数
```
位置：Y=3630
字体：思源黑体 Bold
字号：32px
颜色：#323232
内容：TECHNICAL SPECS

参数行（4行）：
X=120, Y=[3750, 3820, 3890, 3960]
尺寸：宽500px x 高60px
背景色：#FCFCFC

参数内容：
标签（X=140, 16px Bold, #505050）：
Model:
Space:
Features:
Warranty:

数值（X=300, 16px Regular, #323232）：
T850 / MINI
2.5 x 2.5m
White background / 360 rotation
1 year technical support
```

### 第10区：底部CTA
```
位置：Y=4250，高度450px
背景色：#2A292E

位置：Y=4280
字体：思源黑体 Bold
字号：32px
颜色：#FFFFFF
内容：START PROFESSIONAL PHOTOGRAPHY

CTA按钮：
位置：X=200, Y=4380
尺寸：宽350px x 高90px
背景色：#FFF200
圆角：8px

按钮文字：
位置：Y=4405
字体：思源黑体 Bold
字号：20px
颜色：#323232
内容：CONTACT US

联系信息：
位置：Y=4520
字体：思源黑体 Regular
字号：14px
颜色：#B4B4B4
内容：Douyin: @懂点摄影的老刘  |  WeChat: contact
```

---

## 🚀 Photoshop快速操作步骤

### 1. 打开PSD
打开 `详情页模板_合并.psd`

### 2. 添加文字图层
在每个指定位置添加文字图层，使用上述字体规范。

### 3. 图层命名建议
按照编号命名，如：
- `02_标题`
- `06_卖点标题`
- `13_传统标题`
- `23_CTA按钮文字`

### 4. 保存
文件 → 另存为 → `详情页模板_最终.psd`

---

## ⏱ 预计时间
- 添加所有文字图层：约10-15分钟
- 调整细节：约5分钟
- **总计：约20分钟**

---

## 💡 小技巧
1. 使用PS的「字符样式」功能批量管理同类文字
2. 先完成一个卡片，然后复制粘贴修改内容
3. 对齐时使用智能参考线确保整齐
