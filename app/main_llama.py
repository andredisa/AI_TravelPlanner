import streamlit as st
from agents.llama_agent import get_llama_agents

st.title("AI Travel Planner using Llama-3.2 ✈️")
st.caption("Plan your next adventure using local Llama-3")

serp_api_key = st.text_input("Enter Serp API Key for Search functionality", type="password")

if serp_api_key:
    researcher, planner = get_llama_agents(serp_api_key)

    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

    if st.button("Generate Itinerary"):
        with st.spinner("Generating your itinerary..."):
            response = planner.run(f"{destination} for {num_days} days", stream=False)
            st.write(response.content)
