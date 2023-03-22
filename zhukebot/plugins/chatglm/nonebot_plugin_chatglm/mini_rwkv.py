########################################################################################################
# The RWKV Language Model - https://github.com/BlinkDL/RWKV-LM
########################################################################################################
from nonebot.plugin import on_command
import os, sys, torch
import numpy as np
from nonebot.adapters.onebot.v11 import (Bot, Event, GroupMessageEvent,
                                         Message, PrivateMessageEvent)
from nonebot.log import logger
from nonebot.params import CommandArg
from prompt_toolkit import prompt
from .config import *
np.set_printoptions(precision=4, suppress=True, linewidth=200)

import torch
torch.backends.cudnn.benchmark = True
torch.backends.cudnn.allow_tf32 = True
torch.backends.cuda.matmul.allow_tf32 = True

# Tune these below (test True/False for all of them) to find the fastest setting:
torch._C._jit_set_profiling_executor(True)
torch._C._jit_set_profiling_mode(True)
torch._C._jit_override_can_fuse_on_cpu(True)
torch._C._jit_override_can_fuse_on_gpu(True)
torch._C._jit_set_texpr_fuser_enabled(False)
torch._C._jit_set_nvfuser_enabled(False)
# set these before import RWKV
os.environ['RWKV_JIT_ON'] = '1'
os.environ["RWKV_CUDA_ON"] = '1' # '1' to compile CUDA kernel (10x faster), requires c++ compiler & cuda libraries

from rwkv.model import RWKV # pip install rwkv
model = RWKV(model=model_path, strategy='cuda fp16')

# out, state = model.forward([187], None)
# print(out.detach().cpu().numpy())

from rwkv.utils import PIPELINE, PIPELINE_ARGS
pipeline = PIPELINE(model, "/home/wdz/aigc/zhukebot/zhukebot/plugins/chatglm/20B_tokenizer.json")

# For alpha_frequency and alpha_presence, see "Frequency and presence penalties":
# https://platform.openai.com/docs/api-reference/parameter-details

args = PIPELINE_ARGS(temperature = 1.0, top_p = 0.7, top_k=0, # top_k = 0 then ignore
                     alpha_frequency = 0.25,
                     alpha_presence = 0.25,
                     token_ban = [0], # ban the generation of some tokens
                     token_stop = [], # stop generation whenever you see any token here
                     chunk_len = 256) # split input into chunks to save VRAM (shorter -> slower)

########################################################################################################
# 1. set os.environ["RWKV_CUDA_ON"] = '1' if possible, for faster preprocess of a long ctx.
# 2. Reuse the state (use deepcopy to clone it) when you are running the same ctx multiple times. 

RWKV_chat = on_command("R", priority=8)
@RWKV_chat.handle()
async def txtgen(bot: Bot, event: Event, message: Message = CommandArg()):
    qq_id = event.get_user_id()
    msg = Message(f"[CQ:at,qq={qq_id}]生成失败")
    ctx = message.extract_plain_text().strip()
    context = pipeline.generate(ctx, token_count=400, args=args)
    msg = Message(f"[CQ:at,qq={qq_id}]{ctx}{context}")
    await RWKV_chat.finish(msg)