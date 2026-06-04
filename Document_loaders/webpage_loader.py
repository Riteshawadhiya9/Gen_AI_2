from langchain_community.document_loaders import WebBaseLoader

# url = "https://www.riteshawadhiya.me/"
url = "https://github.com/Riteshawadhiya9"

data = WebBaseLoader(url)
docs = data.load()

print(len(docs))
# print(docs[0].page_content)