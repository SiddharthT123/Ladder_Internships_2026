import pyttsx3
import google.genai as genai
import streamlit as st
import builtins

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain with a lot of detail on Miltithreading and Multiprocessing in Python. Make it 3 paragraphs long."
)
text = response.candidates[0].content.parts[0].text
st.write(text)

ask7 = st.text_input("Do you have any questions? (yes / no)", key="ask_2")

if ask7.lower() == "no":
    st.write("Moving on ✅")

elif ask7.lower() == "yes":
    question7 = st.text_input("Please type your question", key="question_input_2")

    if question7:
        response7 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question7 + "Make it pretty short at max 1 paragraph."
        )
        answer7 = response7.candidates[0].content.parts[0].text
        st.write(answer7)

else:
    if ask7:
        st.write("Please type yes or no")

if st.button("Next topic ▶"):
    st.switch_page("pages/8.py")  # use correct path

