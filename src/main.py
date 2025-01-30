import streamlit as st
from bedrock_utils import get_bedrock_client
from prompts import get_word_definition_prompt
from audio_utils import generate_pronunciation, autoplay_audio
import json

def get_word_definition(word_or_sentence):
    prompt = get_word_definition_prompt(word_or_sentence)
    bedrock = get_bedrock_client()
    if bedrock:
        try:
            body = json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 1000,
                "temperature": 0.5,
                "top_p": 1,
            })
            
            response = bedrock.invoke_model(
                body=body,
                modelId="anthropic.claude-v2"
            )
            
            result = json.loads(response.get('body').read())
            return result.get('completion')
        except Exception as e:
            st.error(f"Error getting definition: {e}")
    return None

# Streamlit UI
st.title("GenAI Best English to Chinese Dictionary")
st.write("Enter a word or sentence to get its detailed explanation")

input_text = st.text_input("Enter a word or sentence:")
if input_text:
    with st.spinner("Getting definition..."):
        definition = get_word_definition(input_text)
        if definition:
            # Split the definition into parts
            parts = definition.split("**Pronunciation Reference:**")
            word_meaning = parts[0]
            remaining = parts[1] if len(parts) > 1 else ""
            
            # Display Word Meaning and pronunciation button
            st.markdown(word_meaning)
            
            # Extract the word from the definition
            word = input_text.split()[-1]  # Get the last word if it's a sentence
            if " " not in input_text:  # If it's a single word
                word = input_text
            
            # Create pronunciation button
            if st.button("Pronounce (UK English)"):
                audio_file = generate_pronunciation(word)
                if audio_file:
                    autoplay_audio(audio_file)
            
            # Display the rest of the definition
            if remaining:
                st.markdown("**Pronunciation Reference:**" + remaining)
        else:
            st.error("Failed to get definition. Please try again.") 