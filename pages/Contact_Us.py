import streamlit as st
from send_email import send_email

st.header("Contact Me")


with st.form(key="email_form"):
    email = st.text_input("Enter Your Email Adress:")
    raw_message = st.text_area("Your Message:")
    submit = st.form_submit_button("Submit")
    message = f"""\
Subject: New email from {email}

From: {email}
{raw_message}
"""
    if submit:
        send_email(message)
        st.info("Your email has been sent!")

