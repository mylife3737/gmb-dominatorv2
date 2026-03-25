import streamlit as st
import anthropic
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import io
import requests
import json
from datetime import datetime

# PAGE CONFIG
st.set_page_config(
    page_title="GMB Dominator",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background-color: #0a0a0f; color: #e8e4dc; }
.gmb-hero h1 { font-family: 'Syne', sans-serif; font-size: 3.2rem; background: linear-gradient(135deg, #ff6b00, #ffd000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.gate-card { background: #13131a; border: 1px solid #2a2a3a; border-radius: 16px; padding: 2rem; margin: 2rem auto; max-width: 480px; }
.stButton > button { background: linear-gradient(135deg, #ff6b00, #ff9500) !important; color: white !important; border: none !important; width: 100%; }
</style>
""", unsafe_allow_html=True)

ACCESS_CODE = "GROW2026"

# SESSION STATE
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# HERO
st.markdown('<div class="gmb-hero"><h1>GMB DOMINATOR</h1><p>Rank #1 on Google Maps</p></div>', unsafe_allow_html=True)

# AUTHENTICATION GATE
if not st.session_state.authenticated:
    with st.container():
        st.markdown('<div class="gate-card">', unsafe_allow_html=True)
        st.subheader("🔐 Enter Access Code")
        user_code = st.text_input("Code", type="password")
        if st.button("Unlock App →"):
            if user_code.strip().upper() == ACCESS_CODE:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid Code")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# MAIN APP CONTENT
st.title("🚀 Welcome, GMB Dominator")
st.write("Your app is officially live and connected.")
