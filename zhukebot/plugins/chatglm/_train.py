from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "THUDM/chatglm-6b-int4", trust_remote_code=True
)
model = (
    AutoModelForSeq2SeqLM.from_pretrained(
        "THUDM/chatglm-6b-int4", trust_remote_code=True
    )
    .half()
    .cuda()
)
# model = model.eval()

inputs = tokenizer(
    "凯旋门位于意大利米兰市古城堡旁。1807年为纪念[MASK]而建，门高25米，顶上矗立两武士青铜古兵车铸像。",
    return_tensors="pt",
)
inputs = tokenizer.build_inputs_for_generation(inputs, max_gen_length=512)

inputs = {key: value.cuda() for key, value in inputs.items()}

outputs = model.generate(**inputs, max_length=512, eos_token_id=tokenizer.eop_token_id)

print(tokenizer.decode(outputs[0].tolist()))


# Inference
inputs = tokenizer(
    "Ng is an adjunct professor at [MASK] (formerly associate professor and Director of its Stanford AI Lab or SAIL ). Also a pioneer in online education, Ng co-founded Coursera and deeplearning.ai.",
    return_tensors="pt",
)
inputs = tokenizer.build_inputs_for_generation(inputs, max_gen_length=512)
inputs = inputs.to("cuda")
outputs = model.generate(**inputs, max_length=512, eos_token_id=tokenizer.eop_token_id)
print(tokenizer.decode(outputs[0].tolist()))

# Training
inputs = tokenizer(
    [
        "Tsinghua University is located in [MASK].",
        "One minus one equals zero, is it correct? Answer: [MASK]",
    ],
    return_tensors="pt",
    padding=True,
)
inputs = tokenizer.build_inputs_for_generation(
    inputs, targets=["Beijing", "No"], max_gen_length=8, padding=False
)
inputs = inputs.to("cuda")
outputs = model(**inputs)
loss = outputs.loss
logits = outputs.logits

# classification
inputs = tokenizer(
    [
        "Tsinghua University is located in [MASK].",
        "One minus one equals zero, is it correct? Answer: [MASK]",
    ],
    return_tensors="pt",
    padding=True,
)
choices = [["Beijing", "Shanghai"], ["Yes", "No"]]
inputs = tokenizer.build_inputs_for_multiple_choice(inputs, choices)
inputs = inputs.to("cuda")
outputs = model(**inputs)
logits = outputs.logits

"""
We use three different mask tokens for different tasks: [MASK] for short blank filling, [sMASK] for sentence filling, and [gMASK] for left to right generation. You can find examples about different masks from here.
对于不同的任务，我们使用三种不同的掩码令牌： [MASK] 用于短空格填充， [sMASK] 用于句子填充， [gMASK] 用于从左向右生成。您可以在这里找到不同遮罩的示例。
"""
