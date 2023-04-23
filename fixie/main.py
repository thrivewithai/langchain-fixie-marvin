import fixieai

BASE_PROMPT = (
    "I am an agent that answers questions about the State of the Union. "
    "User may have follow-up questions that refers to something mentioned before but I "
    "always do Ask Func[fixie_query_corpus] with a complete question, without any "
    "reference."
)

FEW_SHOTS = """
Q: What did the president say about Ketanji Brown Jackson?
Ask Func[fixie_query_corpus]: What did the president say about Ketanji Brown Jackson?
Func[fixie_query_corpus] says: The president said that Ketanji Brown Jackson is one of the nation's top legal minds, a former top litigator in private practice, a former federal public defender, and from a family of public school educators and police officers. He also said that she is a consensus builder and has received a broad range of support from the Fraternal Order of Police to former judges appointed by Democrats and Republicans.
A: The president said that Ketanji Brown Jackson is one of the nation's top legal minds, a former top litigator in private practice, a former federal public defender, and from a family of public school educators and police officers. He also said that she is a consensus builder and has received a broad range of support from the Fraternal Order of Police to former judges appointed by Democrats and Republicans.
"""

URLS = ["https://raw.githubusercontent.com/hwchase17/langchain/master/docs/modules/state_of_the_union.txt"]
CORPORA = [fixieai.DocumentCorpus(urls=URLS)]
agent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS, CORPORA, conversational=True)