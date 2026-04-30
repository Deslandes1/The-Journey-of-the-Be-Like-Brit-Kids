import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="The Journey of the Be Like Brit Kids – built by Gesner Deslandes",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- LANGUAGE STATE ----------
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ---------- UI TRANSLATIONS ----------
# (Your existing translations remain unchanged)
# ... (full translations code as in your original app.py) ...

def _(key):
    return ui_text[st.session_state.lang].get(key, key)

# ---------- CHAPTERS: ENGLISH ----------
chapters_en = [
    {
        "title": "Chapter 1: A New Beginning",
        "image": "YOUR_RAW_IMAGE_URL_HERE",  # <-- Replace with the direct image link from GitHub "Raw"
        "text": "The sun rose over the mountains of Grand‑Goâve, painting the sky in shades of orange and pink. Marie, a seven‑year‑old girl with bright eyes and braided hair, stood at the gate of Be Like Brit. She had arrived just the day before, scared and silent. Her parents had passed away, and she had no one left. But when she stepped inside, she was greeted by the warmest smiles. Mama Nerlande took her hand and said, 'You are home now, little one.' Marie looked around at the other children playing football and laughing. For the first time in weeks, she felt a tiny spark of hope. That night, she ate a hot meal and slept in a soft bed. In the morning, she woke to the sound of children singing. Marie smiled. Her new journey had begun.",
        "caption": "The gate of Be Like Brit in Grand‑Goâve"
    },
    # ... (the rest of your chapters, unchanged) ...
]

# ... (the rest of your app.py, unchanged) ...
