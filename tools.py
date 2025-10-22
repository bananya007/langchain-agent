"""
tools.py
Defines tools for the LangChain agent:
1. TavilySearchResults (web search)
2. CalculatorTool (math operations)
"""

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
import math
from dotenv import load_dotenv
import os

load_dotenv()

# --- Tavily Search Tool ---
tavily_tool = TavilySearchResults(
    name="TavilySearch", description="Search the web using Tavily API"
)


# --- Calculator Tool ---
@tool("CalculatorTool", return_direct=True)
def calculator_tool(expression: str) -> str:
    """Evaluates simple math expressions (e.g., '2 + 2', 'sqrt(16)')."""
    try:
        result = eval(
            expression, {"__builtins__": None}, {"sqrt": math.sqrt, "pow": math.pow}
        )
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"


# List of tools to export
TOOLS = [tavily_tool, calculator_tool]
