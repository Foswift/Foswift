#!/bin/bash
# 设置每周自动备份脚本

echo "📧 设置每周自动备份..."
echo "================================"

# 创建cron任务
CRON_JOB="0 9 * * 0 cd /workspace/projects/workspace && python3 /workspace/projects/workspace/scripts/backup_email.py >> /tmp/backup.log 2>&1"

# 检查是否已存在
if crontab -l 2>/dev/null | grep -q "backup_email.py"; then
    echo "⚠ 备份任务已存在，跳过添加"
else
    # 添加到crontab
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "✅ 每周自动备份已设置"
    echo "   时间：每周日 9:00"
fi

# 显示当前crontab
echo ""
echo "当前定时任务："
crontab -l | grep "backup_email.py" || echo "未找到备份任务"
