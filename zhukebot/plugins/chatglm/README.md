<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# nonebot-plugin-chatglm

_✨ NoneBot [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) 支持插件 ✨_

![licese](https://img.shields.io/github/license/DaoMingze/zhukebot)
![Python](https://img.shields.io/badge/python-3.9+-blue)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
![PyPI](https://img.shields.io/pypi/v/nonebot_plugin_chatglm)

</div>

## 介绍

使用[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)为后端，[nonebot2](https://github.com/nonebot/nonebot2)为平台的极其简单的本地 AI chat 插件。

### 环境要求

| 量化等级 | 最低显存 |
| :------: | :------: |
|   FP16   |   13GB   |
|   INT8   |   10GB   |
|   INT4   |   6GB    |

已配置 INT4 量化，可自行修改`chat.py`文件调整。

需要 13GiB 左右的存储空间（模型），NVIDIA 显卡（使用 CUDA）、6G 及以上的显存[^1]。

> 实际可以低于 python3.9，但没测试过。

[^1]: CPU 推理也可，但需要 16G 及以上的内存，可自行修改。

## 安装与更新

### 软件环境

#### CUDA

- Windows：见[CUDA 官方文档|英文](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)
- Linux：见[CUDA 官方文档|英文](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

#### PyTorch

见[PyTorch 官方导引](https://pytorch.org/get-started/locally/)

### 插件

<details>
<summary><b>（一）使用 nb-cli 安装与更新</b></summary>

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-chatglm --upgrade
```

</details>

<details>

<summary><b>（二）使用包管理器安装与更新</b></summary>
1、在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令：
<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-chatglm
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-chatglm
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-chatglm
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-chatglm
```

</details>

2、打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

```toml
plugins = ["nonebot_plugin_chatglm"]
```

</details>

## 配置

下载模型及其配置文件，→[清华云盘](https://cloud.tsinghua.edu.cn/d/fb9f16d6dc8f482596c2/)（仅模型文件）、[🤗 Hugging Face](https://huggingface.co/THUDM/chatglm-6b)（完整文件），约 12.8 GiB。

可关注[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)更新![GitHub last commit](https://img.shields.io/github/last-commit/THUDM/ChatGLM-6B?style=flat-square)

安装模型运行所需依赖

```bash
pip install protobuf==3.20.0 transformers==4.26.1 icetk cpm_kernels
```

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

|    配置项    | 必填  |     类型      | 默认值 |             说明             |
| :----------: | :---: | :-----------: | :----: | :--------------------------: |
| chatglm_model |  是   |      str      |   无   | chatglm 模型及其配置文档路径 |
| chatglm_his | 否 | str | "./data/history/" | 历史记录保存路径
| chatglm_cmd  |  否   | str/list[str] |  "hi"  |           对话命令           |

## 使用

### 指令表

| 指令  |  权限  | 需要@ |   范围    |      说明       |
| :---: | :----: | :---: | :-------: | :-------------: |
|  hi   | 所有人 |  否   | 私聊/群聊 | 与 chatglm 对话 |

## ToDo

- [x] 保存对话记录以实现多轮对话
- [ ] 配置角色功能
- [ ] 图片输出功能
- [ ] 其他中文文本生成模型

## 致谢

- [@A-kirami](https://github.com/A-kirami) 项目使用了 README[模板](https://github.com/A-kirami/nonebot-plugin-template)，有修改
- [chatGLM-6B](https://github.com/THUDM/ChatGLM-6B)
- [nonebot2](https://github.com/nonebot/nonebot2)
