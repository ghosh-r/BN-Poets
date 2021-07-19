import streamlit as st

from transformers import pipeline

poet = pipeline('text-generation',
        model='ghosh-r/robi-kobi',
        tokenizer='ghosh-r/bangla-gpt2')

poem = poet('দরজা ধরে দাঁড়াও তুমি', max_length=250)

output = poem[0]['generated_text'].replace('\n', ' ').replace('\xa0', '')


st.write(output)
