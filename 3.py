import pyttsx3
import google.genai as genai
import streamlit as st
import builtins

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain with a lot of detail on syntax and structures in Python. Make it 3 paragraphs long."
)
text = response.candidates[0].content.parts[0].text
st.write(text)

ask3 = st.text_input("Do you have any questions? (yes / no)", key="ask_2")

if ask3.lower() == "no":
    st.write("Moving on ✅")

elif ask3.lower() == "yes":
    question3 = st.text_input("Please type your question", key="question_input_2")

    if question3:
        response3 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question3 + "Make it pretty short at max 1 paragraph."
        )
        answer3 = response3.candidates[0].content.parts[0].text
        st.write(answer3)

else:
    if ask3:
        st.write("Please type yes or no")

if st.button("Next topic ▶"):
    st.switch_page("pages/4.py")  # use correct path