import streamlit as st

def applyCSS_styles():
    st.markdown("""
        <style>
        /* reset global UI */
        header[data-testid="stHeader"], 
        [data-testid="stSidebarNav"], 
        [data-testid="stSidebar"], 
        [data-testid="collapsedControl"],
        [data-testid="stHeaderActionElements"],
        footer { 
            visibility: hidden !important;
            height: 0% !important;
            display: none !important;
        }
        
        [data-testid="stStatusWidget"] { visibility: hidden; }
        .stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h3 a { display: none !important; }

        [data-testid="stMetric"] {
            background-color: #1E1E1E !important;
            padding: 20px !important;
            border-radius: 12px !important;
            border: 1px solid #333 !important;
        }

        [data-testid="stMetric"] label, 
        [data-testid="stMetricValue"], 
        [data-testid="stMetricDelta"] div {
            color: white !important;
        }

        /* header & footer personalized */
        .header-container {
            background-color: #0E1117;
            padding: 40px 20px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 25px;
        }
        
        .main-footer {
            background-color: #0E1117;
            padding: 40px;
            border-radius: 20px;
            margin-top: 50px;
            margin-bottom: 30px;
            text-align: center;
            border: 1px solid #333;
            color: white !important;
        }

        /* input search bar */
        input::placeholder { color: #A0AEC0 !important; }
        input:focus::placeholder { color: transparent !important; }

        /* bitcoin donation */
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

        /* navigation bottons (HOME and Faq) */
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
        [data-testid="stPageLink-NavLink"]:hover {
            background-color: #262626 !important; 
            border-color: #FF4B4B !important; 
            transform: scale(1.05) !important; 
        }
        [data-testid="stPageLink-NavLink"] p {
            color: white !important;
            font-weight: bold !important;
            margin: 0 !important;
        }

        /* animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        [data-testid="stMetric"], .stPlotlyChart, [data-testid="stVerticalBlock"] > div {
            animation: fadeIn 0.8s ease-out forwards;
        }

        @media (max-width: 768px) {
            .header-text-h1 { font-size: 38px !important; }
        }
        </style>
    """, unsafe_allow_html=True)