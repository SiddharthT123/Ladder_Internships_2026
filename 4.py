import pyttsx3
import google.genai as genai
import streamlit as st
import builtins

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain with a lot of detail on Operators, Control Flow, Functions, and Modules in Python. Make it 3 paragraphs long."
)
text = response.candidates[0].content.parts[0].text
st.write(text)

ask4 = st.text_input("Do you have any questions? (yes / no)", key="ask_2")

if ask4.lower() == "no":
    st.write("Moving on ✅")

elif ask4.lower() == "yes":
    question4 = st.text_input("Please type your question", key="question_input_2")

    if question4:
        response4 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question4 + "Make it pretty short at max 1 paragraph."
        )
        answer4 = response4.candidates[0].content.parts[0].text
        st.write(answer4)

else:
    if ask4:
        st.write("Please type yes or no")

if st.button("Next topic ▶"):
    st.switch_page("pages/5.py")  # use correct path

