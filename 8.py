import pyttsx3
import google.genai as genai
import streamlit as st
import builtins

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()

client = genai.Client(api_key=api_key)



response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain with a lot of detail on Networking and APIs in Python. Make it 3 paragraphs long."
)
text = response.candidates[0].content.parts[0].text
st.write(text)
ask8 = st.text_input("Do you have any questions? (yes / no)", key="ask_2")

if ask8.lower() == "no":
    st.write("Moving on ✅")

elif ask8.lower() == "yes":
    question8 = st.text_input("Please type your question", key="question_input_2")

    if question8:
        response8 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question8 + "Make it pretty short at max 1 paragraph."
        )
        answer8 = response8.candidates[0].content.parts[0].text
        st.write(answer8)

else:
    if ask8:
        st.write("Please type yes or no")

if st.button("Next topic ▶"):
    st.switch_page("pages/9.py")  # use correct path

