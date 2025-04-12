import streamlit as st

# Set page config
st.set_page_config(page_title="🔄 Unit Converter", page_icon="📏", layout="centered")

# --- Styling ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f4f0ff;
    }
    h1 {
        text-align: center;
        color: #6C63FF;
        font-size: 50px;
        margin-bottom: 0.3em;
    }
    h2 {
        text-align: center;
        color: #4F4F4F;
        font-size: 30px;
        margin-bottom: 0.3em;
    }
    p {
        text-align: center;
        font-size: 20px;
        color: #444;
        margin-top: -10px;
    }
    .stSelectbox > div > div {
        cursor: pointer !important;
    }
          .stButton button {
        background-color: #6C63FF; 
        color: #ffffff;           
        font-weight: 600;
        padding: 12px 30px;
        font-size: 18px;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 12px rgba(108, 99, 255, 0.4);
        transition: 0.3s ease;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3); 
    }

    .stButton button:hover {
        background-color: #7d75ff;
        transform: scale(1.03);
    }



    .stNumberInput input {
        font-size: 18px;
        padding: 10px;
        border-radius: 6px;
    }
    .stSelectbox label, .stNumberInput label {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Intro ---
st.markdown("<h1>📏 Unit Converter App 🔄</h1>", unsafe_allow_html=True)
st.markdown("<h2>🧠 Your one-stop tool for smart & easy conversions!</h2>", unsafe_allow_html=True)
st.markdown("<p>✨ Convert 🔢 Length, ⚖️ Weight, 🌡️ Temperature, ⏱️ Time – all in one place!</p>", unsafe_allow_html=True)

# --- Unit Data ---
unit_data = {
    "📏 Length": {
        "units": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        "factors": {
            "Meter": 1,
            "Kilometer": 1000,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254
        }
    },
    "⚖️ Weight": {
        "units": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
        "factors": {
            "Kilogram": 1,
            "Gram": 0.001,
            "Milligram": 0.000001,
            "Pound": 0.453592,
            "Ounce": 0.0283495
        }
    },
    "⏱️ Time": {
        "units": ["Second", "Minute", "Hour", "Day", "Week"],
        "factors": {
            "Second": 1,
            "Minute": 60,
            "Hour": 3600,
            "Day": 86400,
            "Week": 604800
        }
    },
    "🌡️ Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
    }
}

# --- Select Category ---
category = st.selectbox("📂 Choose a category", list(unit_data.keys()))

# --- Unit Selection ---
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("🔁 From", unit_data[category]["units"])
with col2:
    to_unit = st.selectbox("➡️ To", unit_data[category]["units"])

# --- Value Input ---
value = st.number_input("🔢 Enter value", value=0.0, format="%.2f")

# --- Conversion Logic ---
def convert_units(cat, val, from_u, to_u):
    if from_u == to_u:
        return val
    if cat == "🌡️ Temperature":
        if from_u == "Celsius":
            return (val * 9/5 + 32) if to_u == "Fahrenheit" else (val + 273.15)
        elif from_u == "Fahrenheit":
            return (val - 32) * 5/9 if to_u == "Celsius" else ((val - 32) * 5/9 + 273.15)
        elif from_u == "Kelvin":
            return (val - 273.15) if to_u == "Celsius" else ((val - 273.15) * 9/5 + 32)
    else:
        base = unit_data[cat]["factors"][from_u]
        target = unit_data[cat]["factors"][to_u]
        return val * base / target

# --- Convert Button ---
if st.button("🚀 Convert Now"):
    if value == 0:
        st.warning("⚠️ Please enter a value greater than 0")
    else:
        result = convert_units(category, value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {round(result, 4)} {to_unit}")
