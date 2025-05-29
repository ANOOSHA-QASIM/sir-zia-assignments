import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Use a fixed secret key for consistent encryption/decryption
KEY = b'kS6vEFAyzwVvS-5ClYbNg8nPjzXK3mQ_Zl6IF6rjR6Os='
cipher = Fernet(KEY)

# Initialize session state for storage and failed attempts
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)
    for data in st.session_state.stored_data.values():
        if data["encrypted_text"] == encrypted_text and data["passkey"] == hashed:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    st.session_state.failed_attempts += 1
    return None

st.set_page_config(page_title="Secure Vault", page_icon="🔐", layout="centered")
st.markdown("<h1 style='text-align:center;'>🔐 Secure Data Encryption System</h1>", unsafe_allow_html=True)
st.markdown("---")

menu = ["🏠 Home", "📥 Store Data", "📤 Retrieve Data", "🔑 Login"]
choice = st.sidebar.radio("🔎 Navigation Menu", menu)

if choice == "🏠 Home":
    st.markdown("### 🛡️ Welcome to Secure Vault!")
    st.write("Store & retrieve encrypted data securely.")
    st.caption(f"🔢 Stored entries: {len(st.session_state.stored_data)}")

elif choice == "📥 Store Data":
    st.markdown("### 📥 Store Your Secret Data")
    text = st.text_area("📝 Enter your secret data here:")
    passkey = st.text_input("🔑 Choose a passkey:", type="password")

    if st.button("🔐 Encrypt & Save"):
        if text and passkey:
            encrypted = encrypt_data(text)
            hashed = hash_passkey(passkey)
            st.session_state.stored_data[encrypted] = {"encrypted_text": encrypted, "passkey": hashed}
            st.success("✅ Data encrypted & saved!")
            st.markdown("**🔒 Encrypted Text:**")
            st.code(encrypted)
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "📤 Retrieve Data":
    st.markdown("### 📤 Retrieve Your Encrypted Data")
    encrypted_text = st.text_area("🔒 Enter your encrypted text:")
    passkey = st.text_input("🔑 Enter your passkey:", type="password")

    if st.button("🔓 Decrypt"):
        if encrypted_text and passkey:
            decrypted = decrypt_data(encrypted_text, passkey)
            if decrypted:
                st.success("✅ Decryption successful!")
                st.markdown("**🔍 Decrypted Data:**")
                st.code(decrypted)
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Wrong passkey! Attempts left: {attempts_left}")
                if attempts_left <= 0:
                    st.warning("🔒 Too many failed attempts. Please login.")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Please fill both fields!")

elif choice == "🔑 Login":
    st.markdown("### 🔐 Master Login")
    login = st.text_input("Enter master password:", type="password")

    if st.button("Login"):
        if login == "admin123":
            st.session_state.failed_attempts = 0
            st.success("✅ Login successful! You can retry now.")
        else:
            st.error("❌ Incorrect master password!")

st.markdown("---")
st.markdown("<p style='text-align:center;'>🎉 Thanks for using Secure Vault! 🛡️</p>", unsafe_allow_html=True)
