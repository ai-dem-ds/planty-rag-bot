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

from src.engine import get_chat_engine
from src.model_loader import initialise_llm, get_embedding_model

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
        response = chat_engine.chat(user_input)

        st.markdown("### Planty's Answer")
        st.markdown(
            f"<div class='planty-box'>{str(response)}</div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter a question first.")
#-------------------------------------------------

# meta questions
meta_questions = [
    "who are you",
    "what are you",
    "what can you do",
    "what can you help me with",
    "which plants do you know",
    "what plants do you know",
    "what information do you have",
    "tell me about yourself"
]

user_input_lower = user_input.lower().strip()

if any(q in user_input_lower for q in meta_questions):
    response = (
        "I'm Planty, a factual botanical assistant. "
        "I answer questions about plants, herbs, and flowers based on the documents in my knowledge base. "
        "You can ask me about plant uses, families, growing conditions, seasonality, and distribution. "
    )
else:
    response = str(chat_engine.chat(user_input))

if "which plants do you know" in user_input_lower or "what plants do you know" in user_input_lower:
    response = (
        "I currently have information about several plants, herbs, flowers, crops, and trees in my knowledge base. "
        "You can ask me specific question about any plant included in the uploaded documents. "
    )


#-------------------------------------------------

# import streamlit as st

# from src.engine import get_chat_engine
# from src.model_loader import initialise_llm, get_embedding_model

# st.set_page_config(
#     page_title="Planty",
#     page_icon="🌿",
#     layout="wide"
# )

# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(to bottom right, #f8fbf6, #eef5ea);
#         color: #2f3e2f;
#     }

#     .main-title {
#         font-size: 58px;
#         font-weight: 700;
#         color: #2f5d3a;
#         margin-bottom: 0.2rem;
#     }

#     .sub-title {
#         font-size: 22px;
#         font-weight: 600;
#         color: #425b46;
#         margin-bottom: 1rem;
#     }

#     .intro-text {
#         font-size: 18px;
#         color: #5a6d5d;
#         margin-bottom: 2rem;
#         line-height: 1.6;
#     }

#     .section-title {
#         font-size: 30px;
#         font-weight: 700;
#         color: #2f5d3a;
#         margin-top: 1.5rem;
#         margin-bottom: 1rem;
#     }

#     .answer-box {
#         background: #f3f8ef;
#         border: 1px solid #dbe7d2;
#         border-radius: 18px;
#         padding: 22px;
#         color: #334233;
#         font-size: 18px;
#         line-height: 1.7;
#         box-shadow: 0 6px 18px rgba(47, 93, 58, 0.06);
#     }

#     .sidebar-box {
#         background: rgba(255,255,255,0.55);
#         border: 1px solid #dde8d8;
#         border-radius: 18px;
#         padding: 18px;
#         margin-top: 10px;
#     }

#     .small-note {
#         color: #607060;
#         font-size: 15px;
#         line-height: 1.6;
#     }

#     .stTextInput > div > div > input {
#         border-radius: 14px;
#         border: 1px solid #cfdcc9;
#         background-color: #fbfdf9;
#         color: #2f3e2f;
#         padding: 0.7rem;
#     }

#     .stButton > button {
#         border-radius: 14px;
#         border: 1px solid #b9cfb3;
#         background-color: #e8f1e2;
#         color: #2f5d3a;
#         font-weight: 600;
#         padding: 0.5rem 1.2rem;
#     }

#     .stButton > button:hover {
#         background-color: #dcebd3;
#         border: 1px solid #a8c49f;
#         color: #264a2f;
#     }
#     </style>
# """, unsafe_allow_html=True)

# @st.cache_resource
# def load_chat_engine():
#     llm = initialise_llm()
#     embed_model = get_embedding_model()
#     return get_chat_engine(llm=llm, embed_model=embed_model)

# chat_engine = load_chat_engine()

# left_col, right_col = st.columns([1, 2.2], gap="large")

# with left_col:
#     st.markdown("<div class='sidebar-box'>", unsafe_allow_html=True)
#     st.markdown("## About Planty 🌱")
#     st.markdown(
#         "<p class='small-note'>"
#         "Planty is a small RAG chatbot that answers questions based on a custom knowledge base "
#         "about herbs, plants, and flowers."
#         "</p>",
#         unsafe_allow_html=True
#     )

#     st.markdown("### Example questions")
#     st.markdown(
#         """
# - What is rosemary used for?
# - What family does bluebell belong to?
# - What growing conditions does sage prefer?
# - What is English lavender known for?
#         """
#     )
#     st.markdown("</div>", unsafe_allow_html=True)

# with right_col:
#     st.markdown("<div class='main-title'>Planty 🌿</div>", unsafe_allow_html=True)
#     st.markdown(
#         "<div class='sub-title'>Your botanical assistant for plants, herbs, and flowers</div>",
#         unsafe_allow_html=True
#     )
#     st.markdown(
#         "<div class='intro-text'>"
#         "Ask Planty about plant uses, growing conditions, plant families, seasonality, distribution, and more."
#         "</div>",
#         unsafe_allow_html=True
#     )

#     user_input = st.text_input("Enter your plant question here:")

#     if st.button("Ask Planty 🌿"):
#         if user_input.strip():
#             response = chat_engine.chat(user_input)
#             st.markdown("<div class='section-title'>Planty's Answer</div>", unsafe_allow_html=True)
#             st.markdown(
#                 f"<div class='answer-box'>{str(response)}</div>",
#                 unsafe_allow_html=True
#             )
#         else:
#             st.warning("Please enter a question first.")


