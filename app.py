import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title="Welcome to Sreatmlit"
openai_api_key = st.sidebar.text_input("open AI API Key", type='password')

def generate_response(input_text):
    model= ChatOpenAI(temperature=0.7,api_key=openai_api_key,)
    st.info(model.invoke(input_text))


# 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
#res = requests.get('https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/sick2014/SICK_train.txt',verify=False)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)