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

使用[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)为后端，[NoneBot2](https://github.com/nonebot/nonebot2)为平台的极其简单的本地中文（汉语） AI chat 插件。

### 环境要求

| 量化等级 | 最低显存 |
| :------: | :------: |
|   FP16   |   13GB   |
|   INT8   |   10GB   |
|   INT4   |   6GB    |

使用 INT4 量化后的[模型](https://huggingface.co/THUDM/chatglm-6b-int4)。需要 4.2 GB 左右的存储空间（模型），NVIDIA 显卡（使用 CUDA）、6G 及以上的显存。现在默认使用 CPU 推理，方便开箱即用，但速度较慢。

> 实际可以低于 Python 3.9（但none-adapter-onebot要求Python 3.8+）。

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

### 下载模型及其配置文件

如果没有设置路径，则会自动下载到用户目录下的`.cache/huggingface/modules/transformers_modules/THUDM/chatglm-6b-int4`。

- 如果是较小显存（< 10 G）且只用聊天对话模型（ChatGLM-6B-INT4）[^1]则没用必要修改。
- 如果使用6B完整模型，则可以自行设置路径。

模型的具体使用，还请关注[原仓库说明](https://github.com/THUDM/ChatGLM-6B)↓提交检测

![GitHub last commit](https://img.shields.io/github/last-commit/THUDM/ChatGLM-6B?style=flat-square)

[^1]: 在其他位置配置量化后的INT4模型，发生一些编译错误，暂时~~懒得~~没有能力解决。

手动下载：

→[清华云盘](https://cloud.tsinghua.edu.cn/d/fb9f16d6dc8f482596c2/)（仅模型文件，是6B完整模型，显存较小需要量化使用，暂未设置，需要自行在`chat.py`文件中修改）

→[🤗 Hugging Face](https://huggingface.co/THUDM/chatglm-6b-int4)（完整文件），约 4.2 GB。


### 安装运行所需依赖

如果使用pip安装，实际已经自动安装了以下依赖，在此说明是为了方便检查

1、模型所需的依赖

```bash
pip install protobuf==3.20.0 transformers==4.26.1 icetk cpm_kernels
```

2、`NoneBot`运行所需依赖

安装这个插件，那必然是已经有了`NoneBot`项目，或者移步去[NoneBot2](https://github.com/nonebot/nonebot2]查看。由于还不会根据项目自动切换适配器，因此需要安装`nonebot-adapter-onebot`，以便调用`Onebotv11`进行通信。

### 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

|    配置项     | 必填 |     类型      |                                     默认值                                      |             说明             |
| :-----------: | :--: | :-----------: | :-----------------------------------------------------------------------------: | :--------------------------: |
|   chat_mode   |  否  |      str      |                                       cpu                                       |    运行模式，cuda 或 cpu     |
| chatglm_model |  否  |      str      | "$User$/.cache/huggingface/modules/transformers_modules/THUDM/chatglm-6b-int4/" | chatglm 模型及其配置文档路径 |
|  chatglm_his  |  否  |      str      |                                "./data/history/"                                |       历史记录保存路径       |
|  chatglm_cmd  |  否  | str/list[str] |                                      "hi"                                       |           对话命令           |

## 使用

### 指令表

| 指令 |  权限  | 需要@ |   范围    |      说明       |
| :--: | :----: | :---: | :-------: | :-------------: |
|  hi  | 所有人 |  否   | 私聊/群聊 | 与 chatglm 对话 |
| 清空记录 | 所有人 | 否 | 私聊/群聊 | 清空自己的对话历史记录 |
| 导出记录 | 所有人 | 否 | 群聊 | 导出记录文件到群中|

## ToDo

- [x] 保存对话记录以实现多轮对话
- [ ] 配置角色功能
- [ ] 图片输出功能
- [ ] 其他中文文本生成模型
  - [ ] 尝试使用`ChatRWKV`

如有其他功能需求，欢迎提issues，当然如果您实现了某些功能或修复了问题，也非常欢迎您提PR。

## 更新说明

- 2023-03-21，更新说明文件，更新插件到0.1.3，默认使用`ChatGLM-6B-INT4`模型、CPU推理，便于开箱即用；修复忘记设置包名导致的无法使用问题。

## 致谢

- [@A-kirami](https://github.com/A-kirami) 项目使用了 README[模板](https://github.com/A-kirami/nonebot-plugin-template)，有修改
- [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)
- [nonebot2](https://github.com/nonebot/nonebot2)
