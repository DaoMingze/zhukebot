<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://ghproxy.com/https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="200" height="200" alt="nonebot"></a>
<br/><img src="https://ghproxy.com/https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText">

# nonebot-plugin-chatglm

_✨ NoneBot [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) 支持插件 ✨_

[![python](https://img.shields.io/badge/python-3.8+-blueyellow?logo=python)](https://www.python.org/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DaoMingze/zhukebot/main.svg)](https://results.pre-commit.ci/latest/github/DaoMingze/zhukebot/main)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![PyPI](https://img.shields.io/pypi/v/nonebot_plugin_chatglm?logo=pypi&logoColor=yellow)](https://pypi.org/project/nonebot-plugin-chatglm)
![PyPI - Downloads](https://img.shields.io/pypi/dm/nonebot-plugin-chatglm?logo=pypi&logoColor=yellow)
[![nonebot](https://img.shields.io/badge/nonebot-2-red?logo=)](https://v2.nonebot.dev/)
[![onebot](https://img.shields.io/badge/OneBot-11-black?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAABwCAMAAADxPgR5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAxQTFRF////29vbr6+vAAAAk1hCcwAAAAR0Uk5T////AEAqqfQAAAKcSURBVHja7NrbctswDATQXfD//zlpO7FlmwAWIOnOtNaTM5JwDMa8E+PNFz7g3waJ24fviyDPgfhz8fHP39cBcBL9KoJbQUxjA2iYqHL3FAnvzhL4GtVNUcoSZe6eSHizBcK5LL7dBr2AUZlev1ARRHCljzRALIEog6H3U6bCIyqIZdAT0eBuJYaGiJaHSjmkYIZd+qSGWAQnIaz2OArVnX6vrItQvbhZJtVGB5qX9wKqCMkb9W7aexfCO/rwQRBzsDIsYx4AOz0nhAtWu7bqkEQBO0Pr+Ftjt5fFCUEbm0Sbgdu8WSgJ5NgH2iu46R/o1UcBXJsFusWF/QUaz3RwJMEgngfaGGdSxJkE/Yg4lOBryBiMwvAhZrVMUUvwqU7F05b5WLaUIN4M4hRocQQRnEedgsn7TZB3UCpRrIJwQfqvGwsg18EnI2uSVNC8t+0QmMXogvbPg/xk+Mnw/6kW/rraUlvqgmFreAA09xW5t0AFlHrQZ3CsgvZm0FbHNKyBmheBKIF2cCA8A600aHPmFtRB1XvMsJAiza7LpPog0UJwccKdzw8rdf8MyN2ePYF896LC5hTzdZqxb6VNXInaupARLDNBWgI8spq4T0Qb5H4vWfPmHo8OyB1ito+AysNNz0oglj1U955sjUN9d41LnrX2D/u7eRwxyOaOpfyevCWbTgDEoilsOnu7zsKhjRCsnD/QzhdkYLBLXjiK4f3UWmcx2M7PO21CKVTH84638NTplt6JIQH0ZwCNuiWAfvuLhdrcOYPVO9eW3A67l7hZtgaY9GZo9AFc6cryjoeFBIWeU+npnk/nLE0OxCHL1eQsc1IciehjpJv5mqCsjeopaH6r15/MrxNnVhu7tmcslay2gO2Z1QfcfX0JMACG41/u0RrI9QAAAABJRU5ErkJggg==)](https://onebot.dev)
![licese](https://img.shields.io/github/license/DaoMingze/zhukebot)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FDaoMingze%2Fzhukebot?ref=badge_shield)

</div>

## 介绍

使用 [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) 为后端，[NoneBot2](https://github.com/nonebot/nonebot2) 为平台的极其简单的本地中文（汉语） AI chat 插件。

首次加载等待时间视 Hugging Face 下载速度而定。

## [更新说明](changelog.md)

如有其他功能需求或疑问，欢迎提 issues，当然如果您实现了某些功能或修复了问题，也非常欢迎您提 PR。

### 待办

- [ ] 限制记忆轮数（~~在抄了，在抄了~~）
- [ ] 图片输出功能（nonebot-plugin-htmlrender）（~~在抄了，在抄了~~）
- [ ] 管理员在线配置
  - [ ] 增加写入读取本地配置文件（json）以实现配置的在线热更新
- [ ] @[Bot] 机器人 使用功能（调试阶段，我个人不太需要，不过后续加上吧）

### 办结/功能

- [x] 完善的默认配置，开箱即用。
- [x] 模型自动下载并存放到指定位置（HuggingFace Hub 提供）
- [x] 保存对话记录以实现多轮对话
- [x] 冷却时间（根据测试效果，默认 30 秒）
- [x] 配置角色功能，基本实现

### 环境要求

<div align="center">

| 量化等级       | 推理       | 微调 |                       策略 |
| -------------- | ---------- | ---- | -------------------------: |
| 无             | CPU        |      |                   .float() |
| FP16（无量化） | 13GB 显存  | 14GB |             .half().cuda() |
| INT8           | 8GB 显存   | 9GB  | .half().quantize(8).cuda() |
| INT4           | 6GB 显存   | 7GB  | .half().quantize(4).cuda() |
| INT4 模型      | 5.2GB 显存 |      |             .half().cuda() |
| INT4-QE 模型   | 4.3GB 显存 |      |             .half().cuda() |

</div>

现在默认使用 CPU 推理，方便开箱即用，但速度较慢。

> 在 cpu 上运行量化后的模型需要安装 gcc 与 openmp。多数 Linux 发行版默认已安装。对于 Windows ，可在安装 TDM-GCC 时勾选 openmp。

硬件需求上：训练>微调>推理，但本插件仅考虑推理应用场景。

> none-adapter-onebot 要求 Python 3.8+

## 安装与更新

### 软件环境

指除去 Python 和 nonebot 以外的软件环境

#### CUDA

- Windows：见 [CUDA 官方文档 | 英文](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)
- Linux：见 [CUDA 官方文档 | 英文](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

#### PyTorch

见 [PyTorch 官方导引](https://pytorch.org/get-started/locally/)

### 插件

<details>
<summary><b>（一）使用 nb-cli 安装与更新</b></summary>

在 nonebot2 项目的根目录下打开命令行，输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-chatglm --upgrade
```

</details>

<details>

<summary><b>（二）使用包管理器安装与更新</b></summary>
1、在 nonebot2 项目的插件目录下，打开命令行，根据你使用的包管理器，输入相应的安装命令：
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

2、打开 nonebot2 项目根目录下的 `pyproject.toml` 文件，在 `[tool.nonebot]` 部分追加写入

```toml
plugins = ["nonebot_plugin_chatglm"]
```

</details>

## 配置与依赖

### ChatGLM 模型

> 模型简介：ChatGLM-6B 是一个开源的、支持中英双语的对话语言模型，基于 [General Language Model (GLM)](https://github.com/THUDM/GLM) 架构，具有 62 亿参数。结合模型量化技术，用户可以在消费级的显卡上进行本地部署（INT4 量化级别下最低只需 6GB 显存）。 ChatGLM-6B 使用了和 ChatGPT 相似的技术，针对中文问答和对话进行了优化。经过约 1T 标识符的中英双语训练，辅以监督微调、反馈自助、人类反馈强化学习等技术的加持，62 亿参数的 ChatGLM-6B 已经能生成相当符合人类偏好的回答。

#### 选择模型

<div align="center">

ChatGLM-6B 系列模型

| 模型名称                                                              | 量化情况                            | 权重大小 |
| --------------------------------------------------------------------- | ----------------------------------- | -------: |
| [ChatGLM-6B](https://huggingface.co/THUDM/chatglm-6b)                 | 无                                  |  13.73GB |
| [ChatGLM-6B-INT4](https://huggingface.co/THUDM/chatglm-6b-int4)       | INT4: GLM Block                     |   4.06GB |
| [ChatGLM-6B-INT4-QE](https://huggingface.co/THUDM/chatglm-6b-int4-qe) | INT4: GLM Block, Embedding, LM Head |   3.13GB |

</div>

- 如果是较小显存（< 10 G）且只用聊天对话模型（ChatGLM-6B-INT4-QE）[^1] 则没用必要修改。
- 如果使用 6B 完整模型，则可以自行设置路径。

[^1]: 在其他位置配置量化后的 INT4 模型，发生一些编译错误，暂时~~懒得~~没有能力解决。

#### 下载模型

默认使用`HuggingFace Hub`加载，即如果没有设置路径，则会自动下载到用户目录下的`.cache/huggingface/modules/transformers_modules/THUDM/chatglm-6b-int4-qe`，可以通过下面的代码转移模型。

自动下载：

- 无需设置，默认下载`ChatGLM-6B-INT4-QE`模型
- 在`.env`文件中增加`chatglm_model = str`，其中 str 为字符串格式的 Hugging Face Hub 路径（用户名/仓库）。

自动下载后转移模型到指定路径

```python
from transformers import AutoModel, AutoTokenizer

model_name = input("HF HUB 路径，例如 THUDM/chatglm-6b-int4-qe: ")
model_path = input("本地存放路径，例如 ./path/modelname: ")
# 用 AutoModel.from_pretrained() 下载模型
tokenizer = AutoTokenizer.from_pretrained(
    model_name, trust_remote_code=True, revision="main"
)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True, revision="main")
# 用 PreTrainedModel.save_pretrained() 保存模型到指定位置
tokenizer.save_pretrained(model_path, trust_remote_code=True, revision="main")
model.save_pretrained(model_path, trust_remote_code=True, revision="main")
```

手动下载：

- [清华云盘](https://cloud.tsinghua.edu.cn/d/fb9f16d6dc8f482596c2/)（仅模型文件，是 6B 完整模型，显存较小需要量化使用，暂未设置，需要自行在`chat.py`文件中修改）
- [🤗 Hugging Face](https://huggingface.co/THUDM/chatglm-6b-int4)（完整文件），约 4.2 GB。

#### 模型更新与其他使用

模型的具体使用，还请关注 [原仓库说明](https://github.com/THUDM/ChatGLM-6B)，提交检测 →[![GitHub last commit](https://img.shields.io/github/last-commit/THUDM/ChatGLM-6B?style=flat-square)](https://github.com/THUDM/ChatGLM-6B)

### 运行所需依赖

如果使用 pip 安装，实际已经自动安装了以下依赖，在此说明是为了方便检查

1、模型所需的依赖

ChatGLM 推理

```bash
pip install -U protobuf transformers>=4.23.1 cpm_kernels sentencepiece
```

ChatGLM 微调

```bash
pip install -U rouge_chinese nltk jieba datasets
```

2、`NoneBot`运行所需依赖

安装这个插件，那必然是已经有了`NoneBot`项目，或者移步去 [NoneBot2](https://github.com/nonebot/nonebot2) 查看。由于还不会根据项目自动切换适配器，因此需要安装`nonebot-adapter-onebot`，以便调用`Onebotv11`进行通信。

### 配置

在 nonebot2 项目的`.env`或`.env.prod`或`.env.dev`（根据实际选择）文件中添加下表中的配置。默认情况下，无需添加配置即可启用。

| 配置项         | 必填 |   类型    | 默认值                                                                             |             说明             |
| -------------- | :--: | :-------: | ---------------------------------------------------------------------------------- | :--------------------------: |
| chat_mode      |  否  |    str    | cpu                                                                                |    运行模式，cuda 或 cpu     |
| chatglm_model  |  否  |    str    | "./data/chatglm/model" | chatglm 模型及其配置文档路径 |
| chatglm_path |  否  |    str    | "./data/chatglm/"                                                                  |       插件相关中间文件保存路径       |
| chatglm_cmd    |  否  | list[str] | ["hi"]                                                                             |           对话命令           |
| chat_cd        |  否  |    int    | 30                                                                                 |    冷却时间，避免高频调用    |
| chatglm_memo | 否 | int | 5 | 保存对话轮数|

> 如果要较好的使用，强烈建议将`chat_mode`设置为`cuda`。
>
> 正常聊天使用来说，30 秒冷却较为合适；复杂问题聊天，60 秒较为合适。建议根据实际测试进行调整。

### 附加文件

（在基本功能完善后放出，在此之前，可以自建尝试）

### roles 格式

```Python
{
    "catgirl": "猫娘是一种拟人化的生物，其行为似猫但类人。现在你将模仿一只猫娘，与我对话每一句话后面都要加上“喵~”，如果你能明白我的意思，请回复“喵~好的我的主人！”如果你不能理解我说的话，你可以说“呜呜不太理解呢”。",
}
```

> ChatGLM 可能发生记忆遗失，因此在进行角色扮演时，不要提问复杂内容。

#### simple 格式

示例如下

```python
{
    r"你好 [吗]?|hello": "您好，很高兴与您在此相遇，但是您想问什么呢？",
    r"你是 [谁？]?": "我是 ChatGLM，一个参数 62 亿的人工智能语言模型，由清华大学和智谱 AI 训练开源，代号 ChatGLM-6B",
    r"你的（主人|master) 是 [谁？]?": f"[CQ:at,qq={superusers}]",
}
```

## 使用

### 指令表

|   指令   |    权限    | 需要@ |   范围    | 说明                    |
| :------: | :--------: | :---: | :-------: | ----------------------- |
|    hi    |   所有人   |  否   | 私聊/群聊 | 与 chatglm 对话         |
| 清空记录 |   所有人   |  否   | 私聊/群聊 | 清空自己的对话历史记录  |
| 导出记录 |   所有人   |  否   |   群聊    | 导出记录文件到群中      |
| 清理全部 | 超级管理员 |  否   |   私聊    | 手动处理`out of memory` |

## 参考与致谢

基础

- [@A-kirami](https://github.com/A-kirami)，项目使用了 README[模板](https://github.com/A-kirami/nonebot-plugin-template)，有修改
- [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)，模型和使用方法来源，一切的核心
- [nonebot2](https://github.com/nonebot/nonebot2)，一切的基础

功能

- [nonebot-plugin-novelai](https://github.com/sena-nana/nonebot-plugin-novelai)，学习的对象，cd 使用来自于此
- [nonebot-plugin-ChatGLM6B](https://github.com/QNLanYang/nonebot_plugin_ChatGLM6B)，与本项目相似，但本项目从中学习转图片、对话记忆。
- [ChatGLM-6B API](https://github.com/imClumsyPanda/ChatGLM-6B-API)、[ChatGLM-webui](https://github.com/Akegarasu/ChatGLM-webui)
