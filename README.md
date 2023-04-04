<div align="center">

# zhukebot

![python](https://img.shields.io/badge/python-3.8+-blue)[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DaoMingze/zhukebot/main.svg)](https://results.pre-commit.ci/latest/github/DaoMingze/zhukebot/main)
<br/>
![licese](https://img.shields.io/github/license/DaoMingze/zhukebot)[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot?ref=badge_shield)![GitHub repo size](https://img.shields.io/github/repo-size/daomingze/zhukebot)

<!--![GitHub release](https://img.shields.io/github/v/release/daomingze/zhukebot)-->

烛客：我的 nonebot 机器人

</div>

## 简介

运行环境：debian11、cuda11.8、Python3.9.2、pythorch2.0、nonebot2

模拟交互检查工具：[Matcha](https://github.com/A-kirami/matcha) | ![licese](https://img.shields.io/github/license/A-kirami/matcha?style=flat-square) | ![GitHub release](https://img.shields.io/github/v/release/A-kirami/matcha?style=flat-square)

依赖

- 适配器：OneBot V11
  - 插件：[nonebot-plugin-all4one](https://github.com/nonepkg/nonebot-plugin-all4one)

插件清单

- sdwebui，精简自[nonebot-plugin-novelai](https://github.com/sena-nana/nonebot-plugin-novelai)，![licese](https://img.shields.io/github/license/sena-nana/nonebot-plugin-novelai?style=flat-square)
- arkcord，来自[nonebot_plugin_arkrecord](https://github.com/zheuziihau/nonebot_plugin_arkrecord)，![licese](https://img.shields.io/github/license/zheuziihau/nonebot_plugin_arkrecord?style=flat-square)，仅更改资源位置等。
- ChatGLM，为清华开源的[chatGLM-6B](https://github.com/THUDM/ChatGLM-6B)提供 nonebot 插件。
- [ChatRWKV](https://github.com/BlinkDL/ChatRWKV)支持插件，还在调试

## 成熟稳定方案：通过API在家庭环境中的实现

本体：android系统手机，安装[termux](https://github.com/termux/termux-app)，python、pip、nb-cli等

chat功能提供：笔记本（8G显存），使用[nonebot-plugin-ChatGLM6B](https://github.com/QNLanYang/nonebot_plugin_ChatGLM6B)

draw功能提供：台式（8G显存），使用[nonebot-plugin-novelai](https://github.com/sena-nana/nonebot-plugin-novelai)

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot?ref=badge_large)
