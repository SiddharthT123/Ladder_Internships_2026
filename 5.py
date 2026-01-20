import pyttsx3
import google.genai as genai
import streamlit as st
import builtins

from pages.Readme import response

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()
client = genai.Client(api_key=api_key)



response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain with a lot of detail on variables in Python. Make it 3 paragraphs long."
)
text = response.candidates[0].content.parts[0].text
st.write(text)
ask5 = st.text_input("Do you have any questions? (yes / no)", key="ask_2")

if ask5.lower() == "no":
    st.write("Moving on ✅")

elif ask5.lower() == "yes":
    question5 = st.text_input("Please type your question", key="question_input_2")

    if question5:
        response5 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question5 + "Make it pretty short at max 1 paragraph."
        )
        answer5 = response5.candidates[0].content.parts[0].text
        st.write(answer5)

else:
    if ask5:
        st.write("Please type yes or no")

if st.button("Next topic ▶"):
    st.switch_page("pages/6.py")  # use correct path


