import streamlit as st
import hashlib
import json
import os
from cryptography.fernet import Fernet
import time

# Set page config first to define app title and layout
st.set_page_config(page_title="Secure Data Encryption System", layout="centered", page_icon="🛡️")

# Custom CSS for a vibrant, clean UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    body {
        background: linear-gradient(135deg, #e0e7ff, #dbeafe);
        font-family: 'Poppins', sans-serif;
    }
    .container {
        max-width: 800px;
        margin: auto;
        padding: 2rem;
    }
    .title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card {
        background: #ffffff;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        margin-bottom: 1.5rem;
        border: 1px solid #e0e7ff;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .btn-primary {
        background: linear-gradient(90deg, #0d9488, #22d3ee);
        color: white;
        padding: 0.8rem 3rem;
        border-radius: 0.5rem;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        text-align: center;
    }
    .btn-primary:hover {
        background: linear-gradient(90deg, #0f766e, #06b6d4);
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .error {
        color: #b91c1c;
        font-size: 0.95rem;
        font-weight: 500;
        margin-top: 0.75rem;
        background: #fee2e2;
        padding: 0.5rem;
        border-radius: 0.25rem;
    }
    .success {
        color: #15803d;
        font-size: 0.95rem;
        font-weight: 500;
        margin-top: 0.75rem;
        background: #dcfce7;
        padding: 0.5rem;
        border-radius: 0.25rem;
    }
    .input-field {
        border: 2px solid #d1d5db;
        border-radius: 0.5rem;
        padding: 0.8rem;
        width: 100%;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: #f9fafb;
    }
    .input-field:focus {
        outline: none;
        border-color: #0d9488;
        box-shadow: 0 0 0 4px rgba(13, 148, 136, 0.1);
        background: #ffffff;
    }
    .sidebar .stRadio > div {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    .sidebar .stRadio > div label {
        color: #1e3a8a;
        font-weight: 600;
        font-size: 1.1rem;
    }
    .code-block {
        background: #f1f5f9;
        border-radius: 0.5rem;
        padding: 1rem;
        font-family: 'Fira Code', monospace;
        font-size: 0.9rem;
        color: #1e3a8a;
        border: 1px solid #d1d5db;
        word-break: break-all;
    }
    .stTextArea textarea, .stTextInput input {
        border-radius: 0.5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load or generate encryption key for Fernet
KEY_FILE = "secret.key"
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        KEY = f.read()
else:
    KEY = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(KEY)

cipher = Fernet(KEY)

# Load or initialize data storage
DATA_FILE = "data.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_data = json.load(f)
else:
    stored_data = {}

# Initialize session state for tracking attempts and navigation
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Hash the passkey using SHA-256
def hash_passkey(passkey):
    return hashlib.sha256(passkey.strip().encode()).hexdigest()

# Encrypt data using Fernet
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt data with passkey verification
def decrypt_data(encrypted_text, passkey):
    # Strip whitespace from inputs to avoid mismatches
    encrypted_text = encrypted_text.strip()
    hashed_passkey = hash_passkey(passkey)
    
    # Check if encrypted text exists in stored data
    if encrypted_text in stored_data:
        if stored_data[encrypted_text]["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
        else:
            st.session_state.failed_attempts += 1
            return None
    st.session_state.failed_attempts += 1
    return None

# Save encrypted data to JSON file
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(stored_data, f)

# Main UI
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🛡️ Secure Data Encryption System</h1>', unsafe_allow_html=True)

# Sidebar navigation
menu = ["🏠 Home", "📥 Store Data", "🔍 Retrieve Data", "🔐 Login"]
choice = st.sidebar.radio("🌟 Navigate", menu, key="nav")
st.session_state.current_page = choice.lstrip("🏠📥🔍🔐 ").strip()

if choice == "🏠 Home":
    st.markdown("""
        <div class="card">
            <h2 class="text-2xl font-bold text-indigo-900 mb-4">🏠 Welcome to Secure Data Encryption System 🌟</h2>
            <p class="text-gray-700">🔒 Safeguard your sensitive information with our advanced encryption system.</p>
            <p class="text-gray-700 mt-2">🚀 Use the sidebar to securely store or retrieve your data with a unique passkey.</p>
        </div>
    """, unsafe_allow_html=True)

elif choice == "📥 Store Data":
    st.markdown('<div class="card"><h2 class="text-2xl font-bold text-indigo-900 mb-4">📥 Store New Data 🔐</h2>', unsafe_allow_html=True)
    user_data = st.text_area("📝 Enter your data:", placeholder="Type your sensitive data here... ✍️", key="store_data", help="Enter the data you want to encrypt securely 🔒")
    passkey = st.text_input("🔑 Enter a secure passkey:", type="password", placeholder="Choose a strong passkey 🔐", key="store_passkey", help="This passkey will be required to decrypt your data 🔓")
    st.markdown('<style>.stTextArea textarea, .stTextInput input { @extend .input-field; }</style>', unsafe_allow_html=True)
    
    if st.button("🔒 Encrypt & Store", key="store_btn", help="Click to encrypt and store your data 📂"):
        if user_data and passkey:
            encrypted = encrypt_data(user_data)
            stored_data[encrypted] = {"encrypted_text": encrypted, "passkey": hash_passkey(passkey)}
            save_data()
            st.markdown(f'<p class="success">✅ Your data has been encrypted and stored securely! 🎉</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="code-block">{encrypted}</div>', unsafe_allow_html=True)  # Removed 📜 emoji
        else:
            st.markdown(f'<p class="error">⚠️ Please fill out both fields! 🚨</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif choice == "🔍 Retrieve Data":
    if st.session_state.failed_attempts >= 3:
        st.markdown(f'<div class="card"><p class="error">🚫 Too many failed attempts. Please login to continue. 🔐</p></div>', unsafe_allow_html=True)
        st.session_state.current_page = "Login"
        st.rerun()

    st.markdown('<div class="card"><h2 class="text-2xl font-bold text-indigo-900 mb-4">🔍 Retrieve Encrypted Data 🔓</h2>', unsafe_allow_html=True)
    encrypted_text = st.text_area("📜 Enter Encrypted Text:", placeholder="Paste your encrypted text here... 📋", key="retrieve_data", help="Enter the encrypted text you received after storing data 📂")
    passkey = st.text_input("🔑 Enter Your Passkey:", type="password", placeholder="Enter the passkey used for encryption 🔐", key="retrieve_passkey", help="Enter the passkey used during encryption 🔓")
    st.markdown('<style>.stTextArea textarea, .stTextInput input { @extend .input-field; }</style>', unsafe_allow_html=True)

    if st.button("🔓 Decrypt", key="retrieve_btn", help="Click to decrypt your data 📝"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)
            if result:
                st.markdown(f'<p class="success">🔓 Decrypted Data: 🎉</p>', unsafe_allow_html=True)
                st.markdown(f'<div class="code-block">📜 {result}</div>', unsafe_allow_html=True)
            else:
                remaining = 3 - st.session_state.failed_attempts
                st.markdown(f'<p class="error">❌ Incorrect passkey or encrypted text! Attempts left: {remaining} 🚨</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="error">⚠️ Please provide both fields! 🚨</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif choice == "🔐 Login":
    st.markdown('<div class="card"><h2 class="text-2xl font-bold text-indigo-900 mb-4">🔐 Login to Reauthorize 🔑</h2>', unsafe_allow_html=True)
    login_pass = st.text_input("🔑 Enter Master Password:", type="password", placeholder="Enter master password 🔒", key="login_passkey", help="Enter the master password to reset attempts 🔓")
    st.markdown('<style>.stTextInput input { @extend .input-field; }</style>', unsafe_allow_html=True)

    if st.button("🔓 Login", key="login_btn", help="Click to reauthorize 🚀"):
        if login_pass == "admin123":
            st.markdown(f'<p class="success">✅ Login successful! You can now retrieve data. 🎉</p>', unsafe_allow_html=True)
            st.session_state.failed_attempts = 0
            st.session_state.current_page = "Retrieve Data"
            time.sleep(2)  # Delay to show success message
            st.rerun()
        else:
            st.markdown(f'<p class="error">❌ Incorrect master password! 🚨</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)