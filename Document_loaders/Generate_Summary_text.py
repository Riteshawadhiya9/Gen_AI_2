from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

data = TextLoader("Document_loaders/notes.txt")
docs = data.load()

template = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "You are an AI that summarizes text."},
    {"role": "human", "content": "{data}"}
])

model = ChatGroq(model = "llama-3.1-8b-instant")

model2 = ChatMistralAI(model = "mistral-small-2506")

prompt = template.format_prompt(data = docs)
prompt = template.format_prompt(data = docs[0].page_content)

print("-------------------GROQ-------------------------------")
result = model.invoke(prompt)
print(result.content)

print("-------------------MISTRAL-------------------------------")
result2 = model2.invoke(prompt)
print(result2.content)