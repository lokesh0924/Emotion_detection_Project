import streamlit as st
import pickle
import pandas as pd
import plotly.express as px
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

from database.db import init_db, insert_data, get_all_data
from src.utils import get_suggestion
load_dotenv()
init_db()

model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

st.title("Emotion Intelligence System")

with st.form("form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    text = st.text_area("How are you feeling?")
    submit = st.form_submit_button("Analyze")

def send_email(to_email, name, emotion, suggestion, text):
    sender_email = os.getenv("EMAIL_USER")
    app_password = os.getenv("EMAIL_PASS")

    body = f"""Hello {name},

Emotion: {emotion}

Suggestion:
{suggestion}

Your Input:
{text}

Regards,
Emotion AI System
"""

    msg = MIMEText(body)
    msg["Subject"] = "Emotion Report"
    msg["From"] = sender_email
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit()

if submit:
    if not name or not email or not text:
        st.warning("All fields required")
    else:
        vec = vectorizer.transform([text])
        prediction = model.predict(vec)[0]
        probs = model.predict_proba(vec)[0]

        suggestion = get_suggestion(prediction)

        insert_data(name, email, text, prediction)

        st.success(f"Emotion: {prediction}")
        st.info(f"Suggestion: {suggestion}")

        df = pd.DataFrame({
            "Emotion": model.classes_,
            "Probability": probs
        })

        fig = px.bar(df, x="Emotion", y="Probability")
        st.plotly_chart(fig)

        send_email(email, name, prediction, suggestion, text)
        st.success("Email sent!")

st.subheader("Dashboard")

data = get_all_data()

if data:
    df = pd.DataFrame(data, columns=["ID","Name","Email","Text","Emotion"])
    st.write("Total Predictions:", len(df))
