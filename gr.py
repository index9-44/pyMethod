#!/usr/bin/python
# -*- coding: UTF-8 -*-
import gradio as gr
import openai
import time
# 定义 OpenAI API key
openai.api_key = "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"
# 定义模型 ID
model_engine = "text-davinci-003"
# 定义对话历史记录
conversation_history = []
# 定义聊天函数
def chat(prompt):
    # 获取 OpenAI 的 GPT 模型的响应
    response = openai.Completion.create(
        #输入需要使用的引擎
        engine=model_engine,
        #输入发给openai的内容
        prompt=prompt,
        temperature=0.7,
        #这个模型最大4096个token好像，可以设置大一点
        max_tokens=3400,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices[0].text.strip()
    # 将聊天历史记录添加到会话历史记录中
    conversation_history.append(message)
    # 返回模型的文本响应
    return message
#输出接口
def greet(name):
    response = chat(name)
    time.sleep(1)
    return "ChatGtp：" + response
if __name__ == '__main__':
    iface = gr.Interface(fn=greet, inputs=[
        gr.Textbox(placeholder='请输入您想问chatgtp的问题',
                   label="您想问ChatGtp什么问题？",
                   lines=3),
    ], outputs=[
        gr.Textbox(
            lines=15
        )
    ])
    iface.launch(share=True)