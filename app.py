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

st.markdown("""
### Training Procedure

* First a 117 million parameter GPT-2 model was trained from scratch on TPUv3-8 enabled virtual machines. You can find the model [here](https://huggingface.co/ghosh-r/bangla-gpt2).
* Next, that model was fine-tuned on Bengali Poems on text-fortmat. The data can be found [here](https://kaggle.com/truthr/https://www.kaggle.com/truthr/free-bengali-poetry).
* The training Notebook can be found [here](https://colab.research.google.com/drive/1zXpoWWdFoNmMKvlZT1bOboHBY5rWKtuk?usp=sharing).

### References:

* Bangla-GPT2, Ritobrata Ghosh, Hugging Face, 2021
* Ritobrata Ghosh, “Free Bengali Poetry.” Kaggle, 2021, doi: 10.34740/KAGGLE/DSV/2400728.

### Acknowledgements:

* The **Hugging Face Team** for providing thorough and continuous support during the project.
* **Google Cloud** for providing the TPUv3 enabled Virtual Machines.

Copyright Ritobrata Ghosh 2021. [GitHub](https://github.com/ghosh-r/BN-Poets)
        """)
