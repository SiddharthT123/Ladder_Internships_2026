import streamlit as st
import json

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="ChatBot Bob - Auth",
    layout="centered"
)

# -------------------------------------------------
# Load & save users
# -------------------------------------------------
def load_users():
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

users = load_users()

# -------------------------------------------------
# UI
# -------------------------------------------------
st.title("🤖 ChatBot Bob")

mode = st.radio("Choose an option", ["Login", "Sign Up"])

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# -------------------------------------------------
# SIGN UP MODE
# -------------------------------------------------
if mode == "Sign Up":
    st.subheader("Create an account")
    confirm_password = st.text_input("Confirm password", type="password")

    if st.button("Sign Up"):
        if not username or not password or not confirm_password:
            st.warning("Please fill in all fields.")
        elif username in users:
            st.error("Username already exists.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            users[username] = password
            save_users(users)

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Account created successfully!")
            st.switch_page("pages/Readme.py")

# -------------------------------------------------
# LOGIN MODE
# -------------------------------------------------
else:
    st.subheader("Login to your account")

    if st.button("Login"):
        if not username or not password:
            st.warning("Please fill in all fields.")
        elif username not in users:
            st.error("User does not exist.")
        elif users[username] != password:
            st.error("Incorrect password.")
        else:
            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Logged in successfully!")
            st.switch_page("pages/Readme.py")

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.caption("© Coding Coach Bob")





