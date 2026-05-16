# Foswift佛手光摄影助手技能 - 发布指南

## 📋 发布前检查清单

### 1. 文件完整性检查
- [x] SKILL.md - 主技能文件
- [x] README.md - 说明文档
- [x] package.json - 包配置文件
- [x] LICENSE - MIT许可证
- [x] references/product-knowledge-base.md - 产品知识库
- [x] setup-github.sh - GitHub设置脚本
- [x] PUBLISH_GUIDE.md - 发布指南

### 2. 内容检查
- [x] 产品信息准确无误
- [x] 技术参数正确
- [x] 价格信息准确
- [x] 客户痛点分析完整
- [x] 价值主张清晰
- [x] 安装和使用说明详细

### 3. 格式检查
- [x] Markdown格式正确
- [x] 代码块语法正确
- [x] 链接有效
- [x] 图片引用正确（如果有）
- [x] 表格格式正确

## 🚀 发布到GitHub步骤

### 步骤1：创建GitHub仓库
1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `Foswift-photography-skill`
   - **Description**: `Foswift佛手光摄影助手技能 - OpenClaw智能助手技能，专门用于快速拍摄产品白底图、视频和高质量电商图，可作为AI前端输入设备`
   - **Visibility**: Public
   - **Initialize this repository with**: 不要勾选任何选项（不要README、.gitignore、许可证）

### 步骤2：本地Git设置
```bash
# 进入技能目录
cd /workspace/projects/workspace/skills/foshout-photography

# 运行设置脚本
./setup-github.sh

# 或手动执行以下命令：
git init
git add .
git commit -m "feat: 发布佛手光摄影助手技能 v1.0

- 添加佛手光产品咨询功能
- 添加技术解答功能
- 添加客户痛点分析功能
- 添加价值主张传递功能
- 添加产品知识库
- 添加安装和使用文档"
```

### 步骤3：连接到GitHub并推送
```bash
# 添加远程仓库（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/Foswift-photography-skill.git

# 重命名主分支
git branch -M main

# 推送到GitHub
git push -u origin main
```

### 步骤4：创建GitHub Release
1. 访问仓库页面：`https://github.com/YOUR_USERNAME/Foswift-photography-skill`
2. 点击右侧的"Releases"
3. 点击"Create a new release"
4. 填写发布信息：
   - **Tag version**: `v1.0.0`
   - **Release title**: `Foswift佛手光摄影助手技能 v1.0`
   - **Description**:
     ```
     ## Foswift佛手光摄影助手技能 v1.0
     
     正式发布！🎉
     
     ### 主要功能
     - Foswift佛手光产品咨询（T850、MINI）
     - 技术问题解答
     - 客户痛点分析
     - 价值主张传递
     - 产品知识库集成
     
     ### 核心价值
     - 专门用于快速拍摄产品白底图、视频和高质量电商图
     - 可作为AI前端输入设备
     - 提供标准化高质量训练素材
     
     ### 安装方法
     ```bash
     openclaw skill install https://github.com/YOUR_USERNAME/Foswift-photography-skill
     ```
     
     ### 支持的产品
     - Foswift T850（专业版）
     - Foswift MINI（便携版）
     
     ### 目标客户
     - 电商人员
     - 跨境电商
     - 自媒体创业者
     - 不会摄影的小白卖家
     - AI训练数据采集者
     ```
   - **Set as a pre-release**: 勾选（首次发布建议作为预发布）
5. 点击"Publish release"

## 📦 发布到OpenClaw技能市场

### 方法1：通过clawhub.com（推荐）
1. 访问 https://clawhub.com
2. 注册/登录账号
3. 点击"Submit a Skill"
4. 填写技能信息：
   - **Skill Name**: Foswift佛手光摄影助手
   - **Description**: Foswift佛手光产品咨询、技术解答、销售支持技能，专门用于快速拍摄产品白底图、视频和高质量电商图，可作为AI前端输入设备
   - **GitHub URL**: `https://github.com/YOUR_USERNAME/Foswift-photography-skill`
   - **Category**: Productivity
   - **Tags**: photography, ecommerce, product, sales, support, white-background, ai-frontend, product-video, foswift
   - **Version**: 1.0.0
