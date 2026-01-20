import pyttsx3
import google.genai as genai
import streamlit as st
import builtins

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()

client = genai.Client(api_key=api_key)






response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain with a lot of detail on List Comprehensions, File handling, Error, Classes, and OOP in Python. Make it 3 paragraphs long."
)
text = response.candidates[0].content.parts[0].text
st.write(text)

ask6 = st.text_input("Do you have any questions? (yes / no)", key="ask_2")

if ask6.lower() == "no":
    st.write("Moving on ✅")

elif ask6.lower() == "yes":
    question6 = st.text_input("Please type your question", key="question_input_2")

    if question6:
        response6 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question6 + "Make it pretty short at max 1 paragraph."
        )
        answer6 = response6.candidates[0].content.parts[0].text
        st.write(answer6)

else:
    if ask6:
        st.write("Please type yes or no")

if st.button("Next topic ▶"):
    st.switch_page("pages/7.py")  # use correct path

