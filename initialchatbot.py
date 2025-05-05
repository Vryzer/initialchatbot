from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

class AIChatBot:

    def __init__(self, prompt: str):
        print(os.environ.get("APIKEY"))
        self.model = 'gpt-3.5-turbo'
        self.client = OpenAI(api_key=os.environ.get("APIKEY"))
        self.messages = [{"role": "system", "content": prompt}]

    def reply(self, message: str) -> str:
        self.messages.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        response = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response})
        return response

class MirrorChatBot:
    @staticmethod
    def reply(message: str) -> str:
        return message

class DummyChatBot:
    @staticmethod
    def reply(message: str) -> str:
        return 'Hi'

if __name__ == '__main__':

    #bot = DummyChatBot()
    #bot = MirrorChatBot()
    bot = AIChatBot(prompt="You are a helpful assistant") #para esse prompt fique livre pra definir oq quiser pra atribuir um "carater" ao chatbot
    while True:

        message = input("You:")
        if message == "bye":
            print("ChatBot: Goodbye!")
            break
        else:
            print("Chatbot: " + bot.reply(message=message))