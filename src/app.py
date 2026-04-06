import streamlit as st
import plotly.express as px
from dilution_logic import DilutionDetector
from translations import LANGUAGES, FAQ
from styles import applyCSS_styles
import base64
import os
import logging

# basic configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# 1 - config
st.set_page_config(
    page_title="Dilution Eye", 
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
    query = st.text_input(texts["input_label"],
    placeholder=texts["input_placeholder"],
    max_chars=12  # Limita l'input fisico a 12 caratteri
    ).upper()
    btn = st.button(texts["btn_analyze"], type="primary", width="stretch")

st.write("##")

# 6 - logic analysis 
if btn:
    # 1 - se la barra di ricerca è vuota
    if not query.strip():
        st.warning(texts['error_empty'])
    
    # 2 - se c'è del testo
    else:
        with st.spinner(texts['loading_after_research']):
            log_ticker = query.strip().upper()[:12]
            logger.info(f"Ricerca avviata per: {log_ticker}")
            
            try:
                # is ISIN is correct
                detector = DilutionDetector(query)
                
                if detector.fetch_and_normalize_shares() and detector.calculate_dilution_metrics():
                    
                    # company's name
                    try:
                        company_info = detector.ticker.info
                        company_name = company_info.get('longName') or company_info.get('shortName') or query.upper()
                    except Exception:
                        company_name = query.upper()
                    
                    # UI result
                    st.markdown(f"<h2 style='text-align: center; color: white;'>{company_name}</h2>", unsafe_allow_html=True)
                    st.markdown("<hr style='border: 1px solid #333;'>", unsafe_allow_html=True)

                    # KPI
                    m1, m2, m3 = st.columns(3)
                    last_var = detector.yearly_dilution_pct.iloc[-1]
                    tot_shares = detector.shares_data['Adjusted_Shares'].iloc[-1]
                    
                    if last_var <= 0: status = "POSITIVE 🟢"
                    elif 0 < last_var <= 5: status = "STABLE ⚪"
                    elif 5 < last_var <= 10: status = "WARNING 🟡"
                    else: status = "DILUTING 🚩"

                    m1.metric(texts["kpi_shares"], f"{tot_shares:,.0f}")
                    m2.metric(texts["kpi_change"], f"{last_var:.2f}%", delta=f"{last_var:.2f}%", delta_color="inverse")
                    m3.metric(texts["kpi_status"], status)

                    # chart and alert
                    col_left, col_right = st.columns([0.65, 0.35])
                    with col_left:
                        st.subheader(f"{texts['chart_title']}")
                        fig = px.area(x=detector.shares_data.index, y=detector.shares_data['Adjusted_Shares'])
                        fig.update_layout(template="plotly_dark", margin=dict(l=0, r=0, t=10, b=0))
                        st.plotly_chart(fig, width="stretch")
                        
                    with col_right:
                        st.subheader(f"{texts['alert_title']}")
                        with st.container(height=450):
                            for alert in detector.alerts[::-1]:
                                if "🚩" in alert or "🚨" in alert: st.error(alert)
                                elif "⚠️" in alert: st.warning(alert)
                                elif "🟢" in alert: st.success(alert)
                                else: st.info(alert)
                else:
                    # valid ticker but no data (yf)
                    st.error(texts["error_not_found"])

            except ValueError as e:
                # catch Invalid ISIN
                logger.error(f"Validazione fallita per {log_ticker}: {e}")
                st.error(texts["error_not_found"])
                
            except Exception as e:
                # other errors
                logger.error(f"Errore imprevisto su {log_ticker}: {e}")
                st.error(texts["error_not_found"])

# 7 - link FAQ
st.write("##")
col_vuota1, col_bottone, col_vuota2 = st.columns([9, 2, 9])
with col_bottone:
    st.page_link("pages/faq.py", label=faq_texts["title"], width="stretch")
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