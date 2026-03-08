# 📈 Autonomous Finance AI Research Agent

Building a professional-grade financial intelligence tool using multi-agent orchestration. This project represents my journey from writing basic scripts to developing secure, agentic AI systems that reason through real-time market data.

---

## 🧠 The Development Journey

I built this project to master **AI Agentic Workflows**. Unlike a simple chatbot, this assistant uses specialized agents to handle complex financial research tasks.

### What I Learned:
* **Orchestration with Agno:** I learned how to use the Agno framework to manage hand-offs between a Finance Agent (data-focused) and a News Agent (sentiment-focused).
* **API Security (The Hard Way):** After initially exposing my API keys, I learned how to perform a Git history reset and implement a proper `.env` strategy to keep credentials private.
* **Data Synthesis:** I moved beyond pulling raw data. I trained the agent to synthesize "Buy/Hold/Sell" analyst ratings with live ticker news to provide a human-readable summary.

---

## ⚡ Core Features I Implemented

* **Real-Time Intelligence:** Automated retrieval of stock prices, spreads, and volume via `YFinance`.
* **Multi-Agent Reasoning:** The system cross-references market technicals with global news headlines before responding.
* **Security-First Design:** Implemented environment variable protection to ensure production-ready security standards.
* **Analyst Sentiment Aggregation:** Automatically calculates consensus from institutional analyst ratings.

---

## 🛠️ Technical Architecture

| Component | Technology |
| :--- | :--- |
| **Agent Framework** | [Agno](https://github.com/agno-ai/agno) |
| **Reasoning Model** | OpenAI GPT-4o |
| **Data Source** | YFinance (Yahoo Finance) |
| **Environment** | Python 3.10+ |

---

## ⚙️ Installation & Usage

1. **Clone the Project:**
   ```bash
   git clone [https://github.com/shivani-i-i/finance-ai-assistant.git](https://github.com/shivani-i-i/finance-ai-assistant.git)
Configure Security: Create a .env file in the root directory:

Plaintext
OPENAI_API_KEY=your_secret_key_here
Run the Assistant:

Bash
pip install -r requirements.txt
python finance_agent.py
📂 Project Roadmap
[x] Multi-Agent Workflow Implementation

[x] Real-time Financial Data Ingestion

[ ] Multi-Ticker Comparison Dashboards

[ ] Technical Indicator Integration (RSI/MACD)

[ ] PDF Report Exporting
 




 
