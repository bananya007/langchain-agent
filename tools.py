"""
tools.py
Defines tools for the agent:
1) TavilySearch (web search)
2) CalculatorTool (evaluate ENTIRE arithmetic expression)
"""

from dotenv import load_dotenv

load_dotenv()

# --- Tavily Search Tool (LangChain community) ---
from langchain_community.tools.tavily_search import TavilySearchResults

tavily_tool = TavilySearchResults(
    name="TavilySearch",
    description=(
        "Web search. Use for questions that require current or factual web information. "
        "Input should be a search query in plain English."
    ),
)

# --- Calculator Tool ---
from langchain.tools import tool
import math


@tool("CalculatorTool", return_direct=True)
def calculator_tool(expression: str) -> str:
    """
    Evaluate the ENTIRE arithmetic expression and return only the numeric result.
    Supports +, -, *, /, parentheses, and functions: sqrt, pow.
    Examples:
      '12 * sqrt(25)' -> '60.0'
      '(3 + 7) / 2'   -> '5.0'
    """
    safe_globals = {"__builtins__": None}
    safe_locals = {"sqrt": math.sqrt, "pow": math.pow}
    try:
        value = eval(expression, safe_globals, safe_locals)
        return str(value)
    except Exception as e:
        return f"Error evaluating expression: {e}"


# Export tools
TOOLS = [tavily_tool, calculator_tool]
