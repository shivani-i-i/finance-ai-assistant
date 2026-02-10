# skip-secret-scanning:true
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

# 1. Load the API key from your .env file
load_dotenv()

# 2. Create the Finance Agent (Fixed for the newest Agno version)
finance_agent = Agent(
    name="Finance AI Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        DuckDuckGoTools(), 
        YFinanceTools() # No extra arguments needed here anymore!
    ],
    instructions=["Use tables to display financial data.", "Always cite your sources."],
    markdown=True,
)

# 3. Simple terminal interface
print("\n🚀 Finance Agent is ready!")
while True:
    query = input("\n💬 Ask a finance query (or type 'exit'): ")
    if query.lower() in ['exit', 'quit']:
        break
    finance_agent.print_response(query, stream=True)