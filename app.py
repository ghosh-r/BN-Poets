import streamlit as st

from transformers import pipeline

st.set_page_config(page_title="🖋BN-Poets")
st.title("Bengali Poets")

st.sidebar.subheader("Select sequence length of poem.")
max_len = st.sidebar.slider(
    "Maximum length",
    value=150,
    min_value=100,
    max_value=250,
    help="The maximum length of the sequence to be generated."
)

poet = pipeline('text-generation',
        model='ghosh-r/robi-kobi',
        tokenizer='ghosh-r/bangla-gpt2')

if st.button("Write a poem"):
    poem = poet('দরজা ধরে দাঁড়াও তুমি', max_length=max_len)

    output = poem[0]['generated_text'].replace('\n', ' ').replace('\xa0', '')


    st.write(output)
