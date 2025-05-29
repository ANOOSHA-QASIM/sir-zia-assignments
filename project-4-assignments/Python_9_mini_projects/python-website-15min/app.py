import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page config
st.set_page_config(page_title="Generative AI Website", page_icon="🤖", layout="wide")

# Function to load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
ai_animation = load_lottieurl("https://lottie.host/c75eafa0-f207-4564-861d-4166485ad377/dTOybMcYYX.json")  # Home animation
other_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_zrqthn6o.json")  # Demo animation for other sections
future_animation = load_lottieurl("https://lottie.host/a8115d2f-73ea-4181-9947-0d36d073f5f0/eDqGppoNh1.json")


# Custom CSS for styling
st.markdown("""
    <style>
    header {visibility: hidden;}
    .main {
        background: linear-gradient(to right, #fdfbfb, #ebedee);
        padding: 30px;
        border-radius: 15px;
        font-family: 'Segoe UI', sans-serif;
    }
    .header {
        font-size: 55px;
        color: #7b1fa2;
        font-weight: 800;
        margin-top: 30px;
        text-align: center;
    }
    .subhead {
        font-size: 32px;
        color: #512da8;
        font-weight: bold;
        margin-top: 25px;
    }
    .info {
        font-size: 18px;
        color: #333;
        line-height: 1.6;
    }
    .multicolor-header {
        background: linear-gradient(to right, #ff6f00, #f44336, #6a1b9a);
        color: white;
        font-size: 40px;
        padding: 12px;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
section = st.sidebar.radio("📚 Navigate", ["🏠 Home", "🚀 Benefits", "🔬 Applications", "⚠️ Risks", "📌 Future"])

# Home Section
if section == "🏠 Home":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="multicolor-header">Generative AI: Revolutionizing Creativity 🤖</div>', unsafe_allow_html=True)
    st.markdown('<div class="header">What is Generative AI?</div>', unsafe_allow_html=True)

    if ai_animation:
        st_lottie(ai_animation, height=250, key="ai")
    
    st.markdown('''
        <p class="info">
        Generative AI is a powerful branch of artificial intelligence that can create new and original content — from text to music, code, and images.
        With tools like <b>ChatGPT, DALL·E, and Midjourney</b>, AI is helping creators, students, and professionals bring ideas to life faster than ever.
        </p>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Benefits Section
elif section == "🚀 Benefits":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="multicolor-header">The Power of Generative AI 🌟</div>', unsafe_allow_html=True)
    st.markdown('<div class="subhead">Benefits of Generative AI</div>', unsafe_allow_html=True)

    st_lottie(other_animation, height=250, key="benefits")

    st.markdown('''
        <p class="info">
        Generative AI brings countless advantages to various industries and individuals:
        <ul>
            <li>🧠 <b>Enhanced Creativity:</b> Artists, writers, and musicians generate ideas or full compositions using AI tools.</li>
            <li>⏱️ <b>Time Saver:</b> Content creation, coding, and design become much faster.</li>
            <li>🌍 <b>Language Translation:</b> Breaks language barriers with real-time AI translations.</li>
            <li>🎯 <b>Personalization:</b> Creates customized ads, learning plans, and user experiences.</li>
            <li>🧬 <b>Healthcare Advances:</b> AI speeds up medical research and drug discovery.</li>
        </ul>
        </p>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Applications Section
elif section == "🔬 Applications":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="multicolor-header">Generative AI Applications 🌍</div>', unsafe_allow_html=True)
    st.markdown('<div class="subhead">Real-World Applications</div>', unsafe_allow_html=True)

    st_lottie(other_animation, height=250, key="applications")

    st.markdown('''
        <p class="info">
        Generative AI is already shaping the world in ways you might not even realize:
        <ul>
            <li>📝 <b>Writing:</b> AI like ChatGPT writes essays, blogs, and scripts.</li>
            <li>🎨 <b>Design:</b> Tools like DALL·E generate unique visuals for marketing and art.</li>
            <li>🧬 <b>Healthcare:</b> AI analyzes patient data and suggests treatments.</li>
            <li>🎮 <b>Gaming:</b> Game developers use AI to generate stories, environments, and characters.</li>
            <li>🛍️ <b>E-Commerce:</b> Personalized product recommendations and chatbots.</li>
        </ul>
        </p>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Risks Section
elif section == "⚠️ Risks":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="multicolor-header">Understanding the Risks ⚠️</div>', unsafe_allow_html=True)
    st.markdown('<div class="subhead">Risks of Generative AI</div>', unsafe_allow_html=True)

    st_lottie(other_animation, height=250, key="risks")

    st.markdown('''
        <p class="info">
        While Generative AI is powerful, it comes with serious concerns:
        <ul>
            <li>🔍 <b>Misinformation:</b> Deepfakes and AI-written fake news can spread quickly.</li>
            <li>📉 <b>Job Displacement:</b> Automation may replace certain human jobs.</li>
            <li>🤖 <b>Bias:</b> AI trained on biased data can produce unfair outcomes.</li>
            <li>🔐 <b>Data Privacy:</b> AI systems require massive amounts of user data.</li>
            <li>🧠 <b>Over-Reliance:</b> People may stop thinking critically and rely too much on AI.</li>
        </ul>
        </p>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Future Section
elif section == "📌 Future":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="multicolor-header">The Future of Generative AI 🚀</div>', unsafe_allow_html=True)
    st.markdown('<div class="subhead">What’s Next?</div>', unsafe_allow_html=True)

    st_lottie(future_animation, height=250, key="future")

    st.markdown('''
        <p class="info">
        The future of Generative AI looks even more exciting:
        <ul>
            <li>🚀 <b>AI Co-Pilots:</b> Like GitHub Copilot, assisting developers in real-time.</li>
            <li>🌐 <b>Hyper-Personalization:</b> Every app, website, and product will adapt to each user.</li>
            <li>🤝 <b>Human + AI:</b> Seamless collaboration between people and intelligent systems.</li>
            <li>🧠 <b>Smarter Assistants:</b> Virtual agents that understand emotion and intent.</li>
            <li>🦾 <b>Enhanced Creativity:</b> AI helping artists, musicians, and creators push the boundaries of imagination.</li>
        </ul>
        </p>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
