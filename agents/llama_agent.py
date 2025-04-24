from textwrap import dedent
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
from agno.models.ollama import Ollama

def get_llama_agents(serp_api_key):
    researcher = Agent(
        name="Researcher",
        role="Searches for travel destinations, activities, and accommodations based on user preferences",
        model=Ollama(id="llama3.2", max_tokens=1024),
        description=dedent("""\
            You are a world-class travel researcher...
        """),
        instructions=[
            "Generate a list of 3 search terms...",
            "For each term, `search_google` and analyze...",
            "Return the 10 most relevant results.",
        ],
        tools=[SerpApiTools(api_key=serp_api_key)],
        add_datetime_to_instructions=True,
    )

    planner = Agent(
        name="Planner",
        role="Generates a draft itinerary based on user preferences and research results",
        model=Ollama(id="llama3.2", max_tokens=1024),
        description=dedent("""\
            You are a senior travel planner...
        """),
        instructions=[
            "Generate a draft itinerary...",
            "Ensure quality, clarity, and factual accuracy.",
        ],
        add_datetime_to_instructions=True,
    )

    return researcher, planner
