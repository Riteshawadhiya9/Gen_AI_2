# Generative AI Learning & Implementation Project

A comprehensive Python project exploring Generative AI concepts, LLM integration, document processing, and vector-based retrieval systems. This project demonstrates practical implementations of modern AI technologies including multi-provider LLM support, document loading, embeddings, and semantic search.

## 🎯 Project Overview

This project serves as both a **learning resource** and a **practical implementation** of Generative AI technologies. It includes:

- **Multi-LLM Support**: Integration with Google Gemini, Groq (Llama), and Mistral AI
- **Document Processing**: PDF and webpage loaders for content extraction
- **Vector Store**: ChromaDB for semantic search and similarity matching
- **Comprehensive Documentation**: Detailed notes on GenAI concepts and LLM architectures

## 📁 Project Structure

```
Gen_AI_2/
├── Document_loaders/          # Document extraction and loading
│   ├── Generate_Summary_text.py
│   ├── Implement_pypdf_loader.py
│   ├── main.py               # Main document loading pipeline
│   ├── pdf_loader.py         # PDF processing
│   ├── webpage_loader.py     # Web content extraction
│   └── notes.txt             # Comprehensive GenAI concepts
├── Vector_Store/              # Embedding and vector database
│   └── DB.py                 # ChromaDB implementation
├── retrievers/               # Information retrieval systems
│   └── arixv.py
├── test_all_models/          # LLM testing and comparison
│   └── llms.py              # Multi-model inference tests
├── chroma-db/               # Persistent vector database
│   └── (ChromaDB storage)
├── requirements.txt         # Project dependencies
├── test.py                 # General tests
└── test_OpenRouter.py      # OpenRouter API testing
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- API keys for:
  - Google Generative AI (Gemini)
  - Groq
  - Mistral AI

### Installation

1. **Clone the repository**
   ```bash
   cd Gen_AI_2
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```
   GOOGLE_API_KEY=your_google_api_key
   GROQ_API_KEY=your_groq_api_key
   MISTRAL_API_KEY=your_mistral_api_key
   ```

## 📦 Dependencies

Core dependencies:
- **LangChain**: Framework for building LLM applications
  - `langchain` - Core framework
  - `langchain-core` - Core abstractions
  - `langchain-community` - Community integrations
  - `langchain-google-genai` - Google Gemini integration
  - `langchain-groq` - Groq integration
  - `langchain-mistralai` - Mistral AI integration

- **Vector Store**: `chromadb` - Vector database for embeddings
- **Document Processing**: 
  - `pypdf` - PDF processing
  - `beautifulsoup4` - Web scraping
  - `requests` - HTTP requests

- **Utilities**:
  - `python-dotenv` - Environment variable management
  - `fastapi` & `uvicorn` - Web framework (optional)
  - `faiss-cpu` - Vector similarity search
  - `tiktoken` - Token counting

## 💡 Key Features

### 1. **Multi-LLM Testing** (`test_all_models/llms.py`)
Compare responses from different LLM providers:
```python
# Google Gemini
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Groq (Llama 3.1)
model2 = ChatGroq(model="llama-3.1-8b-instant")

# Mistral AI
model3 = ChatMistralAI(model="mistral-small-2506")
```

### 2. **Document Loading** (`Document_loaders/`)
- **PDF Loader**: Extract text from PDF files
- **Webpage Loader**: Scrape and process web content
- **Text Loader**: Process text files
- **Summarization**: Generate summaries of loaded documents

### 3. **Vector Store & Embeddings** (`Vector_Store/DB.py`)
- Create embeddings using Mistral AI
- Store vectors in ChromaDB
- Perform semantic similarity search
- Retrieve contextually relevant documents

### 4. **Retriever Systems** (`retrievers/`)
- Semantic search based on embeddings
- Document retrieval pipelines
- Context-aware information extraction

## 🔧 Usage Examples

### Running LLM Tests
```bash
cd test_all_models
python llms.py
```

This will test all three LLM providers and display their responses side-by-side.

### Loading Documents
```bash
cd Document_loaders
python main.py
```

Loads and processes documents from the specified sources.

### Vector Search
```bash
cd Vector_Store
python DB.py
```

Creates embeddings and performs similarity search on sample documents.

