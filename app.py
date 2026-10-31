
import streamlit as st
from deep_translator import MyMemoryTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translation Tool")
st.write("Translate text easily into different languages!")
st.divider()

languages = {
    "English": "en-US",
    "Hindi": "hi-IN",
    "Kannada": "kn-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Malayalam": "ml-IN",
    "French": "fr-FR",
    "Spanish": "es-ES",
    "German": "de-DE",
    "Japanese": "ja-JP"
}

# Verified greeting translations for reliable demonstration
greetings = {
    "good morning": {
        "Hindi": "सुप्रभात",
        "Kannada": "ಶುಭೋದಯ",
        "Tamil": "காலை வணக்கம்",
        "Telugu": "శుభోదయం",
        "Malayalam": "സുപ്രഭാതം",
        "French": "Bonjour",
        "Spanish": "Buenos días",
        "German": "Guten Morgen",
        "Japanese": "おはようございます"
    },
    "hello": {
        "Hindi": "नमस्ते",
        "Kannada": "ನಮಸ್ಕಾರ",
        "Tamil": "வணக்கம்",
        "Telugu": "నమస్కారం",
        "Malayalam": "നമസ്കാരം",
        "French": "Bonjour",
        "Spanish": "Hola",
        "German": "Hallo",
        "Japanese": "こんにちは"
    },
    "thank you": {
        "Hindi": "धन्यवाद",
        "Kannada": "ಧನ್ಯವಾದಗಳು",
        "Tamil": "நன்றி",
        "Telugu": "ధన్యవాదాలు",
        "Malayalam": "നന്ദി",
        "French": "Merci",
        "Spanish": "Gracias",
        "German": "Danke",
        "Japanese": "ありがとうございます"
    }
}

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=0
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter Text",
    placeholder="Type your text here...",
    height=150
)

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if st.button("🌐 Translate", use_container_width=True):

    st.session_state.translated_text = ""

    if not text.strip():
        st.warning("Please enter text to translate.")

    elif source == target:
        st.warning("Please select different languages.")

    else:
        try:
            cleaned_text = text.strip().lower()

            # Use verified greetings for English source
            if (
                source == "English"
                and cleaned_text in greetings
                and target in greetings[cleaned_text]
            ):
                translated = greetings[cleaned_text][target]

            else:
                with st.spinner("Translating..."):
                    translator = MyMemoryTranslator(
                        source=languages[source],
                        target=languages[target]
                    )

                    translated = translator.translate(text)

            st.session_state.translated_text = translated
            st.success("Translation completed successfully!")

        except Exception as e:
            st.error(f"Translation failed: {e}")

if st.session_state.translated_text:
    st.subheader("Translated Text")

    st.text_area(
        "Translation Result",
        value=st.session_state.translated_text,
        height=120
    )

    st.code(
        st.session_state.translated_text,
        language=None
    )

st.divider()
st.caption("CodeAlpha Internship | Language Translation Tool")
