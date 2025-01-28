import streamlit as st
from datetime import datetime

today = datetime.today().strftime("%H:%M:%S")

st.title(today)

model = st.selectbox("choose your model", ("GPT-3", "GPT-4") )

if model == "GPT-3":
    st.write("cheap")
else:
    # st.write("not cheap")

    st.write(model)

    name = st.text_input("What is your name")

    st.write(name)

    value = st.slider("temperature", min_value=0.1, max_value=1.0 )