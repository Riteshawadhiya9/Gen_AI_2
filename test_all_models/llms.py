from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

model2 = ChatGroq(model = "llama-3.1-8b-instant")

model3 = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

print("-------------------GEMINI-------------------------------")

res = model.invoke("what is pydantic explain in simple way?for interview")
print("Gemini :", res.content)

print("--------------------GROQ------------------------------")

res2 = model2.invoke("what is pydantic explain in simple and short with real-life example?Interview Ready answer")
print("Groq  :", res2.content)

print("-------------------MISTRALAI-------------------------------")

res3 = model3.invoke("hello..!!")
print("Mistral :", res3.content)