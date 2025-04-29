import streamlit as st

# Page setup
st.set_page_config(page_title="🧼 Eraser Canvas Game", layout="centered")

# Grid settings
ROWS = 5
COLS = 5

# Session state
if "grid_colors" not in st.session_state:
    st.session_state.grid_colors = [["blue" for _ in range(COLS)] for _ in range(ROWS)]

# CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
    }

    .main-title {
        text-align: center;
        color: white;
        background: linear-gradient(135deg, #8e2de2, #4a00e0);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 10px;
        font-size: 32px;
    }

    .note {
        text-align: center;
        font-size: 16px;
        color: #555;
        margin-bottom: 25px;
    }

    .stButton>button {
        height: 45px;
        border-radius: 12px !important;
        background: #2980b9;
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        transition: 0.2s ease-in-out;
    }

    .stButton>button:hover {
        background: #1c5980;
        transform: scale(1.04);
        box-shadow: 0px 6px 14px rgba(0,0,0,0.15);
    }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>🎨 Eraser Canvas Game</div>", unsafe_allow_html=True)

# Note
st.markdown("<div class='note'>Click <b>once</b> on a blue box to erase it. Erased boxes disappear completely!</div>", unsafe_allow_html=True)

# Reset button
if st.button("🔄 Reset Canvas"):
    st.session_state.grid_colors = [["blue" for _ in range(COLS)] for _ in range(ROWS)]

# Draw the grid
for row in range(ROWS):
    cols = st.columns(COLS, gap="small")
    for col in range(COLS):
        color = st.session_state.grid_colors[row][col]
        if color == "blue":
            with cols[col]:
                if st.button(" ", key=f"{row}-{col}", use_container_width=True):
                    st.session_state.grid_colors[row][col] = "white"
