from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
import os

load_dotenv()

print(os.getenv("MISTRAL_API_KEY"))

model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

res = model.invoke("hello..!!")
print(res.content)