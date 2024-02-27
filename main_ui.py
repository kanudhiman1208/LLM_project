# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import streamlit as st
#from langchain_helper import get_qa_chain, create_vector_db
from ipynb.fs.full.langchain_helper import get_qa_chain, create_vector_db

from streamlit_jupyter import StreamlitPatcher, tqdm
StreamlitPatcher().jupyter()

st.title("PeopleMetrics Mate")
btn = st.button("Update the Repository")
if btn:
    create_vector_db()

# +
question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
# -


