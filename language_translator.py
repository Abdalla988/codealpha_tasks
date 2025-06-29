import streamlit as st
from googletrans import Translator, LANGUAGES

# Set up the Streamlit app
st.set_page_config(page_title="AI Language Translator", layout="centered")
st.title("🌍 Language Translation Tool")

# Create translator instance
translator = Translator()

# Show text input box
input_text = st.text_area("Enter text to translate:")

# Language dropdowns
lang_list = sorted(LANGUAGES.values())  # safer for dropdowns
lang_codes = {v: k for k, v in LANGUAGES.items()}

# Handle case if index throws an error due to string mismatch
default_src = lang_list.index("english") if "english" in lang_list else 0
default_tgt = lang_list.index("french") if "french" in lang_list else 1

source_lang = st.selectbox("From (Source Language):", lang_list, index=default_src)
target_lang = st.selectbox("To (Target Language):", lang_list, index=default_tgt)


# Translate button
if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter text.")
    else:
        src = lang_codes[source_lang]
        tgt = lang_codes[target_lang]
        try:
            translated = translator.translate(input_text, src=src, dest=tgt)
            st.success("Translation:")
            st.write(f"**{translated.text}**")
        except Exception as e:
            st.error(f"Error: {e}")
