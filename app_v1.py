import streamlit as st
import asyncio
from googletrans import Translator, LANGUAGES

# Set up Streamlit page
st.set_page_config(
    page_title="Translator App",
    page_icon="🈸",
    layout="centered"
)

st.title("🈸 Language Translator App")

# Get language list dynamically
languages = {v.title(): k for k, v in LANGUAGES.items()}

col1, col2 = st.columns(2)

with col1:
    input_language_name = st.selectbox("Your Language", options=languages.keys())
    input_language = languages[input_language_name]

with col2:
    output_languages_list = {k: v for k, v in languages.items() if v != input_language}
    output_language_name = st.selectbox("Translated Language", options=output_languages_list.keys())
    output_language = output_languages_list[output_language_name]

input_text = st.text_area("Type the text to be translated")

if st.button("Translate"):
    if input_text.strip():
        try:
            translator = Translator()
            translation = asyncio.run(translator.translate(input_text, src=input_language, dest=output_language))
            st.success(translation.text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter text to translate.")
