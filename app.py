import streamlit as st
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="EthicoAI | Ethical AI Farming",
    page_icon="🌱",
    layout="wide"
)

# 2. Advanced CSS for "Pop" and Prominent UI
st.markdown("""
    <style>
    /* Background and Main Font */
    .main {
        background-color: #F8FAF7;
    }
    
    /* Navigation Button Styling */
    div[data-testid="stSidebarNav"] {
        padding-top: 2rem;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #1B3F17 !important;
        font-family: 'Trebuchet MS', sans-serif;
    }

    /* Prominent Info Cards */
    .ethical-card {
        background: linear-gradient(135deg, #ffffff 0%, #f0f9f0 100%);
        padding: 30px;
        border-radius: 20px;
        border-left: 8px solid #4A7c44;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }

    /* Product Box "Pop" Effect */
    .product-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        border: 1px solid #e0e0e0;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .product-box:hover {
        transform: translateY(-5px);
        border-color: #4A7c44;
    }

    /* Out of Stock Badge */
    .out-of-stock {
        color: #ffffff;
        background-color: #CC3333;
        font-weight: bold;
        font-size: 0.75rem;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 50px;
        margin-top: 15px;
    }
    
    /* Category Header Styles */
    .category-header {
        background-color: #2D5A27;
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation (Prominent Radio Buttons)
with st.sidebar:
    try:
        st.image("ethicoai_logo.jpg", use_container_width=True)
    except:
        st.title("EthicoAI")
    
    st.markdown("### 🌾 Marketplace")
    selection = st.radio(
        "Select Department:",
        ["🏠 Home", "🐐 Shop Goat Products", "🐔 Shop Poultry Products", "🐟 Shop Organic Fertilizer"],
        index=0
    )
    st.markdown("---")
    st.write("© 2026 EthicoAI Co-operative")

# 4. HOME SECTION
if "🏠 Home" in selection:
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("ethicoai_logo.jpg", width=180)
    with col2:
        st.title("EthicoAI")
        st.subheader("Farming with Intelligence, Rooted in Ethics.")

    st.divider()
    st.markdown("""
    <div class="ethical-card">
        <h2 style="margin-top:0;">Who we are?</h2>
        <p style="font-size: 1.3rem; line-height: 1.7; color: #2D3E2B;">
            We are an <strong>AI (Artificial Intelligence) powered co-operative ethical farming and Animal Husbandry company</strong>. 
            We provide <strong>compassion based animal and plant products</strong> to you.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Value Props
    c1, c2, c3 = st.columns(3)
    c1.metric("Model", "Co-operative")
    c2.metric("Intelligence", "AI-Powered")
    c3.metric("Ethics", "Compassion-Based")

# 5. GOAT PRODUCTS SECTION
elif "🐐 Shop Goat Products" in selection:
    st.markdown('<div class="category-header"><h1>Goat Husbandry Shop</h1></div>', unsafe_allow_html=True)
    try:
        st.image("durgivegan_goatfarm2.jpg", use_container_width=True)
    except:
        st.warning("Landing image 'durgivegan_goatfarm2.jpg' not found.")

    goat_items = [
        {"n": "Goat Milk", "i": "🥛"}, {"n": "Goat Curd", "i": "🥣"},
        {"n": "Goat Butter", "i": "🧈"}, {"n": "Goat Ghee", "i": "🍯"},
        {"n": "Goat Paneer", "i": "🧀"}, {"n": "Goat Cheese", "i": "🍕"}
    ]

    cols = st.columns(3)
    for idx, item in enumerate(goat_items):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="product-box">
                <div style="font-size: 3.5rem;">{item['i']}</div>
                <h4 style="margin: 10px 0;">{item['n']}</h4>
                <div class="out-of-stock">Out of Stock</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

# 6. POULTRY PRODUCTS SECTION
elif "🐔 Shop Poultry Products" in selection:
    st.markdown('<div class="category-header"><h1>Ethical Poultry Shop</h1></div>', unsafe_allow_html=True)
    try:
        st.image("ethicoai_cock.png", use_container_width=True)
    except:
        st.warning("Landing image 'ethicoai_cock.png' not found.")

    poultry_items = [
        "Unfertilized chicken eggs", "Unfertilized chicken eggs (Desi)", 
        "Unfertilized quail eggs", "Unfertilized turkey eggs", 
        "Unfertilized Chinese Hen eggs", "Unfertilized Emu eggs", 
        "Unfertilized Ostrich eggs", "Unfertilized duck eggs", 
        "Unfertilized goose eggs"
    ]

    cols = st.columns(3)
    for idx, name in enumerate(poultry_items):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="product-box">
                <div style="font-size: 3.5rem;">🥚</div>
                <h4 style="margin: 10px 0;">{name}</h4>
                <div class="out-of-stock">Out of Stock</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

# 7. ORGANIC FERTILIZER SECTION
elif "🐟 Shop Organic Fertilizer" in selection:
    st.markdown('<div class="category-header"><h1>Organic Fertilizer Shop</h1></div>', unsafe_allow_html=True)
    try:
        st.image("ethicoai_fish.png", use_container_width=True)
    except:
        st.warning("Landing image 'ethicoai_fish.png' not found.")

    fert_items = [
        {"n": "Organic Fish Manure Liquid Serum", "i": "🧪"},
        {"n": "Organic Goat Derived Fertilizer", "i": "🌿"},
        {"n": "Organic Poultry Derived Fertilizer", "i": "🍂"},
        {"n": "Organic Pig Derived Fertilizer", "i": "♻️"},
        {"n": "Organic Cow Derived Fertilizer", "i": "🚜"}
    ]

    cols = st.columns(3)
    for idx, item in enumerate(fert_items):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="product-box">
                <div style="font-size: 3.5rem;">{item['i']}</div>
                <h4 style="margin: 10px 0;">{item['n']}</h4>
                <div class="out-of-stock">Out of Stock</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
