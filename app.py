import streamlit as st

from transformers import pipeline

st.set_page_config(page_title="🖋BN-Poets")
st.title("Bengali Poets")

st.markdown(
        """**Bengali-Poets** is an app, developed by [Ritobrata Ghosh](https://ghosh-r.github.io)  where you can generate Bengali poetry using a prompt of your choice. You can either choose a model that writes poetry in the style of [Rabindranath Tagore](https://wikipedia.org/wiki/Rabindranath_Tagore), Asia's first Nobel Laureate in Literature."""
)

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

user_input = st.text_input("prompt", value="আমি তোমাকে দেখেছি হৃদয় মাঝে ", help="The AI will generate poetry taking this as the first line")

if st.button("Write a poem"):
    poem = poet(user_input, max_length=max_len)

    output = poem[0]['generated_text'].replace('\n', ' ').replace('\xa0', '')


    st.write(output)
