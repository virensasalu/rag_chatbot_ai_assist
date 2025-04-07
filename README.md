
#   Jeeva AI Assistant

A conversational AI assistant designed to help users explore Jeeva's website summarizing key content, answering questions, and providing quick insights into Jeeva’s mission, journey, and services.

This assistant scrapes content from the Jeeva website, converts it into Markdown, indexes the content using LangChain + FAISS, and serves answers via a beautiful Gradio chat interface with an elegant, corporate-clean UI.

---

##  Features

-  **Web Scraping** — Extract structured data and page text from any Jeeva-related webpage.
-  **Markdown Export** — Saves scraped content into `.md` files for transparency and reuse.
- **LangChain + FAISS** — Index and retrieve content using vector search.
- **OpenAI GPT Integration** — Use LLMs to summarize and answer questions conversationally.
- **Gradio Chat UI** — A clean and user-friendly frontend styled for enterprise-grade UX.
- **RAG Pipeline** — Uses retrieval-augmented generation to ground answers in scraped content.

---

## Project Structure

```
├── README.md  
├── requirements.txt  
├── .env  
├── .gitignore  
├── jeevaenv/                   # Virtual environment (should be gitignored)  
├── knowledge_base/             # Markdown files used for the knowledge base  
│   ├── about.md  
│   ├── journey.md  
│   └── serve.md  
├── scr/                        # Source code and notebooks  
│   ├── scrape.py               # Web scraping + markdown exporter  
│   ├── chat_rag.ipynb          # RAG + vector search notebook  
│   ├── openai.ipynb            # Summarization + chat logic  
└── logo.png                    # Project logo for branding
```

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/jeeva-ai-assistant.git
cd jeeva-ai-assistant
```

### 2. Create a virtual environment

```bash
python3 -m venv jeevaenv
source jeevaenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a `.env` file in the root:

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

##  How It Works

1. `scr/scrape.py` scrapes the website and converts the content to Markdown
2. `knowledge_base/*.md` are loaded and split into chunks
3. `chat_rag.ipynb` creates embeddings and sets up the retrieval chain
4. `app.py` (or similar) runs a Gradio chat interface using LangChain + OpenAI

---

##  Usage

Run the app with:

```bash
python app.py
```

Or run your notebooks interactively in VS Code or Jupyter:

```bash
jupyter notebook
```

---

## Tech Stack

- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/)
- [Gradio](https://gradio.app/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Python 3.10+](https://www.python.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)



---

##  Deployment

This app is suitable for deployment on platforms like:

- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Render](https://render.com/)
- [Replit](https://replit.com/)
- [Streamlit Cloud](https://streamlit.io/cloud)



---

##  License

MIT License. Feel free to use, extend, or fork this project for educational or commercial use.

---

## Credits

Created by [@virensasalu](https://github.com/virensasalu)

---
