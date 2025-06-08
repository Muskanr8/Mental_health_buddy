import streamlit as st
from mood_detector import detect_mood
import base64

# 🔹 MUST be the very first Streamlit command
st.set_page_config(page_title="Mental Health Companion", layout="centered")

# 🔹 Then define background
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 🔹 Call background setup
set_bg("assets/bg1.jpg")

# ✅ Now the rest of your app
st.markdown(
    "<h1 style='text-align: center; color: #bd84e8;'>YOUR MENTAL HEALTH BUDDY</h1>",
    unsafe_allow_html=True
)

st.markdown("Hi! Tell me how you're feeling today...")

user_input = st.text_area("Your thoughts here:", "")

if st.button("Analyze Mood"):
    if user_input.strip() != "":
        mood, confidence = detect_mood(user_input)
        st.success(f"Detected Mood: **{mood}** (Confidence: {confidence:.2f})")

        # Suggest remedies
        st.markdown("### 🌿 Suggested Remedy")
        if mood == "Happy":
            st.info("Keep doing what makes you feel good! 😊 Maybe share your happiness with a friend.")
        elif mood == "Sad or Stressed":
            st.info("Try a short meditation or write down your thoughts. Talking to someone helps too.")
        else:
            st.info("Stay mindful and present. Take a short walk or listen to calming music.")
    else:
        st.warning("Please enter some text to analyze.")
