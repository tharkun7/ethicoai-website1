import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="EthicoAI | Ethical AI Farming",
    page_icon="🌱",
    layout="wide"
)

# 2. Custom CSS (Corrected the argument name here)
st.markdown("""
    <style>
    .main {
        background-color: #F4F7F2;
    }
    .stMarkdown h1 {
        color: #2D5A27;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .ethical-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #4A7c44;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True) # Changed from unsafe_allow_status

# 3. Sidebar Navigation
try:
    st.sidebar.image("ethicoai_logo.jpg", use_container_width=True)
except:
    st.sidebar.warning("Logo file not found. Please ensure 'ethicoai_logo.jpg' is in the same folder.")

st.sidebar.title("EthicoAI Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Farm Memory", "Our Products"])

# 4. Home Page
if selection == "Home":
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            st.image("ethicoai_logo.jpg", width=200)
        except:
            st.write("Logo Placeholder")
    with col2:
        st.title("EthicoAI")
        st.subheader("Farming with Intelligence, Rooted in Ethics.")

    st.divider()

    st.header("Who we are?")
    # Corrected the argument here as well
    st.markdown("""
    <div class="ethical-card">
        <p style="font-size: 1.2rem; line-height: 1.6;">
            We are <strong>AI (Artificial Intelligence) powered co-operative ethical farming and Animal Husbandry company</strong>. 
            We provide compassion based animal and plant products to you.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("##")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.success("### 🤖 AI Powered\nOptimizing health and yield without stress.")
    with col_b:
        st.success("### 🤝 Co-operative\nOwned by the community.")
    with col_c:
        st.success("### 💚 Compassion\nTreating every living being with dignity.")

elif selection == "Farm Memory":
    st.header("📜 Farm History & Memory")
    st.info("This section will connect to your memory.db.")

st.sidebar.markdown("---")
st.sidebar.write("© 2026 EthicoAI Co-operative")
