<div align="center">

# zhukebot

![Python Version](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/DaoMingze/zhukebot/refs/heads/main/assets/badge/python.json)
[![PDM-managed](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/DaoMingze/zhukebot/refs/heads/main/assets/badge/pdm.json)](https://pdm.fming.dev)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/DaoMingze/zhukebot/refs/heads/main/assets/badge/ruff_v2.json)](https://github.com/astral-sh/ruff)

[![Code Style](https://img.shields.io/badge/code%20style-black-black?logo=python&logoColor=edb641)](https://github.com/psf/black)
![Pyright](https://img.shields.io/badge/types-pyright-797952?logo=python&logoColor=edb641)

![licese](https://img.shields.io/github/license/DaoMingze/zhukebot?logo=scales)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DaoMingze/zhukebot/main.svg)](https://results.pre-commit.ci/latest/github/DaoMingze/zhukebot/main)
[![Ruff](https://github.com/DaoMingze/zhukebot/actions/workflows/ruff.yml/badge.svg?branch=main&event=push)](https://github.com/DaoMingze/zhukebot/actions/workflows/ruff.yml)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot?ref=badge_shield)
![GitHub repo size](https://img.shields.io/github/repo-size/daomingze/zhukebot)

![document style](https://img.shields.io/badge/doc%20style-pangu-white)

烛客：我的社交媒体机器人

</div>

## 简介

- python技术栈：[nonebot](https://nonebot.dev)
- JavaScript技术栈：[koishi](https://koishi.chat)

### Nonebot

[![NoneBot Version](https://img.shields.io/badge/nonebot-2+-red.svg)](https://nonebot.dev/)
![GitHub release](https://img.shields.io/github/v/release/daomingze/zhukebot)

#### 运行环境

- OS：[Debian Stable(12 "bookwarm")](https://wiki.debian.org/DebianStable)，with Python3(3.11.2)
- APT INSTALLED：nvidia-driver 525.105.17.1、nvidia-cuda-toolkit 11.8
- PIP INSTALLED：PyTorch 2.0、nb-cli

> 由于 `fastapi需要` [`watchfiles`](https://pypi.org/project/watchfiles) 而该模块暂不兼容 Python3.11，因此 nb-cli 实际运行的环境是 Python3.8-3.10，或是需要 Rust 编译。

#### 开发工具

- 包管理器：PDM、UV
- 编程检查：ruff（black、flake8）、pyright、pylint
- 编辑环境：VS Code

#### 工作环境

- 应用场景：QQ
- 协议：onebot
- 协议前端：NTQQ+签名服务器
- 服务后端：nonebot

#### 插件清单

- [X] SDwebui，精简自 [nonebot-plugin-novelai](https://github.com/sena-nana/nonebot-plugin-novelai)，![licese](https://img.shields.io/github/license/sena-nana/nonebot-plugin-novelai?style=flat-square)
- [X] ChatGLM，为清华开源的 [chatGLM-6B](https://github.com/THUDM/ChatGLM-6B) 提供 nonebot 插件。
- [ ] [ChatRWKV](https://github.com/BlinkDL/ChatRWKV) 支持插件，还在调试
- [ ] 缝合[nonebot-plugin-hitokoto](https://github.com/A-kirami/nonebot-plugin-hitokoto)和[nonebot-plugin-everyday-en](https://github.com/MelodyYuuka/nonebot_plugin_everyday_en)

### 基于 Termux 的方案

<details>

<summary>通过 API 分离 AIGC，减轻机器人服务器压力</summary>

### 安装

本体：android 系统手机，安装 [termux](https://github.com/termux/termux-app)，python、pip、nb-cli 等

1. 在 Android 手机上，从 [termux](https://github.com/termux/termux-app) 下载安装`termux`APP。
2. 打开`termux`APP，使用`termux-change-repo`进入图形化界面更换软件源（空格是选择，Enter 是确认），中国国内建议用清华源（北外源）、南大源、中科大源等。
3. 更新`termux`的软件源（更换后一般会自动更新），然后用`apt upgrade`命令升级（也可以用`apt list --upgradable`查看可升级列表），其中需要确认配置的，一律选择缺省设置（defualt，即输入`n`）。
4. 进入 Debian stable 环境
   1. 安装发行版工具：`apt install proot-distro`
   2. 安装`Debian`，`proot-distro install debian`
   3. 登录`Debian`，`proot-distro login debian`
   4. 更新 debian apt 源，可参考清华开源镜像的 [说明](https://mirrors.tuna.tsinghua.edu.cn/help/debian/)
5. 安装 Python 环境
   1. python、pip、等。输入`apt install python3 python3-pip -y`
   2. 更换 pip 源，中国国内建议用清华源（北外源）、南大源、中科大源等，`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`，并升级`pip install -U pip setuptools wheel`。
   3. 用 pip 安装 pipx 工具，`python3 -m pip install --user pipx`和`python3 -m pipx ensurepath`
6. 安装`nb-cli`，`pipx install nb-cli`
7. 初始化 nonebot 环境，`nb init`。之后的可参考 [nonebot 官方文档](https://v2.nonebot.dev/docs)

常见错误及解决

- 定时插件报错，时区设置问题：修改时区 date，tzselect，export TZ="Asia/Shanghai"

用以下代码检查时区是否正确

```Python
from tzlocal import get_localzone
get_localzone()
```

## 插件

### 核心功能插件

适配器

服务器状态：[nonebot-plugin-status](https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status)，[![pypi package](https://img.shields.io/pypi/v/nonebot-plugin-status?style=social)](https://pypi.org/project/nonebot-plugin-status)

撤回

定时任务：[nonebot-plugin-apscheduler](https://github.com/nonebot/plugin-apscheduler)，[![pypi package](https://img.shields.io/pypi/v/nonebot-plugin-apscheduler?style=social)](https://pypi.org/project/nonebot-plugin-apscheduler)

### AIGC 功能插件

Chat 功能提供：笔记本（8G 显存），使用 [nonebot-plugin-ChatGLM6B](https://github.com/QNLanYang/nonebot_plugin_ChatGLM6B)

Draw 功能提供：台式（8G 显存），使用 [nonebot-plugin-novelai](https://github.com/sena-nana/nonebot-plugin-novelai)

</details>

## License

<center>

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot?ref=badge_large)

[![zhukebot Star History Chart](https://api.star-history.com/svg?repos=DaoMingze/zhukebot&type=Date)](https://star-history.com/#star-history/star-history&Date)

</center>
