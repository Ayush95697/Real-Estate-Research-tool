from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

#load_dotenv()
load_dotenv(dotenv_path=Path(__file__).parent / '.env', override=True)
# needed to call grok in environment

# Constants
EMBEDDINGS_MODEL = "Alibaba-NLP/gte-base-en-v1.5"
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
# Here it will save our data as vector database
COLLECTION_NAME = "real_estate"

llm = None
vector_store = None


# This is to stop keep initilizing llm everytime this fun is called
def initialize_components():
    global llm
    global vector_store
    if llm is None:
        llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.9, max_tokens=1000)
    # To create the embeddings
    if vector_store is None:
        ef = HuggingFaceEmbeddings(
            model_name=EMBEDDINGS_MODEL,
            model_kwargs={"trust_remote_code": True}
        )
        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=str(VECTORSTORE_DIR),
            embedding_function=ef,
        )


def process_urls(urls):

    # This is for streamlit ui to show this process as progress bar
    yield "Initializing Components..."
    initialize_components()

    yield "Resetting vectors database..."
    vector_store.reset_collection()

    # Use headers to improve fetching reliability
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    yield "Fetching URLs..."
    loader = UnstructuredURLLoader(urls=urls, headers=headers)

    data = loader.load()

    # Use 'separators' instead of 'separator'

    yield "Splitting texts into chunks..."
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=1000
    )

    docs = text_splitter.split_documents(data)

    # Check if the list of documents is empty before proceeding
    if not docs:
        print("Warning: No documents were created from the provided URL. Skipping upsert.")
        return  # Exit the function to prevent the ValueError


    yield "Adding chunks..."
    vvids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(docs, ids=vvids)

    yield "Done adding docs to vector database..."

def generate_answers(query):
    if not vector_store:
        raise Exception("No vector store")
    chain=RetrievalQAWithSourcesChain.from_llm(llm=llm,retriever=vector_store.as_retriever())
    results=chain.invoke({"question": query})
    answers = results.get("answer", "")  # Use get() for safety
    sources = results.get("source_documents", "")
    return answers, sources


if __name__ == "__main__":
    urls = ["https://books.toscrape.com/"]
    process_urls(urls)
