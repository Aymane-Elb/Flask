from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "styles" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "Animation.json"

# Function to load and display animation
def load_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Apply effect
def run_snow_animation():
    rain(emoji="🏂", font_size=18, falling_speed=4, animation_length="infinite")

# Function to get name
def getting_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["mate"])[0]

# Page config
st.set_page_config(page_title="Happy journey", page_icon="❤️")

# Running the snowfall animation
run_snow_animation()

# Applying CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Personalized name
PERSON_NAME = getting_name()
st.header(f"Happy Journey, {PERSON_NAME}! 🚗")

# Displaying animation
lottie_animation = load_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=320)
