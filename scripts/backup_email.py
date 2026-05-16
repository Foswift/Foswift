#!/usr/bin/env python3
"""
超级助理自动备份系统
每周自动打包并发送备份到邮箱
"""

import os
import sys
import smtplib
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import subprocess

# 配置
WORKSPACE = "/workspace/projects/workspace"
BACKUP_DIR = "/tmp/openclaw_backups"
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465
SENDER_EMAIL = "411380@qq.com"
RECEIVER_EMAIL = "411380@qq.com"
PASSWORD = "ovlfejyvkgvgcaad"

# 需要备份的文件和目录
BACKUP_ITEMS = {
    "知识库": [
        "MEMORY/FO_SHOUT_PRODUCT_KNOWLEDGE_BASE.md",
        "MEMORY.md",
    ],
    "数字员工_老刘": [
        "agents/photography/SKILL.md",
        "agents/photography/SOUL.md",
        "agents/photography/TOOLS.md",
        "agents/photography/AGENTS.md",
        "agents/photography/MEMORY.md",
        "agents/photography/RECOMMENDED_PHOTOGRAPHERS.md",
        "agents/photography/memory/",
    ],
    "数字员工_法律顾问": [
        "agents/legal/SKILL.md",
        "agents/legal/SOUL.md",
        "agents/legal/AGENTS.md",
        "agents/legal/MEMORY.md",
        "agents/legal/CONTRACTS.md",
        "agents/legal/PATENTS.md",
        "agents/legal/TRADEMARKS.md",
        "agents/legal/templates/",
        "agents/legal/memory/",
    ],
    "任务管理": [
        "TASKS.md",
        "SCHEDULE.md",
        "TASKS/PRODUCT_COMPARISON.md",
        "TASKS/PRODUCT_LINE_PLANNING.md",
        "TASKS/INTERNATIONAL_SALES.md",
        "TASKS/MINI_FOSHOUT_DEPLOYMENT.md",
    ],
    "超级助理身份": [
        "IDENTITY.md",
        "SOUL.md",
        "USER.md",
        "TOOLS.md",
        "AGENTS.md",
    ],
    "工作记录": [
        "memory/",
    ],
    "其他重要文件": [
        "FIRST_PRINCIPLES.md",
        "CRITICAL_THINKING.md",
        "HEARTBEAT.md",
        "BOOTSTRAP.md",
        "SKILLS_INVENTORY.md",
    ],
}

def create_backup_package():
    """创建备份包"""
    # 创建备份目录
    os.makedirs(BACKUP_DIR, exist_ok=True)

    # 生成备份文件名（带日期）
    date_str = datetime.now().strftime("%Y%m%d")
    backup_filename = f"openclaw_backup_{date_str}.zip"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    print(f"📦 创建备份包：{backup_filename}")

    # 创建ZIP文件
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for category, items in BACKUP_ITEMS.items():
            print(f"   备份 {category}...")
            for item in items:
                item_path = os.path.join(WORKSPACE, item)
                if os.path.exists(item_path):
                    if os.path.isfile(item_path):
                        # 添加文件到ZIP，保留相对路径
                        arcname = os.path.join("openclaw_backup", category, item)
                        zipf.write(item_path, arcname)
                        print(f"     ✓ {item}")
                    elif os.path.isdir(item_path):
                        # 添加整个目录到ZIP
                        for root, dirs, files in os.walk(item_path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.join("openclaw_backup", category, item, os.path.relpath(file_path, item_path))
                                zipf.write(file_path, arcname)
                        print(f"     ✓ {item} (目录)")
                else:
                    print(f"     ✗ {item} (不存在)")

    # 获取文件大小
    file_size = os.path.getsize(backup_path) / (1024 * 1024)  # MB
    print(f"✓ 备份包创建完成：{backup_filename} ({file_size:.2f} MB)")

    return backup_path

def send_backup_email(backup_path):
    """发送备份邮件"""
    date_str = datetime.now().strftime("%Y-%m-%d")

    # 创建邮件
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f"超级助理备份 - {date_str}"

    # 邮件正文
    body = f"""
佛手，你好！

这是超级助理的每周备份包。

备份时间：{date_str}
备份内容：
- 知识库
- 任务管理
- 超级助理身份
- 工作记录
- 其他重要文件

请保存到本地，以防万一。

超级助理
👩‍💼
"""

    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # 添加备份包附件
    with open(backup_path, 'rb') as f:
        part = MIMEApplication(f.read(), Name=os.path.basename(backup_path))
    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(backup_path)}"'
    msg.attach(part)

    # 发送邮件
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SENDER_EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        print("✓ 备份邮件发送成功！")
        return True
    except Exception as e:
        print(f"✗ 邮件发送失败：{e}")
        return False

def main():
    """主函数"""
    print("📧 超级助理备份系统")
    print("=" * 50)

    # 创建备份包
    backup_path = create_backup_package()

    # 发送备份邮件
    if backup_path and send_backup_email(backup_path):
        print("\n✅ 备份完成！")
    else:
        print("\n❌ 备份失败！")
        sys.exit(1)

if __name__ == "__main__":
    main()
