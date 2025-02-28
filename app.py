import streamlit as st
import base64

# --- Utility Functions ---
def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Custom CSS ---
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    /* Force all text to be white */
    * {
        font-family: 'Poppins', sans-serif;
        color: #ffffff !important;
    }

    /* Ensure text inside Streamlit elements is visible */
    .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCaption, .stExpander {
        color: #ffffff !important;
    }

    .stApp {
        background-color: #121212; /* Dark mode background */
        color: #ffffff !important;
    }

    .card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
    }

    .stButton > button {
        background: linear-gradient(135deg, #007bff, #0056b3);
        color: white;
        font-size: 16px;
        padding: 12px 30px;
        border-radius: 30px;
        border: none;
        transition: all 0.3s ease;
        width: 100%;
        position: relative;
        overflow: hidden;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 123, 255, 0.4);
    }

    h1, h2, h3 {
        text-align: center;
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }

    .logo {
        display: block;
        margin: 0 auto 20px;
        width: 200px;
        filter: drop-shadow(0 0 10px rgba(0, 123, 255, 0.5));
        animation: float 3s ease-in-out infinite;
    }

    .final-cost {
        font-size: 32px;
        font-weight: 700;
        color: #ffd700 !important;
        text-align: center;
        animation: glow 1.5s infinite alternate;
        padding: 20px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 15px;
        margin: 20px 0;
    }

    @keyframes glow {
        0% { text-shadow: 0 0 10px #ffd700; }
        100% { text-shadow: 0 0 20px #ffd700; }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .progress-bar {
        width: 100%;
        height: 10px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 5px;
        margin: 30px 0;
    }

    .progress {
        height: 100%;
        background: linear-gradient(90deg, #007bff, #00ff88);
        border-radius: 5px;
        transition: width 0.5s ease;
    }

    .option-label {
        font-size: 18px;
        font-weight: 600;
        margin: 15px 0;
        color: #ffffff !important;
    }

    .price-breakdown {
        background: rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }

</style>


"""

# --- Initialization ---
# [Keep the same session state initialization]
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'material' not in st.session_state:
    st.session_state.material = None
if 'jersey_type' not in st.session_state:
    st.session_state.jersey_type = None
if 'sleeve' not in st.session_state:
    st.session_state.sleeve = None
if 'collar' not in st.session_state:
    st.session_state.collar = None
if 'front_printing' not in st.session_state:
    st.session_state.front_printing = []
if 'back_printing' not in st.session_state:
    st.session_state.back_printing = []

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1
# --- Background & Logo ---
set_background("background.jpg")
st.image("jersey_placeholder.png", use_column_width=False, width=200)
st.title("🏆 Custom Jersey Designer")

# Add progress bar
progress = min((st.session_state.page - 1) * 25, 100)
st.markdown(f"""
<div class="progress-bar">
    <div class="progress" style="width: {progress}%"></div>
</div>
""", unsafe_allow_html=True)

# --- Page Content ---
if st.session_state.page == 1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Design Your Dream Jersey 🎨")
    st.markdown("""
    <div style='text-align: center; margin: 30px 0;'>
        <p style='font-size: 18px;'>
            Create a unique jersey that represents your team's spirit!<br>
            Start your customization journey below.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Start Designing →", on_click=next_page)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Step 2: Select Material 🌟")
    st.session_state.material = st.radio(
        "Choose your preferred material:", ["Micro PP", "DotKnit Honey Comb"],
        format_func=lambda x: f"🌟 {x}"
    )
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("← Previous", on_click=prev_page)
    with col2:
        st.button("Next →", on_click=next_page)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Step 3: Jersey Type 🧥")
    options = [
        "Single Colour Jersey",
        "Front Sublimation Jersey",
        "Bothside Sublimation Jersey",
        "Bothside with Sleeve Sublimation",
    ]
    st.session_state.jersey_type = st.radio(
        "Choose the type of jersey:",
        options,
        format_func=lambda x: f"🔥 {x}"
    )
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("← Previous", on_click=prev_page)
    with col2:
        st.button("Next →", on_click=next_page)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Step 4: Customization Options ✨")
    
    # Common Options
    st.session_state.sleeve = st.selectbox("Select Sleeve", ["Half", "Long", "Ribs"])
    st.session_state.collar = st.selectbox("Select Collar", ["Normal Collar", "Chinese Collar", "Round"])
    
    # Printing Options
    st.session_state.front_printing = st.multiselect(
        "Select Front Printing", ["Logo (Left & Right)", "Name (Below Chest)"]
    )
    st.session_state.back_printing = st.multiselect(
        "Select Back Printing", ["Team Name", "Player Name", "Number"]
    )
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("← Previous", on_click=prev_page)
    with col2:
        st.button("Next →", on_click=next_page)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 5:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🎉 Final Price Estimate")
    
    # Pricing Calculation
    st.markdown("### Price Breakdown")
    st.markdown("<div class='price-breakdown'>", unsafe_allow_html=True)
    
    base_price = 170
    pricing = [
        ("Base Price", 170),
        ("Jersey Type", {
            "Single Colour Jersey": 0,
            "Front Sublimation Jersey": 100,
            "Bothside Sublimation Jersey": 150,
            "Bothside with Sleeve Sublimation": 200,
        }[st.session_state.jersey_type]),
        ("Sleeve Type", {
            "Half": 0, "Long": 30, "Ribs": 20
        }[st.session_state.sleeve]),
        ("Collar Type", {
            "Normal Collar": 0, "Chinese Collar": 40, "Round": 30
        }[st.session_state.collar]),
        ("Front Printing", sum([50 if "Logo" in p else 30 for p in st.session_state.front_printing])),
        ("Back Printing", sum([40 if "Team" in p else 50 if "Player" in p else 20 for p in st.session_state.back_printing]))
    ]
    
    for item, price in pricing:
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; margin: 10px 0;">
            <span>{item}</span>
            <span>+ Rs. {price}</span>
        </div>
        """, unsafe_allow_html=True)
    
    total = sum(p[1] for p in pricing)
    st.markdown(f"""
    <div style="border-top: 2px solid #ffffff; margin: 20px 0; padding: 10px 0;">
        <div style="display: flex; justify-content: space-between; font-weight: bold;">
            <span>Price per Jersey</span>
            <span>Rs. {total}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # End price-breakdown
    
    quantity = st.selectbox("Select Quantity:", ["10pcs", "20pcs", "50pcs", "100pcs+"])
    total_cost = total * {
        "10pcs": 10, "20pcs": 20, "50pcs": 50, "100pcs+": 100
    }[quantity]
    
    st.markdown(f"<div class='final-cost'>Total: Rs. {total_cost:,.2f}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("← Previous", on_click=prev_page)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Confetti Animation
    st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js"></script>
    <script>
        confetti({
            particleCount: 150,
            spread: 100,
            origin: { y: 0.6 },
            colors: ['#ff0000', '#00ff00', '#0000ff']
        });
    </script>
    """, unsafe_allow_html=True)

st.markdown(custom_css, unsafe_allow_html=True)

# Hide Streamlit branding and footer
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)