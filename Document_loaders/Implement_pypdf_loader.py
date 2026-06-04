from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

data = PyPDFLoader("Document_loaders/GenAIpart2.pdf")
docs = data.load()

template = ChatPromptTemplate.from_messages([
    {"role": "system", "content": "You are an AI that summarizes text."},
    {"role": "human", "content": "{data}"}
])

model = ChatGroq(model = "llama-3.1-8b-instant")

model2 = ChatMistralAI(model = "mistral-small-2506")

prompt = template.format_prompt(data = docs[27].page_content)
# prompt = template.format_prompt(data = docs) # this will give error because of context window limit of the model. I am giveing whole pdf which is more that that model can handle. So I am giving only one page content to the model to summarize.

print("-------------------GROQ-------------------------------")
result = model.invoke(prompt)
print(result.content)

print("-------------------MISTRAL-------------------------------")
result2 = model2.invoke(prompt)
print(result2.content)