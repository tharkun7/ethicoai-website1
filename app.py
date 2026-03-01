import streamlit as st
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="EthicoAI | Ethical AI Farming",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS for styling
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
    """, unsafe_allow_status=True)

# 2. Sidebar Navigation
st.sidebar.image("ethicoai_logo.jpg", use_container_width=True)
st.sidebar.title("EthicoAI Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Farm Memory", "Our Products"])

# 3. Home Page / Landing Page
if selection == "Home":
    # Header with Logo
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("ethicoai_logo.jpg", width=200)
    with col2:
        st.title("EthicoAI")
        st.subheader("Farming with Intelligence, Rooted in Ethics.")

    st.divider()

    # Who We Are Section (Your specific text)
    st.header("Who we are?")
    st.markdown(f"""
    <div class="ethical-card">
        <p style="font-size: 1.2rem; line-height: 1.6;">
            We are <strong>AI (Artificial Intelligence) powered co-operative ethical farming and Animal Husbandry company</strong>. 
            We provide compassion based animal and plant products to you.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Values Section
    st.write("##")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.success("### 🤖 AI Powered\nOptimizing health and yield without stress.")
    with col_b:
        st.success("### 🤝 Co-operative\nOwned by the community, for the community.")
    with col_c:
        st.success("### 💚 Compassion\nTreating every living being with dignity.")

# 4. Farm Memory Section (Placeholder for your memory.db)
elif selection == "Farm Memory":
    st.header("📜 Farm History & Memory")
    st.info("This section connects to your memory.db to show the transparent history of our farm.")
    # Here you would later add: 
    # df = pd.read_sql_query("SELECT * FROM history", sqlite3.connect('memory.db'))
    # st.dataframe(df)
    st.write("Coming soon: Real-time transparency logs.")

# 5. Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2026 EthicoAI Co-operative")
