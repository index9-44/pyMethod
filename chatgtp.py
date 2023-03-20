import openai
import time

# 定义 OpenAI API key
openai.api_key = "请输入你自己的key"
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


# 测试聊天函数
while True:
    # 获取用户输入的信息
    user_input = input("请输入问题: ")

    # 结束对话的条件
    if user_input.lower() == "exit":
        break

    # 聊天并打印模型的响应
    response = chat(user_input)
    print("ChatGPT: " + response)
    time.sleep(1)
