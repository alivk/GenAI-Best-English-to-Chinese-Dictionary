import base64
from gtts import gTTS
import streamlit as st

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def generate_pronunciation(word: str, lang='en-uk'):
    try:
        tts = gTTS(text=word, lang=lang)
        file_path = f"temp/pronunciation.mp3"
        tts.save(file_path)
        return file_path
    except Exception as e:
        st.error(f"Error generating pronunciation: {e}")
        return None 