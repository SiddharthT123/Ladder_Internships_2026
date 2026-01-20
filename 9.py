import pyttsx3
import google.genai as genai        
import streamlit as st
import builtins 

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain with a lot of detail on Databases, Advanced Libraries, and Frameworks in Python. Make it 3 paragraphs long."
)
text = response.candidates[0].content.parts[0].text
st.write(text)

ask9 = st.text_input("Do you have any questions? (yes / no)", key="ask_2")

if ask9.lower() == "no":
    st.write("Moving on ✅")

elif ask9.lower() == "yes":
    question9 = st.text_input("Please type your question", key="question_input_2")

    if question9:
        response9 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question9 + "Make it pretty short at max 1 paragraph."
        )
        answer9 = response9.candidates[0].content.parts[0].text
        st.write(answer9)

else:
    if ask9:
        st.write("Please type yes or no")

if st.button("Next topic ▶"):
    st.switch_page("pages/10")  # use correct path