import streamlit as st
import pandas as pd
import joblib
import base64

def local_background(image_file):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("file://{image_file}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Add background image
local_background(r"C:\Users\admin\Desktop\ipl_winning_prediction\images\ipl_banner.jpg")

st.title("🏏 IPL Winning Team Predictor")


# Load model and encoders
model = joblib.load("models/ipl_model.pkl")
le_batting = joblib.load("models/le_batting.pkl")
le_bowling = joblib.load("models/le_bowling.pkl")
le_venue = joblib.load("models/le_venue.pkl")

# Title
st.title("🏏 IPL Winning Team Predictor")

# Team & Venue Inputs
batting_team = st.selectbox("Select Batting Team", le_batting.classes_)
bowling_team = st.selectbox("Select Bowling Team", [t for t in le_bowling.classes_ if t != batting_team])
venue = st.selectbox("Select Venue", le_venue.classes_)
score = st.slider("1st Innings Score", 50, 250, 150)

# Predict
if st.button("Predict Winner"):
    input_df = pd.DataFrame([{
        "batting_team": le_batting.transform([batting_team])[0],
        "bowling_team": le_bowling.transform([bowling_team])[0],
        "venue": le_venue.transform([venue])[0],
        "total": score
    }])
    
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.success(f"🎉 {batting_team} is likely to win!")
    else:
        st.warning(f"⚠️ {bowling_team} might win.")
