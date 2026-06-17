# Smart Website Navigator Agent

A LangGraph-powered AI agent that crawls a website, extracts page content, and uses a Groq LLM to identify the pages most relevant to a user's topic of interest.

Instead of relying only on URL names or anchor text, the agent analyzes the actual content of each webpage and ranks pages semantically.

---

## Features

- Website crawling
- Internal link discovery
- Content extraction using BeautifulSoup
- Semantic relevance scoring using Groq LLM
- LangGraph workflow orchestration
- JSON report generation
- Topic-based website exploration

---

## Example

### Input

Website URL:

```text
https://intelgic.com
```

Topic:

```text
machine learning
```

### Output

```text
Score: 10
URL: https://intelgic.com/machine-vision-system-AI

Reason:
This page focuses on AI-powered machine vision systems and industrial machine learning applications.
```

---

## Project Structure

```text
site_map/
│
├── app.py
├── requirements.txt
├── .env
│
├── agents/
│   ├── crawler.py
│   ├── content_agent.py
│   ├── relevance_agent.py
│   └── reporter.py
│
├── graph/
│   └── workflow.py
│
├── models/
│   └── state.py
│
├── utils/
│   ├── crawler_utils.py
│   ├── page_parser.py
│   └── llm.py
│
└── outputs/
```

---

## Workflow

```text
User URL
    ↓
Crawler Agent
    ↓
Extract Internal Links
    ↓
Content Extraction Agent
    ↓
Groq Relevance Agent
    ↓
Rank Pages
    ↓
Generate Report
```

---

## Technologies Used

- Python
- LangGraph
- LangChain
- Groq
- BeautifulSoup4
- Requests

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd site_map
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get a free API key from:

https://console.groq.com

---

## Run Project

```bash
python app.py
```

Enter:

```text
Website URL: https://example.com
Topic of interest: machine learning
```

---

## Output

The application generates:

```text
outputs/
└── relevant_pages.json
```

Example:

```json
[
  {
    "url": "https://example.com/ai-solutions",
    "score": 10,
    "reason": "The page focuses on machine learning and AI solutions."
  }
]
```

---

## Future Improvements

- Streamlit Web UI
- Website visualization graph
- Multi-page content summarization
- RAG-based website search
- Export results to PDF
- Parallel crawling for faster analysis
- Support for sitemap.xml discovery

---

## Learning Outcomes

This project demonstrates:

- Agentic workflow design using LangGraph
- Web crawling and scraping
- LLM-powered semantic search
- Prompt engineering
- Structured JSON extraction from LLMs
- Workflow orchestration

---

## Author

Chaandrayee Dutta