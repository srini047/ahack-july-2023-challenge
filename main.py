import streamlit as st
import warnings

# Data
import pandas as pd

df = pd.read_csv("./archive/cleaned_data.csv")

# Chat
from app.chat import chat_with_pokemon_data

# Plots
from pages.radar_plot import radar_plot
from pages.contour_plot import contour_plot
from pages.heatmap_plot import heatmap_plot
from pages.total_dist_plot import dist_plot


warnings.filterwarnings("ignore")
chat_history = []

# App title
st.set_page_config(page_title="🏙️💬 Data Story Telling")
st.title("Data Visualisation")
st.caption("Talk your way through data")

INITIAL_MESSAGE = [
    {"role": "user", "content": "Hi!"},
    {
        "role": "assistant",
        "content": "Hey user, I'm Pokemon Chatty, your all in answer finder to any questions related to Pokemon. Feel free to ask them...💬",
    },
]


with open("ui/styles.md", "r") as styles_file:
    styles_content = styles_file.read()

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I help you?"}
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    # with st.chat_message("assistant"):
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_with_pokemon_data(prompt)
            st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

################################################################
# Here it has to be updated with intro and about the dataset


################################################################
# Plots
with st.container():
    # 1. Radar plot
    st.write("Radar plot")
    st.plotly_chart(radar_plot(df, "Charmander"))

    # 2. Contour plot (Not supported yet by Streamlit)
    st.write("Contour plot")
    st.plotly_chart(contour_plot(df))

    # 3. Heatmap plot
    st.write("Heatmap plot")
    st.plotly_chart(heatmap_plot(df))

    # 4. Distplot
    st.write("Distplot")
    st.plotly_chart(dist_plot(df, "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"))