## 📚 Learning Resources

The `Document_loaders/notes.txt` contains comprehensive documentation on:

- **Introduction to Generative AI**: Concepts and definitions
- **Evolution of GenAI**: Historical context and milestones
- **Core Concepts**: AI, ML, DL, Neural Networks
- **Large Language Models (LLMs)**: How they work and applications
- **Transformer Architecture**: Foundation of modern GenAI
- **Tokenization and Embeddings**: Text representation techniques
- **Fine-tuning and Training**: Model customization
- **Practical Applications**: Real-world use cases
- **Challenges and Future**: Current limitations and opportunities

## 🔑 Key Concepts Covered

### Generative AI Fundamentals
- What is GenAI and how it differs from traditional AI
- Evolution from ML → DL → Transformers → LLMs
- Types of generative models (GANs, VAEs, Diffusion Models, LLMs)

### LLMs in Practice
- How LLMs process and generate text
- Token-based processing
- Context windows and attention mechanisms
- Prompt engineering and fine-tuning

### Vector Embeddings
- Converting text to numerical representations
- Similarity metrics (cosine, euclidean)
- Semantic search applications

### Document Processing
- PDF extraction and parsing
- Web scraping and content cleaning
- Text preprocessing and normalization

## 🧪 Testing

### Test Files
- `test.py` - General functionality tests
- `test_OpenRouter.py` - OpenRouter API testing
- `test_all_models/llms.py` - LLM comparison tests

Run tests with:
```bash
python test.py
python test_all_models/llms.py
```

## 🔐 Security Notes

- Never commit `.env` files containing API keys
- Keep API keys secure and rotate regularly
- Use environment variables for sensitive information
- Review API rate limits for each provider

## 📊 LLM Providers Comparison

| Provider | Model | Use Case | Speed | Cost |
|----------|-------|----------|-------|------|
| Google Gemini | gemini-2.5-flash | General purpose, fast responses | ⚡⚡⚡ | 💰 |
| Groq | llama-3.1-8b | Open-source, efficient | ⚡⚡⚡⚡ | 💰💰 |
| Mistral | mistral-small-2506 | Balanced performance | ⚡⚡ | 💰 |

## 🛠️ Development Workflow

1. **Set up environment**: Create `.venv` and install dependencies
2. **Configure API keys**: Add to `.env` file
3. **Explore notebooks**: Start with test files to understand APIs
4. **Integrate LLMs**: Build custom chains with LangChain
5. **Process documents**: Use document loaders for your content
6. **Create retrievers**: Build RAG (Retrieval-Augmented Generation) systems
7. **Deploy**: Use FastAPI for production endpoints

## 📈 Next Steps & Extensions

- [ ] Build a chatbot using LangChain agents
- [ ] Implement RAG (Retrieval-Augmented Generation) pipeline
- [ ] Add more document loaders (CSV, Excel, SQL databases)
- [ ] Create FastAPI endpoints for LLM inference
- [ ] Implement fine-tuning pipelines
- [ ] Add prompt templates and chains
- [ ] Build evaluation metrics for LLM responses
- [ ] Deploy with Docker containers

## 🤝 Contributing

This is a personal learning project. Feel free to:
- Extend with new LLM providers
- Add more document loaders
- Improve vector search capabilities
- Create additional retrieval strategies

## 📝 Notes

- This project uses the latest versions of LangChain (v0.1+)
- ChromaDB is used for persistent vector storage
- All models are accessed via API (no local model deployment)
- Requires active internet connection for API calls

## 🚨 Troubleshooting

### API Key Issues
- Verify keys are correctly set in `.env`
- Check API key permissions and quotas
- Ensure APIs are enabled in respective dashboards

### Import Errors
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Verify virtual environment is activated
- Check Python version compatibility

### Memory Issues
- Use `faiss-cpu` instead of GPU versions for lighter memory usage
- Process documents in batches
- Clear cache periodically

## 📄 License

This project is open for learning and educational purposes.

## 👨‍💻 Author

Created as a comprehensive learning resource for Generative AI technologies.

---

**Last Updated**: 2026-06-04

For questions or issues, refer to the comprehensive notes in `Document_loaders/notes.txt` or the LangChain documentation.
