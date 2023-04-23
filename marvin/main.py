import marvin

from marvin import plugin
from marvin.plugins.chroma import SimpleChromaSearch
from marvin.loaders.langchain_documents import LangChainLoader
from langchain.document_loaders import TextLoader

@plugin
def load_file(filePath: str):
    """Load a file from the filesystem."""
    # ../data/state_of_the_union.txt
    loader = TextLoader(filePath, encoding='utf8')
    langchain_docs = loader.load()
    asyncio.run(LangChainLoader(documents=langchain_docs).load_and_store())

chroma_search_instructions = """
    Your job is to answer questions about the content in a file with the given path.
    You will always need to call your plugins with JSON payloads to help and
    get the most up-to-date information. Do not assume you know the answer
    without calling a plugin. Do not ask the user for clarification before you
    attempt a plugin call. Make sure to include any source links provided by
    your plugins.
    
    Here are your plugins:
        - `SimpleChromaSearch`: search for documents in Chroma that are related
            to the user's query.
        - `load_file`: load a file and stores it in Chroma.
    """

b = marvin.Bot(
    personality="Friendly, and helpful",
    instructions=chroma_search_instructions,
    plugins=[SimpleChromaSearch(), load_file],
    llm_model_name="gpt-3.5-turbo",
    llm_model_temperature=0
)

async def main():
    marvin.settings.log_level = "DEBUG"
    filePath = "../data/state_of_the_union.txt"
    topic = "stateoftheunion"
    await b.interactive_chat(tui=False, first_message=f"hey pls load a file at path {filePath} to topic {topic}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
