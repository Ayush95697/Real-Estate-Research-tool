# 📊 Real Estate Research Tool  

A **Retrieval-Augmented Generation (RAG) powered research assistant** that lets you fetch content from websites, store them in a vector database, and ask natural language questions with **answers + sources**.  

Built with **Streamlit, LangChain, ChromaDB, HuggingFace embeddings, and Groq LLMs**.  

---

## 📌 Features  

- ✅ Enter multiple URLs and process them into a vector database  
- ✅ Ask natural language questions related to those websites  
- ✅ Get summarized answers with proper **citations/sources**  
- ✅ Streamlit UI for easy interaction  
- ✅ Uses **HuggingFace Embeddings** + **Chroma Vector DB** + **Groq LLM**  

---

## 🛠️ Tech Stack  

- **Frontend/UI** → Streamlit  
- **LLM** → Groq `openai/gpt-oss-20b`  
- **Embeddings** → HuggingFace `Alibaba-NLP/gte-base-en-v1.5`  
- **Vector DB** → ChromaDB  
- **Framework** → LangChain  
- **Data Loading** → UnstructuredURLLoader  

---

## 🔄 Project Workflow  

The application follows a **Retrieval-Augmented Generation (RAG)** pipeline:  

1. **Input URLs** → User enters one or more research URLs in the Streamlit app.  
2. **Document Loading** → Content is fetched from the given websites using `UnstructuredURLLoader`.  
3. **Text Splitting** → Large documents are broken down into smaller, meaningful **chunks** with `RecursiveCharacterTextSplitter`.  
4. **Embedding Generation** → Each chunk is converted into vector embeddings using HuggingFace’s `gte-base-en-v1.5` model.  
5. **Vector Database Storage** → Chunks + embeddings are stored in **ChromaDB** for efficient semantic search.  
6. **Query Handling** → User submits a natural language question.  
7. **Retriever** → Relevant chunks are retrieved from the vector database.  
8. **LLM Reasoning** → Groq’s `gpt-oss-20b` processes the retrieved context and generates an answer.  
9. **Final Output** → Answer is displayed along with **source citations** in the Streamlit app.  

---

### 🖇️ Workflow Diagram  

```
flowchart TD
    A[Input URLs<br>via Streamlit] --> B[Document Loader<br>(UnstructuredURLLoader)]
    B --> C[Text Splitter<br>(RecursiveCharacterTextSplitter)]
    C --> D[Embeddings<br>(HuggingFace gte-base-en-v1.5)]
    D --> E[Vector Store<br>(ChromaDB)]
    E --> F[Retriever<br>Semantic Search]
    F --> G[LLM<br>(Groq gpt-oss-20b)]
    G --> H[Answer + Sources<br>Displayed in Streamlit]

```
## 📂 Project Structure


📦 real-estate-research-tool
```
├── resources/
│   └── vectorstore/        # Persistent ChromaDB storage
│   └── flowchart.png       # Flow diagram
├── rag.py                  # Core RAG logic (loading, embeddings, retrieval)
├── app.py                  # Streamlit UI
├── .env                    # API keys (Groq, etc.)
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## 🚀 Installation

1️⃣ Clone the repository:
```
git clone https://github.com/your-username/real-estate-research-tool.git
cd real-estate-research-tool
```
2️⃣ Create a virtual environment:
```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```
3️⃣ Install dependencies:
```
pip install -r requirements.txt
```

4️⃣ Set up environment variables in .env:
```
GROQ_API_KEY=your_groq_api_key
```
## ▶️ Usage

Run the Streamlit app:
```
streamlit run app.py
```

## 📸 Screenshots

🔹 App UI
<img width="2481" height="1366" alt="image" src="https://github.com/user-attachments/assets/9fc6a4ac-70f1-4d83-9a44-a6b2e782c205" />

🔹 Working Example
<img width="2069" height="1193" alt="Screenshot 2025-09-09 200231" src="https://github.com/user-attachments/assets/4a487423-66ca-421c-a153-8b346374d9de" />

## 🧩 Example Query
 url
 ```
https://www.researchnester.com/reports/web-scraping-software-market/5041
```
Question:
```
Size of the web scraping market?
```


📈 Future Improvements

 * Add support for PDF uploads

 * Use FAISS for faster retrieval on large datasets

 * Integrate with OpenAI GPT-4 or LLaMA-3 as alternative LLMs

 * Deploy on Streamlit Cloud / Hugging Face Spaces

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

## 📜 License

This project is licensed under the MIT License.