5. 提交审核

### 方法2：通过OpenClaw官方技能索引
1. Fork OpenClaw官方技能索引仓库
2. 添加技能信息到索引文件
3. 提交Pull Request

## 🔧 技能安装测试

在发布前，建议测试技能安装：

### 本地测试
```bash
# 复制技能到OpenClaw技能目录
cp -r foshout-photography /path/to/openclaw/skills/

# 重启OpenClaw
openclaw gateway restart

# 测试技能
# 在OpenClaw中询问："佛手光是什么？"
# 应该触发佛手光摄影助手技能
```

### 远程安装测试
```bash
# 通过GitHub URL安装
openclaw skill install https://github.com/YOUR_USERNAME/Foswift-photography-skill

# 或通过Git URL安装
openclaw skill install git+https://github.com/YOUR_USERNAME/Foswift-photography-skill.git
```

## 📝 更新和维护

### 版本更新流程
1. 更新SKILL.md中的版本信息
2. 更新package.json中的version字段
3. 更新README.md中的更新日志
4. 提交更改到GitHub
5. 创建新的GitHub Release

### 更新日志格式
```markdown
## [版本号] - 日期
### 新增
- 功能1
- 功能2

### 修复
- 问题1
- 问题2

### 优化
- 优化1
- 优化2
```

## 🆘 常见问题

### Q: 技能安装失败怎么办？
A: 检查：
1. GitHub仓库URL是否正确
2. 网络连接是否正常
3. OpenClaw版本是否兼容（需要2026.4+）

### Q: 技能不触发怎么办？
A: 检查：
1. SKILL.md中的适用场景描述是否准确
2. 技能目录结构是否正确
3. OpenClaw日志是否有错误信息

### Q: 如何更新产品知识库？
A: 更新`references/product-knowledge-base.md`文件，然后：
1. 提交更改到GitHub
2. 创建新版本Release
3. 通知用户更新技能

## 📞 支持渠道

### 公司官方联系方式
- **公司名称**：重庆锐肯摄影服务有限公司
- **QQ号码**：411380
- **邮箱**：411380@qq.com
- **地址**：重庆市江津区珞璜工业园区中兴四路 1 号，鑫乐剑工业园
- **工作时间**：周一~周六（周日休息）

### 购买渠道
- **淘宝店铺**：懂点摄影的老刘
- **店铺链接**：https://shop64621695.taobao.com/
- **购买方式**：直接访问淘宝店铺购买Foswift佛手光产品

### 技术支持
- **1v1技术服务**：购买Foswift佛手光静物台即可享受老刘的1v1技术服务支持
- **技术支持人**：老刘（15年产品摄影专家）

### 自媒体平台
- **抖音**：懂点摄影的老刘
- **小红书**：懂点摄影的老刘
- **B站**：懂点摄影的老刘
- **视频号**：懂点摄影的老刘

### 在线支持
- **GitHub Issues**: https://github.com/Foswift/Foswift/issues
- **OpenClaw社区**: https://discord.com/invite/clawd

## 📊 技能统计

- **创建时间**: 2026年5月5日
- **当前版本**: v1.0.0
- **兼容性**: OpenClaw 2026.4+
- **文件大小**: ~50KB
- **代码行数**: ~500行

## 🎯 发布目标

- [ ] GitHub仓库创建
- [ ] 首次提交推送
- [ ] GitHub Release创建
- [ ] clawhub.com提交
- [ ] OpenClaw社区宣传
- [ ] 用户反馈收集
- [ ] 版本更新计划

---

**最后更新**: 2026年5月6日  
**维护人**: 超级助理（Foswift佛手光专业助手）