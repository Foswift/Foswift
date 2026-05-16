# 超级助理技能清单

> 本文件记录所有可用的技能，供系统恢复参考
> 更新时间：2026-03-29

---

## 技能分类

### 1. 飞书相关技能（openclaw-lark）

| 技能名称 | 路径 | 功能描述 |
|---------|------|---------|
| feishu-bitable | /workspace/projects/extensions/openclaw-lark/skills/feishu-bitable/ | 飞书多维表格创建、查询、编辑和管理 |
| feishu-calendar | /workspace/projects/extensions/openclaw-lark/skills/feishu-calendar/ | 飞书日历与日程管理 |
| feishu-channel-rules | /workspace/projects/extensions/openclaw-lark/skills/feishu-channel-rules/ | 飞书channel输出规则 |
| feishu-create-doc | /workspace/projects/extensions/openclaw-lark/skills/feishu-create-doc/ | 创建飞书云文档 |
| feishu-fetch-doc | /workspace/projects/extensions/openclaw-lark/skills/feishu-fetch-doc/ | 获取飞书云文档内容 |
| feishu-im-read | /workspace/projects/extensions/openclaw-lark/skills/feishu-im-read/ | 飞书IM消息读取 |
| feishu-task | /workspace/projects/extensions/openclaw-lark/skills/feishu-task/ | 飞书任务管理 |
| feishu-troubleshoot | /workspace/projects/extensions/openclaw-lark/skills/feishu-troubleshoot/ | 飞书插件问题排查 |
| feishu-update-doc | /workspace/projects/extensions/openclaw-lark/skills/feishu-update-doc/ | 更新飞书云文档 |

### 2. Coze相关技能（coze-openclaw-plugin）

| 技能名称 | 路径 | 功能描述 |
|---------|------|---------|
| coze-asr | /workspace/projects/extensions/coze-openclaw-plugin/skills/coze-asr/ | 语音转文字（Coze ASR） |
| coze-image-gen | /workspace/projects/extensions/coze-openclaw-plugin/skills/coze-image-gen/ | 文字生成图片（Coze） |
| coze-tts | /workspace/projects/extensions/coze-openclaw-plugin/skills/coze-tts/ | 文字转语音（Coze TTS） |
| openclaw-faq | /workspace/projects/extensions/coze-openclaw-plugin/skills/openclaw-faq/ | OpenClaw/龙虾/扣子常见问题 |

### 3. 工作空间技能（workspace）

| 技能名称 | 路径 | 功能描述 |
|---------|------|---------|
| agent-browser | /workspace/projects/workspace/skills/agent-browser/ | 浏览器自动化 |
| find-skills | /workspace/projects/workspace/skills/find-skills/ | 技能发现/安装 |
| skillhub-preference | /workspace/projects/workspace/skills/skillhub-preference/ | 优先使用skillhub |
| social-media-director | /workspace/projects/workspace/skills/social-media-director/ | 自媒体编导助手 |

### 4. 系统技能（/usr/lib/node_modules/openclaw/skills）

| 技能名称 | 路径 | 功能描述 |
|---------|------|---------|
| healthcheck | /usr/lib/node_modules/openclaw/skills/healthcheck/ | 主机安全加固和风险配置 |
| node-connect | /usr/lib/node_modules/openclaw/skills/node-connect/ | OpenClaw节点连接诊断 |
| skill-creator | /usr/lib/node_modules/openclaw/skills/skill-creator/ | 创建、编辑技能 |
| tmux | /usr/lib/node_modules/openclaw/skills/tmux/ | 远程控制tmux会话 |
| weather | /usr/lib/node_modules/openclaw/skills/weather/ | 获取天气和预报 |

### 5. 其他可用技能（部分列出）

| 技能名称 | 路径 | 功能描述 |
|---------|------|---------|
| github | /usr/lib/node_modules/openclaw/skills/github/ | GitHub操作 |
| discord | /usr/lib/node_modules/openclaw/skills/discord/ | Discord机器人 |
| session-logs | /usr/lib/node_modules/openclaw/skills/session-logs/ | 会话日志查看 |
| apple-reminders | /usr/lib/node_modules/openclaw/skills/apple-reminders/ | 苹果提醒事项 |

---

## 超级助理核心能力

### 内置工具（无需技能）

1. **消息系统**
   - 飞书消息发送/读取
   - 微信消息发送/读取
   - 跨平台消息发送

2. **文件系统**
   - 读取/写入/编辑文件
   - 搜索文件
   - 执行命令

3. **网络能力**
   - 网页搜索
   - 网页内容获取
   - 图片分析
   - PDF分析

4. **会话管理**
   - 创建子会话
   - 发送消息到其他会话
   - 查看会话历史

5. **定时任务**
   - Cron定时任务
   - 心跳检查

6. **日历和任务**
   - 飞书日历管理
   - 飞书任务管理

---

## 数字员工技能

### 老刘（摄影分身）

**路径**：`/workspace/projects/workspace/agents/photography/SKILL.md`

**核心技能**：
- 摄影技术知识
- 布光技巧
- 相机操作
- 镜头知识
- 佛手光技术
- 富士胶片模拟参数
- 实战案例分析

**学习能力**：
- 可以学习新的摄影知识
- 可以分析照片并给出建议
- 可以学习书籍内容

### 法律顾问

**路径**：`/workspace/projects/workspace/agents/legal/SKILL.md`

**核心技能**：
- 专利申请
- 商标保护
- 合同审核
- 知识产权
- 法律文件撰写

---

## 技能恢复指南

### 如果系统需要恢复技能

1. **检查技能是否安装**
   ```bash
   # 列出可用技能
   openclaw skills list
   ```

2. **重新安装技能**
   ```bash
   # 从skillhub安装
   openclaw skills install <skill-name>
   
   # 或从本地安装
   openclaw skills install /path/to/skill
   ```

3. **验证技能**
   ```bash
   # 测试技能是否正常工作
   openclaw skills verify <skill-name>
   ```

---

## 自定义技能位置

用户自定义技能位置：
- `/workspace/projects/workspace/skills/` - 本地技能
- `/workspace/projects/workspace/agents/` - 数字员工技能

---

## 备份说明

本清单记录在：
```
/workspace/projects/workspace/SKILLS_INVENTORY.md
```

包含：
- ✅ 所有可用技能列表
- ✅ 技能路径
- ✅ 技能功能描述
- ✅ 恢复指南
- ✅ 数字员工技能
- ✅ 内置能力

---

**更新时间**：2026-03-29 00:02
**记录人**：超级助理
