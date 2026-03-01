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

# 2. Custom CSS for Styling
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
        height: 100%;
    }
    .out-of-stock {
        color: #d9534f;
        font-weight: bold;
        font-size: 0.85rem;
        text-transform: uppercase;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
try:
    st.sidebar.image("ethicoai_logo.jpg", use_container_width=True)
except:
    pass

st.sidebar.title("EthicoAI Navigation")
# Using a radio selector which acts as your primary button navigation
selection = st.sidebar.radio("Go to:", [
    "Home", 
    "Shop Products from Goats", 
    "Shop Products from Poultry",
    "Farm History"
])

# 4. HOME SECTION
if selection == "Home":
    col1, col2 = st.columns([1, 4])
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

# 5. GOAT PRODUCTS SECTION
elif selection == "Shop Products from Goats":
    st.header("🐐 Goat Husbandry Products")
    try:
        st.image("durgivegan_goatfarm2.jpg", use_container_width=True, caption="Our No-Kill Goat Farm")
    except:
        st.warning("Landing image 'durgivegan_goatfarm2.jpg' not found.")

    goat_products = [
        {"name": "Goat Milk", "icon": "🥛"},
        {"name": "Goat Curd", "icon": "🥣"},
        {"name": "Goat Butter", "icon": "🧈"},
        {"name": "Goat Ghee", "icon": "🍯"},
        {"name": "Goat Paneer", "icon": "🧀"},
        {"name": "Goat Cheese", "icon": "🍕"}
    ]

    cols = st.columns(3)
    for i, p in enumerate(goat_products):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-box">
                <div style="font-size: 3rem;">{p['icon']}</div>
                <h4 style="margin: 10px 0;">{p['name']}</h4>
                <p class="out-of-stock">⚠️ Out of Stock</p>
            </div>
            """, unsafe_allow_html=True)
            st.write(" ")

# 6. POULTRY PRODUCTS SECTION
elif selection == "Shop Products from Poultry":
    st.header("🐔 Ethical Poultry Products")
    try:
        st.image("ethicoai_cock.png", use_container_width=True, caption="Compassion-based Poultry Care")
    except:
        st.warning("Landing image 'ethicoai_cock.png' not found.")

    poultry_products = [
        "Unfertilized chicken eggs",
        "Unfertilized chicken eggs (Desi)",
        "Unfertilized quail eggs",
        "Unfertilized turkey eggs",
        "Unfertilized Chinese Hen eggs",
        "Unfertilized Emu eggs",
        "Unfertilized Ostrich eggs"
    ]

    cols = st.columns(3)
    for i, name in enumerate(poultry_products):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-box">
                <div style="font-size: 3rem;">🥚</div>
                <h4 style="margin: 10px 0;">{name}</h4>
                <p class="out-of-stock">⚠️ Out of Stock</p>
            </div>
            """, unsafe_allow_html=True)
            st.write(" ")

# 7. FARM HISTORY (Database Bridge)
elif selection == "Farm History":
    st.header("📜 Farm History & Memory")
    try:
        conn = sqlite3.connect('memory.db')
        df = pd.read_sql_query("SELECT * FROM history ORDER BY timestamp DESC LIMIT 15", conn)
        st.dataframe(df, use_container_width=True)
        conn.close()
    except:
        st.info("Database connection active. No history logs found in 'memory.db' yet.")

st.sidebar.markdown("---")
st.sidebar.write("© 2026 EthicoAI Co-operative")
