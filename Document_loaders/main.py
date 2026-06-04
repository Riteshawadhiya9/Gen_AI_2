from langchain_community.document_loaders import TextLoader


data = TextLoader("Document_loaders/notes.txt")

docs = data.load()

# print(docs)
print(docs[0])