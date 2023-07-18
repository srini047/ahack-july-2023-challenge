from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

import streamlit as st

# Load the OpenAI API key from the environment variable
def chat_with_pokemon_data(prompt: str):
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

    agent = create_csv_agent(
        OpenAI(temperature=0.7),
        "archive/cleaned_data.csv",
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    response = agent.run(prompt)
    return response
