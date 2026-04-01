import streamlit as st
import plotly.express as px
from dilution_logic import DilutionDetector
from translations import LANGUAGES, FAQ
import base64
import os

# 1 - config
st.set_page_config(
    page_title="Dilution Eye", 
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2 - CSS
st.markdown("""
    <style>
    header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0%;
    }
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    
    [data-testid="stSidebarNav"], 
    [data-testid="stSidebar"], 
    [data-testid="collapsedControl"] {
        display: none !important;
    }

    footer { visibility: hidden; }
    [data-testid="stStatusWidget"] { visibility: hidden; }
    .stMarkdown h1 a, .stMarkdown h2 a { display: none !important; }

    [data-testid="stMetric"] {
        background-color: #1E1E1E !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid #333 !important;
    }
    
    .header-container {
        background-color: #0E1117;
        padding: 40px 20px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 25px;
    }
            
    input::placeholder { color: #A0AEC0 !important; transition: color 0.3s ease; }
    input:focus::placeholder { color: transparent !important; }

    .main-footer {
        background-color: #0E1117;
        padding: 40px;
        border-radius: 20px;
        margin-top: 50px;
        margin-bottom: 30px;
        text-align: center;
        border: 1px solid #333;
    }
    
    .btc-address {
        background-color: #1E1E1E;
        color: #F7931A;
        padding: 12px 20px;
        border-radius: 10px;
        font-family: monospace;
        font-size: 14px;
        border: 1px dashed #F7931A;
        display: inline-block;
        margin-top: 10px;
        cursor: pointer;
        transition: all 0.3s;
        word-break: break-all;
    }
    .btc-address:hover {
        background-color: #262626;
        transform: scale(1.05);
    }

    @media (max-width: 768px) {
        .header-text-h1 { font-size: 38px !important; }
        div[data-testid="stPopover"] { margin-top: 10px !important; }
    }
            
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    [data-testid="stMetric"], .stPlotlyChart, [data-testid="stVerticalBlock"] > div {
        animation: fadeIn 0.8s ease-out forwards;
    }
            
    /* FAQ button */
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

    /* Hover effect */
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

# 4 - HEADER
st.markdown(f"""
    <div class="header-container">
        <h1 class="header-text-h1" style="color: white; margin: 0; font-size: 60px; letter-spacing: 2px; font-weight: bold;">
            {texts["title"]}
        </h1>
        <p style="color: #A0AEC0; font-size: 20px; margin-top: 10px;">
            {texts["tagline"]}
        </p>
    </div>
    """, unsafe_allow_html=True)

# 5 - research area
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    query = st.text_input(texts["input_label"], placeholder=texts["input_placeholder"]).upper()
    btn = st.button(texts["btn_analyze"], type="primary", use_container_width=True)

st.write("##")

# 6 - logic analysis 
if btn:
    # 1 - if the search bar is empty
    if not query.strip():
        st.warning(texts['error_empty'])
    
    # 2 - if there is text
    else:
        with st.spinner(texts['loading_after_research']):
            detector = DilutionDetector(query)
            
            # let's try downloading data
            if detector.fetch_and_normalize_shares() and detector.calculate_dilution_metrics():
                # KPI (key performance indicator)
                m1, m2, m3 = st.columns(3)
                last_var = detector.yearly_dilution_pct.iloc[-1]
                tot_shares = detector.shares_data['Adjusted_Shares'].iloc[-1]
                
                # status definition
                if last_var <= 0: 
                    status = "POSITIVE 🟢"
                elif 0 < last_var <= 5: 
                    status = "STABLE ⚪"
                elif 5 < last_var <= 10: 
                    status = "WARNING 🟡"
                else: 
                    status = "DILUTING 🚩"

                m1.metric(texts["kpi_shares"], f"{tot_shares:,.0f}")
                m2.metric(texts["kpi_change"], f"{last_var:.2f}%", delta=f"{last_var:.2f}%", delta_color="inverse")
                m3.metric(texts["kpi_status"], status)

                st.write("###")

                # slipt the page
                col_left, col_right = st.columns([0.65, 0.35])
                
                with col_left:
                    st.subheader(texts["chart_title"])
                    # In app.py, sostituisci la riga px.area con questa:
                    fig = px.area(
                        x=detector.shares_data.index, 
                        y=detector.shares_data['Adjusted_Shares'],
                        labels={'x': texts['date'], 'y': texts['kpi_shares']} # Usa la traduzione già pronta!
                    )
                    
                    # chart
                    fig.update_layout(
                        template="plotly_dark", 
                        margin=dict(l=0, r=0, t=10, b=0),
                        dragmode=False
                    )
                    
                    # chart
                    st.plotly_chart(
                        fig, 
                        use_container_width=True,
                        config={
                            'scrollZoom': False, 
                            'displayModeBar': False
                        }
                    )
                    
                with col_right:
                    st.subheader(texts["alert_title"])
                    with st.container(height=450):
                        for alert in detector.alerts[::-1]:
                            if "🚩" in alert or "🚨" in alert: st.error(alert)
                            elif "⚠️" in alert: st.warning(alert)
                            elif "🟢" in alert: st.success(alert)
                            else: st.info(alert)
            else:
                # yfinance can't find anything
                st.error(texts["error_not_found"])

# 7 - link FAQ
st.write("##")
col_vuota1, col_bottone, col_vuota2 = st.columns([9, 2, 9])
with col_bottone:
    st.page_link("pages/faq.py", label=faq_texts["title"], use_container_width=True)
st.write("##")

# 8 - footer
ADDRESS_BTC = "bc1q2a2ajtq685lz8rxxcun98x2a8dk9xcwmq79g7s"

st.markdown(f"""
    <div class="main-footer">
        <p style="color: white; font-weight: bold; font-size: 20px; margin-bottom: 5px;">
            {texts["donate_title"]} ₿
        </p>
        <p style="color: #A0AEC0; font-size: 14px; margin-bottom: 15px;">
            {texts["donate_sub"]}
        </p>
        <div class="btc-address" id="btc-box" onclick="copyAddress()">
            <span id="addr-text">{ADDRESS_BTC}</span>
        </div>
        <script>
        function copyAddress() {{
            const addr = "{ADDRESS_BTC}";
            navigator.clipboard.writeText(addr).then(function() {{
                const box = document.getElementById('btc-box');
                const text = document.getElementById('addr-text');
                const originalText = text.innerText;
                text.innerText = "{texts['address_copied']}";
                box.style.borderColor = "#4BB543";
                box.style.color = "#4BB543";
                setTimeout(function() {{
                    text.innerText = originalText;
                    box.style.borderColor = "#F7931A";
                    box.style.color = "#F7931A";
                }}, 2000);
            }});
        }}
        </script>
        <div style="margin-top: 30px; color: #666; font-size: 12px; max-width: 800px; margin-left: auto; margin-right: auto;">
            {texts["footer_disclaimer"]}
        </div>
        <p style="color: #444; font-size: 10px; margin-top: 20px;">
            © 2026 Dilution Eye - All Rights Reserved
        </p>
    </div>
    """, unsafe_allow_html=True)