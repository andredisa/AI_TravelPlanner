from textwrap import dedent
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
from agno.models.openai import OpenAIChat

def get_gpt_agents(openai_api_key, serp_api_key):
    researcher = Agent(
        name="Researcher",
        role="Searches for travel destinations...",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        description=dedent("""\
            You are a world-class travel researcher...
        """),
        instructions=[
            "Generate a list of 3 search terms...",
            "Search and analyze results.",
            "Return top 10 most relevant.",
        ],
        tools=[SerpApiTools(api_key=serp_api_key)],
        add_datetime_to_instructions=True,
    )

    planner = Agent(
        name="Planner",
        role="Generates a draft itinerary...",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        description=dedent("""\
            You are a senior travel planner...
        """),
        instructions=[
            "Use research to generate itinerary.",
            "Ensure structure, detail, and accuracy.",
        ],
        add_datetime_to_instructions=True,
    )

    return researcher, planner
