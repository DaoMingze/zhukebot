# 更新日志

## 2023年

### 0.1.X

#### 2023-03-26

- 规范开源许可证，去除部分依赖。

#### 2023-03-25

- 根据修改更新配置表。
- 引入[ChatGLM-6B API](https://github.com/imClumsyPanda/ChatGLM-6B-API)、[ChatGLM-webui](https://github.com/Akegarasu/ChatGLM-webui)的`torch_gc()`函数，解决单纯的使用`torch.cuda.empty_cache()`效用不强的问题。
- 优化`config.py`文件将多重判断改为配置类（`class Config(BaseSettings)`）（~~自己的手动判断笑死人了~~）。
- 优化`chat.py`减轻模型运行负担，对特定问题进行字典Q&A回复（~~我讨厌复读机占用资源~~）。可以以此加载一些专业词典或免责声明，实际上是fakeAI（假冒AI），最好不要用。
- 引入[nonebot-plugin-htmlrender](https://github.com/kexue-z/nonebot-plugin-htmlrender)提供的`md_to_pic`功能，并增加[nonebot-plugin-htmlrender](https://github.com/kexue-z/nonebot-plugin-htmlrender)依赖。

<details>

<summary>历史记录</summary>

#### 2023-03-24

- 更新说明文件
- 分离/移除`ChatRWKV`至[chatrwkv](../chatrwkv/)，循名责实。

#### 2023-03-22

- **更新插件到 0.1.4。**
- 更新说明文件。
- 加入`ChatRWKV`生成中文小说文本，在配置使用`chatglm_mode="rwkv"`，并需修改模型路径（默认使用 cuda fp16 策略，如需修改，请自行更改`minirwkv.py`文件）

#### 2023-03-21

- **更新插件到 0.1.3。**
- 更新说明文件。
- 默认使用`ChatGLM-6B-INT4`模型、CPU 推理，便于开箱即用。
- 修复忘记设置包名导致的无法使用问题。

</details>
