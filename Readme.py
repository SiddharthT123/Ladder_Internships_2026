import pyttsx3
import google.genai as genai
import streamlit as st
import builtins

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="ChatBot Bob - Sign Up",
    layout="centered"
)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.say(text)
    engine.runAndWait()

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()

# Don't create the client until we actually have a key
if not api_key:
    st.stop()

client = genai.Client(api_key=api_key)



def speak_response(resp):
    speak(resp.text)

def response(text):
    return client.models.generate_content(
        model="gemini-2.0-flash",
        contents=text
    )

# model = genai.GenerativeModel("gemini-pro")

builtins_print = speak

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Talk with a lot of enthusiasm about how to code in Python. Give an overview of the language and its uses. Use 1 sentence."
)
text = response.candidates[0].content.parts[0].text
st.write(text)

ask = st.text_input("Do you have any questions? (yes / no)", key="ask_1")

if ask.lower() == "no":
    st.write("Moving on ✅")

elif ask.lower() == "yes":
    question = st.text_input(
        "Please type your question",
        key="question_input_1"
    )

    if question:  # only call Gemini after user types something
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question + "Make it pretty short at max 1 paragraph."
        )

        # extract and display model text
        answer = response.candidates[0].content.parts[0].text
        st.write(answer)

else:
    if ask:  # only warn after user types something
        st.write("Please type yes or no")

if st.button("Next topic ▶"):
    st.switch_page("pages/2.py")  # use correct path


