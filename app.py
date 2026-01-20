import streamlit as st
import json

st.set_page_config(page_title="Bob Tutor - Login", layout="centered")

def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

users = load_users()

st.title("🤖 Coding Coach Bob")
st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username in users and users[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.switch_page("chat2.py")
    else:
        st.error("Invalid username or password")
