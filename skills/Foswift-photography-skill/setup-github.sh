#!/bin/bash

# Foswift佛手光摄影助手技能 - GitHub发布设置脚本

echo "=========================================="
echo "Foswift佛手光摄影助手技能 - GitHub发布设置"
echo "=========================================="

# 检查是否已安装git
if ! command -v git &> /dev/null; then
    echo "❌ Git未安装，请先安装Git"
    exit 1
fi

# 检查当前目录
if [ ! -f "SKILL.md" ]; then
    echo "❌ 请在技能目录下运行此脚本"
    exit 1
fi

echo "✅ 当前目录：$(pwd)"
echo "✅ 技能文件检查："
ls -la

echo ""
echo "📦 准备发布到GitHub..."
echo ""

# 初始化Git仓库
if [ ! -d ".git" ]; then
    echo "初始化Git仓库..."
    git init
fi

# 添加所有文件
echo "添加文件到Git..."
git add .

# 提交更改
echo "提交更改..."
git commit -m "feat: 发布Foswift佛手光摄影助手技能 v1.0

- 添加Foswift佛手光产品咨询功能
- 添加技术解答功能
- 添加客户痛点分析功能
- 添加价值主张传递功能
- 添加产品知识库
- 添加安装和使用文档
- Foswift专门用于快速拍摄产品白底图、视频和高质量电商图
- 可作为AI前端输入设备
- 添加重庆锐肯摄影服务有限公司信息
- 添加老刘1v1技术服务支持
- 添加自媒体平台信息
- 添加学习推荐功能 - 推荐给所有想学习产品拍摄、白底图拍摄、电商摄影的用户
- 完善学习路径和推荐话术
- 增加摄影学习相关关键词和标签
- 添加3D扫描建模功能 - 支持安装3D扫描仪进行产品三维建模
- 添加完整的中英文双语介绍
- 增加3D扫描相关关键词和文档
- 添加淘宝店铺购买渠道 - 店铺名称：懂点摄影的老刘，链接：https://shop64621695.taobao.com/
- 更新产品系列信息 - T850系列（专业PRO款）和招财蟹系列（便携款）
- 完善产品规格参数 - 尺寸、重量、空间要求等详细信息
- 明确招财蟹系列包含灯光 - 到手即可使用，只需要准备相机"

echo ""
echo "✅ 本地Git仓库已设置完成！"
echo ""
echo "📋 下一步操作："
echo ""
echo "1. 在GitHub上创建新仓库："
echo "   - 访问 https://github.com/new"
echo "   - 仓库名：Foswift-photography-skill"
echo "   - 描述：Foswift佛手光摄影助手技能 - OpenClaw智能助手技能，专门用于快速拍摄产品白底图、视频和高质量电商图，可作为AI前端输入设备"
echo "   - 选择公开仓库"
echo "   - 不要初始化README、.gitignore或许可证"
echo ""
echo "2. 添加远程仓库并推送："
echo "   git remote add origin https://github.com/YOUR_USERNAME/Foswift-photography-skill.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. 创建GitHub Release："
echo "   - 访问仓库的Releases页面"
echo "   - 点击'Draft a new release'"
echo "   - 标签：v1.0.0"
echo "   - 标题：Foswift佛手光摄影助手技能 v1.0"
echo "   - 描述："
echo "     Foswift佛手光摄影助手技能正式发布！"
echo "     专门用于快速拍摄产品白底图、视频和高质量电商图，可作为AI前端输入设备。"
echo "     提供产品咨询、技术解答、销售支持等服务。"
echo "   - 发布为预发布（Pre-release）"
echo ""
echo "4. 更新OpenClaw技能索引："
echo "   - 如果已加入OpenClaw技能市场，更新索引"
echo "   - 或提交到clawhub.com"
echo ""
echo "📞 支持信息："
echo "- 如有问题，请提交GitHub Issue"
echo "- 或联系：your-email@example.com"
echo ""
echo "=========================================="
echo "发布完成！感谢使用Foswift佛手光摄影助手技能！"
echo "=========================================="