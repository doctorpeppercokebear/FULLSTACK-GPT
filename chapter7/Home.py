import streamlit as st
from langchain.prompts import PromptTemplate

a = [1, 2, 3, 4]

d = {"x": 1}

p = PromptTemplate.from_template("xxxx")

a

d

st.selectbox("choose your model", ("GPT-3", "GPT-4") )