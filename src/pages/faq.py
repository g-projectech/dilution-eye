import streamlit as st
from translations import LANGUAGES, FAQ

# 1- config
st.set_page_config(
    page_title="FAQ - Dilution Eye", 
    page_icon="👁️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2 - CSS
st.markdown("""
    <style>   
    [data-testid="stHeaderActionElements"] { 
        display: none !important; 
    }
    
    header[data-testid="stHeader"] { 
        visibility: hidden !important;
        height: 0% !important;
    }
    
    [data-testid="stSidebarNav"], 
    [data-testid="stSidebar"], 
    [data-testid="collapsedControl"] { 
        display: none !important; 
    }
    
    footer { 
        visibility: hidden !important; 
    }

    /* home button */
    [data-testid="stPageLink-NavLink"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        background-color: #1E1E1E !important; 
        border: 1px solid #FF7676 !important;
        border-radius: 12px !important; 
        padding: 10px 0px !important; 
        transition: all 0.3s ease !important; 
    }
    [data-testid="stPageLink-NavLink"] p {
        flex: none !important; 
        margin: 0 !important;
        font-weight: bold !important;
    }
    [data-testid="stPageLink-NavLink"]:hover {
        background-color: #262626 !important; 
        border-color: #FF4B4B !important;
        transform: scale(1.05) !important; 
    }
    </style>
    """, unsafe_allow_html=True)

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
for i in range(1, 10):
    q_key = f"q{i}"
    a_key = f"a{i}"
    
    if q_key in faq_texts:
        with st.expander(f"**{faq_texts[q_key]}**"):
            st.write(faq_texts[a_key])

st.write("##")