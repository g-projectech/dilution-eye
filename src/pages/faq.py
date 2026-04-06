import streamlit as st
from translations import LANGUAGES, FAQ
from styles import applyCSS_styles

# 1- config
st.set_page_config(
    page_title="FAQ - Dilution Eye", 
    page_icon="👁️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

applyCSS_styles()

# 3 - language selector
if "selected_language" not in st.session_state:
    st.session_state["selected_language"] = list(LANGUAGES.keys())[0]

_, lang_col = st.columns([0.9, 0.1])
with lang_col:
    with st.popover("🌐"):
        sel_lang = st.radio(
            "Lang", 
            options=list(LANGUAGES.keys()), 
            index=list(LANGUAGES.keys()).index(st.session_state["selected_language"]),
            label_visibility="collapsed"
        )
        st.session_state["selected_language"] = sel_lang

texts = LANGUAGES[sel_lang]
faq_texts = FAQ[sel_lang]

# 4 - Home button
st.write("##")
col_empty1, col_button, col_empty2 = st.columns([7, 2, 7])
with col_button:
    st.page_link("app.py", label="Home", use_container_width=True)
st.write("##")

# 5 - page title
st.markdown(f"<h1 style='text-align: center; color: white;'>{faq_texts['title']}</h1>", unsafe_allow_html=True)
st.write("#")

# 6- FAQ generator
for i in range(1, 100):
    q_key = f"q{i}"
    a_key = f"a{i}"
    
    if q_key in faq_texts:
        with st.expander(f"**{faq_texts[q_key]}**"):
            st.write(faq_texts[a_key])

st.write("##")