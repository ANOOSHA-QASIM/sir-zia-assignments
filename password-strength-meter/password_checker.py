import streamlit as st
import re
import random
import string
import requests

# Function to load Lottie animation from URL
def load_lottie_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # return json data if the request is successful
        return None
    except:
        return None  # return None if there's any issue with the request

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Password must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Use both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔸 Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔸 Include a special character (!@#$%^&*).")

    # Blacklist check
    blacklist = ["password123", "12345678", "qwerty", "admin", "iloveyou"]
    if password.lower() in blacklist:
        feedback.append("🔸 This password is too common. Choose a unique one.")
        score = 0

    return score, feedback

# Function to generate a strong random password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(12))  # 12 character password
    return password

# Streamlit UI setup
st.set_page_config(page_title="Password Strength Checker", layout="centered", page_icon="🔐")

# Page title and description
st.title("🔐 Password Strength Checker")
st.subheader("Check the strength of your password and get a stronger one 💪")

# User inputs for username and password
username = st.text_input("👤 Enter your username")
password = st.text_input("🔑 Enter your password", type="password")

# Button to check password strength
if st.button("🚀 Check Password Strength"):
    if username and password:
        score, feedback = check_password_strength(password)
        st.write(f"👋 Hello, {username}!")

        if score == 4:
            st.success("✅ Your password is Strong!")
            st.balloons()
            # Lottie animation
            lottie = load_lottie_url("https://lottie.host/9a1e3a95-3575-4c13-9d26-1597fbdc8233/rfQ8c0JIkM.json")
            if lottie:
                st.json(lottie)  # If the animation loads successfully, display it
        elif score == 3:
            st.warning("⚠️ Your password is Moderate. Improve it!")
            for msg in feedback:
                st.write(msg)
        else:
            st.error("❌ Weak password!")
            for msg in feedback:
                st.write(msg)
    else:
        st.warning("⚠️ Please enter both username and password.")

# Button to suggest a strong password
if st.button("🎲 Suggest Strong Password"):
    new_password = generate_strong_password()
    st.info(f"🔐 Try this: `{new_password}`")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Created with ❤️ by Anusha</p>", unsafe_allow_html=True)
