import streamlit as st
import random
import joblib
import numpy as np
import time

# Load the trained ML model
# model = joblib.load("redshift_model.pkl")

# Page config
st.set_page_config(page_title='Galactic Explorer', page_icon='🌌', layout='wide')

# Theme Selector
theme_choice = st.sidebar.selectbox("Choose Theme:", ["Dark Galaxy", "Nebula Glow", "Starry Night", "Cosmic Aurora"])
theme_styles = {
    "Dark Galaxy": {"bg": "#0D0D0D", "text": "#FFFFFF"},
    "Nebula Glow": {"bg": "#3D2C8D", "text": "#FFD700"},
    "Starry Night": {"bg": "#1A1A40", "text": "#87CEEB"},
    "Cosmic Aurora": {"bg": "#004D40", "text": "#FF69B4"}
}

def apply_theme(bg_color, text_color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}
        @keyframes fadeIn {{
            0% {{opacity: 0;}}
            100% {{opacity: 1;}}
        }}
        h1, h2, h3, p, label {{
            color: {text_color} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

apply_theme(theme_styles[theme_choice]["bg"], theme_styles[theme_choice]["text"])

# Title with animation
st.markdown(
    f"""
    <h1 style='text-align: center; color: {theme_styles[theme_choice]["text"]}; text-shadow: 2px 2px 8px #8B0000;'>
    🚀 Galactic Explorer 🌌
    </h1>
    """,
    unsafe_allow_html=True
)

# Description
st.markdown(
    f"<p style='text-align: center; font-size: 20px; color: {theme_styles[theme_choice]["text"]};'>Discover the wonders of the universe and explore the vastness of space!</p>",
    unsafe_allow_html=True
)

# Interactive Galaxy Facts
galaxy_facts = [
    "The Milky Way is about 100,000 light-years in diameter.",
    "There are more than 100 billion galaxies in the observable universe.",
    "A supermassive black hole exists at the center of most galaxies.",
    "Some galaxies have trillions of stars!",
    "Andromeda will collide with the Milky Way in 4.5 billion years."
]
if st.button("🌠 Discover a Galaxy Fact!"):
    st.markdown(f"<p style='text-align:center; font-size:18px; color: {theme_styles[theme_choice]['text']};'>{random.choice(galaxy_facts)}</p>", unsafe_allow_html=True)

# AI Space Fortune Teller
st.header("🔮 AI Space Fortune Teller")
user_name = st.text_input("Enter your name to receive a cosmic fortune:")
if user_name and st.button("🔭 Reveal My Fortune"):
    fortunes = [
        "You will discover a new galaxy!",
        "Dark matter will reveal its secrets to you!",
        "A comet will bring you great luck!",
        "Your future is as bright as a supernova!",
        "The universe has big plans for you!"
    ]
    st.success(f"{user_name}, {random.choice(fortunes)}")

# Cosmic Trivia Quiz
st.header(" Cosmic Trivia Quiz")
questions = {
    "What galaxy do we live in?": ["Andromeda", "Milky Way", "Whirlpool", "Sombrero"],
    "What is the biggest planet in our Solar System?": ["Earth", "Mars", "Jupiter", "Saturn"],
    "How long does light take to travel from the Sun to Earth?": ["8 minutes", "1 hour", "3 seconds", "24 hours"]
}
question = random.choice(list(questions.keys()))
answer = st.radio(question, questions[question])
if st.button("Submit Answer"):
    correct_answers = {"What galaxy do we live in?": "Milky Way", "What is the biggest planet in our Solar System?": "Jupiter", "How long does light take to travel from the Sun to Earth?": "8 minutes"}
    if answer == correct_answers[question]:
        st.success("🎉 Correct!")
    else:
        st.error(" Wrong! Try again.")

# Redshift Prediction Form
st.header(" Predict Redshift")
st.markdown("Enter galaxy properties to predict redshift:")
feature1 = st.number_input("Feature 1 (e.g., Spectral Line Intensity)", min_value=0.0, step=0.01)
feature2 = st.number_input("Feature 2 (e.g., Galaxy Brightness)", min_value=0.0, step=0.01)
feature3 = st.number_input("Feature 3 (e.g., Distance from Earth in Mpc)", min_value=0.0, step=0.01)
if st.button("Predict Redshift"):
    input_features = np.array([[feature1, feature2, feature3]])
    prediction = 0.42  # Replace with model.predict(input_features)[0]
    st.success(f"Predicted Redshift: {prediction:.5f}")

# Space Sound Effects
if st.sidebar.checkbox("Enable Space Sounds"):
    st.audio("https://www.example.com/space-sound.mp3", format='audio/mp3')

# Sidebar with additional resources
st.sidebar.header("Explore More")
st.sidebar.markdown(" [NASA's Galaxy Guide](https://www.nasa.gov/galaxies)")
st.sidebar.markdown("[Hubble Telescope Discoveries](https://hubblesite.org/)")
st.sidebar.markdown(" [Latest Space News](https://www.space.com/news)")
