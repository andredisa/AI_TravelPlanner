import streamlit as st
from agents.gpt_agent import get_gpt_agents

st.title("AI Travel Planner ✈️")
st.caption("Plan your next adventure using GPT-4o")

openai_api_key = st.text_input("Enter OpenAI API Key to access GPT-4o", type="password")
serp_api_key = st.text_input("Enter Serp API Key for Search functionality", type="password")

if openai_api_key and serp_api_key:
    researcher, planner = get_gpt_agents(openai_api_key, serp_api_key)

    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

    if st.button("Generate Itinerary"):
        with st.spinner("Researching your destination..."):
            research_results = researcher.run(f"Research {destination} for a {num_days} day trip", stream=False)
            st.write("✓ Research completed")

        with st.spinner("Creating your personalized itinerary..."):
            prompt = f"""
            Destination: {destination}
            Duration: {num_days} days
            Research Results: {research_results.content}

            Please create a detailed itinerary based on this research.
            """
            response = planner.run(prompt, stream=False)
            st.write(response.content)
