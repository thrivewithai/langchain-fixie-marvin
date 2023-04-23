from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader

loader = TextLoader('../data/state_of_the_union.txt', encoding='utf8')
index = VectorstoreIndexCreator().from_loaders([loader])

response = index.query("What did the president say about Ketanji Brown Jackson")
print(response)