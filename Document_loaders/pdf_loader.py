from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("Document_loaders/GenAIpart2.pdf")

docs = data.load()

# print(len(docs))

print(docs[63].page_content)
print("============================================")
print(docs[66].page_content)