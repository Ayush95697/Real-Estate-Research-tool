import streamlit as st
import pandas as pd
import numpy as np
from rag import process_urls , generate_answers

st.title("Real Estate Research Tool")
url1=st.sidebar.text_input("Enter the URL",key="url1")
url2=st.sidebar.text_input("Enter the URL",key="url2")
url3=st.sidebar.text_input("Enter the URL",key="url3")

placeholder=st.empty()
process_url_button=st.sidebar.button("Process URLs")
if process_url_button:
    urls=[url for url in (url1,url2,url3) if url!=""]
    if len(urls)==0:
        placeholder.error("Please select at least one URL")
    else:
        for status in process_urls(urls):
            placeholder.text(status)

query=placeholder.text_input("Question")
if query!="":
    try:
        answers,sources=generate_answers(query)
        st.header("Answers:")
        st.write(answers)

        if sources:
            st.header("Sources:")
            for source in sources.split("\n"):
                st.write(source)
    except RuntimeError as e:
        placeholder.text("You must process urls First")