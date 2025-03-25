import asyncio
import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS

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

# Generate and show the original audio as soon as the user types something
input_audio_path = "audio/input_audio.mp3"

if input_text.strip():
    gTTS(text=input_text, lang=input_language, slow=False).save(input_audio_path)
    st.markdown("**🔊 Original Audio:**")
    st.audio(input_audio_path, format="audio/mp3")

if st.button("Translate"):
    if input_text.strip():
        try:
            translator = Translator()
            translation = asyncio.run(translator.translate(input_text, src=input_language, dest=output_language))
            translated_text = translation.text

            # Display translated text
            st.success(translated_text)

            # Generate and show translated audio
            translated_audio_path = "audio/translated_audio.mp3"
            gTTS(text=translated_text, lang=output_language, slow=False).save(translated_audio_path)

            st.markdown("**🔊 Translated Audio:**")
            st.audio(translated_audio_path, format="audio/mp3")

        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter text to translate.")
