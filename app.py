# import streamlit as st

# from src.engine import get_chat_engine
# from src.model_loader import initialise_llm, get_embedding_model

# st.title("Planty")
# st.write("Welcome to My Plant Chatbot App!")
# st.write("Ask Planty A Question About Plants, Herbs, and Flowers.")

# @st.cache_resource
# def load_chat_engine():
#     llm = initialise_llm()
#     embed_model = get_embedding_model()
#     chat_engine = get_chat_engine(llm=llm, embed_model=embed_model)
#     return chat_engine

# chat_engine = load_chat_engine()
    
# user_input = st.text_input("Your Question:")

# if st.button("Ask Planty"):
#     if user_input.strip():
#         response = chat_engine.chat(user_input)
#         st.write("Planty's Answer:")
#         st.write(str(response))
#     else:
#         st.warning("Please Enter a Question First.")

#-------------------------------------------------

import streamlit as st
from pathlib import Path

from src.engine import get_chat_engine
from src.model_loader import initialise_llm, get_embedding_model


#--------------------------------------------------------

def get_available_plants() -> list[str]:
    data_path = Path("data")
    plant_names = []

    for file in sorted(data_path.glob("*.txt")):
        name = file.stem.replace("_", " ").title()
        plant_names.append(name)
    
    return plant_names

#--------------------------------------------------------

st.set_page_config(
    page_title="Planty",
    page_icon="🌿",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #f6fbf4;
    }

    h1 {
        color: #2f6b3b;
    }

    h2, h3 {
        color: #3f7d47;
    }

    .stTextInput > div > div > input {
        border-radius: 12px;
    }

    .planty-box {
        background-color: #eaf6e6;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #cfe7c8;
        margin-top: 15px;
    }

    .small-note {
        color: #4f6f52;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Planty 🌿")
st.subheader("Your Botanical Assistant for Plants, Herbs, and Flowers")

st.markdown(
    "<p class='small-note'>Ask Planty about plant uses, growing conditions, plant families, seasonality, and more.</p>",
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("About Planty 🌱")
    st.write(
        "Planty is a small RAG Chatbot that answers questions based on a custom knowledge base about Herbs, Plants, and Flowers."
    )
    st.write("Example questions:")
    st.write("- What is Rosemary used for?")
    st.write("- What family does Bluebell belong to?")
    st.write("- What growing conditions does Sage prefer?")

@st.cache_resource
def load_chat_engine():
    llm = initialise_llm()
    embed_model = get_embedding_model()
    chat_engine = get_chat_engine(llm=llm, embed_model=embed_model)
    return chat_engine

chat_engine = load_chat_engine()

user_input = st.text_input("Enter your plant question here:")

if st.button("Ask Planty 🌿"):
    if user_input.strip():
        user_input_lower = user_input.lower().strip()

        if (
            "which plants do you know" in user_input_lower
            or "what plants do you know" in user_input_lower
            or "what flowers do you know" in user_input_lower
            or "what herbs do you know" in user_input_lower
            or "what information do you have" in user_input_lower
        ):
            plant_names = get_available_plants()
            response = (
                "I currently have information about the following plants, herbs, flowers, crops, and trees:\n\n- "
                + "\n- ".join(plant_names)
            )

        elif (
            "who are you" in user_input_lower
            or "what are you" in user_input_lower
            or "tell me about yourself" in user_input_lower
        ):
            response = (
                "I'm Planty, a factual botanical assistant. "
                "I answer questions about plants, herbs, and flowers based on the documents in my knowledge base."
            )

        elif (
            "what can you do" in user_input_lower
            or "what can you help me with" in user_input_lower
        ):
            response = (
                "I can answer questions about plant uses, families, growing conditions, seasonality, and distribution."
            )

        else:
            response = str(chat_engine.chat(user_input))

        st.markdown("## Planty's Answer")
        st.markdown(
            f"<div class='planty-box'>{response}</div>",
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter a question first.")

#-------------------------------------------------

user_input_lower = user_input.lower().strip()

if (
    "which plants do you know" in user_input_lower
    or "what plants do you know" in user_input_lower
    or "what flowers do you know" in user_input_lower
    or "what herbs do you know" in user_input_lower
    or "what information do you have" in user_input_lower
):
    plant_names = get_available_plants()
    response = (
        "I currently have information about the following plants, herbs, flowers, crops, and trees:\n\n- "
        + "\n- ".join(plant_names)
    )

elif (
    "who are you" in user_input_lower
    or "what are you" in user_input_lower
    or "tell me about yourself" in user_input_lower
):
    response = (
        "I'm Planty, a factual botanical assistant. "
        "I answer questions about plants, herbs, and flowers based on the documents in my knowledge base."
    )

elif (
    "what can you do" in user_input_lower
    or "what can you help me with" in user_input_lower
):
    response = (
        "I can answer questions about plant uses, families, growing conditions, seasonality, and distribution."
    )

else:
    response = str(chat_engine.chat(user_input))

