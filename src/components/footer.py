import streamlit as st


def footer_home():
    st.markdown("""
        <div style="
            margin-top:2rem;
            text-align:center;
            font-size:24px;
            font-weight:700;
            color:white;
        ">
            Crafted by <span style="color:#FFD700;">Annanth P Jose</span>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="
            margin-top:2rem;
            text-align:center;
            font-size:24px;
            font-weight:700;
            color:black;
        ">
            Crafted by <span style="color:#000000;">Annanth P Jose</span>
        </div>
    """, unsafe_allow_html=True)