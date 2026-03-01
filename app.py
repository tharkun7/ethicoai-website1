import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="EthicoAI | Ethical AI Farming",
    page_icon="🌱",
    layout="wide"
)

# 2. Custom CSS for a clean, ethical aesthetic
st.markdown("""
    <style>
    .main {
        background-color: #F4F7F2;
    }
    .stMarkdown h1 {
        color: #2D5A27;
    }
    .ethical-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #4A7c44;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .product-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #e0e0e0;
    }
    .out-of-stock {
        color: #d9534f;
        font-weight: bold;
        font-size: 0.85rem;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar with Logo
try:
    st.sidebar.image("ethicoai_logo.jpg", use_container_width=True)
except:
    st.sidebar.info("Upload 'ethicoai_logo.jpg' to show logo.")

st.sidebar.title("EthicoAI")
selection = st.sidebar.radio("Navigation", ["Home", "Shop Products", "Farm History"])

# 4. Home Page
if selection == "Home":
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("ethicoai_logo.jpg", width=150)
    with col2:
        st.title("EthicoAI")
        st.subheader("Farming with Intelligence, Rooted in Ethics.")

    st.divider()

    st.header("Who we are?")
    st.markdown("""
    <div class="ethical-card">
        <p style="font-size: 1.2rem; line-height: 1.6;">
            We are <strong>AI (Artificial Intelligence) powered co-operative ethical farming and Animal Husbandry company</strong>. 
            We provide compassion based animal and plant products to you.
        </p>
    </div>
    """, unsafe_allow_html=True)

# 5. Products Page
elif selection == "Shop Products":
    st.header("Our Ethical Products")
    
    # Hero Image of the Farm
    try:
        st.image("durgivegan_goatfarm2.png", use_container_width=True, caption="Our No-Kill Goat Farm")
    except:
        st.warning("Hero image 'durgivegan_goatfarm2.png' not found.")

    st.write("### Available Items")
    
    # Product List
    products = [
        {"name": "Goat Milk", "icon": "🥛"},
        {"name": "Goat Curd", "icon": "🥣"},
        {"name": "Goat Butter", "icon": "🧈"},
        {"name": "Goat Ghee", "icon": "🍯"},
        {"name": "Goat Paneer", "icon": "🧀"},
        {"name": "Goat Cheese", "icon": "🍕"}
    ]

    # Grid Display
    cols = st.columns(3)
    for i, p in enumerate(products):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-box">
                <div style="font-size: 3rem;">{p['icon']}</div>
                <h4 style="margin: 10px 0;">{p['name']}</h4>
                <p class="out-of-stock">⚠️ Out of Stock</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("") # Spacer

# 6. Farm History (Database Integration)
elif selection == "Farm History":
    st.header("📜 Farm History (memory.db)")
    try:
        conn = sqlite3.connect('memory.db')
        df = pd.read_sql_query("SELECT * FROM history ORDER BY timestamp DESC LIMIT 10", conn)
        st.dataframe(df, use_container_width=True)
        conn.close()
    except:
        st.info("Database connection active. No history logs found in 'memory.db' yet.")

st.sidebar.markdown("---")
st.sidebar.write("© 2026 EthicoAI Co-operative")
