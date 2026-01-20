import pyttsx3
import google.genai as genai    
import streamlit as st
import builtins 

api_key = st.text_input("Enter your Gemini API key:  ", key="api_key").strip()
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain with a lot of detail on Memory Management and Optimization in Python. Make it 3 paragraphs long."
)
text = response.candidates[0].content.parts[0].text
st.write(text)
ask10 = st.text_input("Do you have any questions? (yes / no)", key="ask_2")

if ask10.lower() == "no":
    st.write("Moving on ✅")

elif ask10.lower() == "yes":
    question10 = st.text_input("Please type your question", key="question_input_2")

    if question10:
        response10 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question10 + "Make it pretty short at max 1 paragraph."
        )
        answer10 = response10.candidates[0].content.parts[0].text
        st.write(answer10)

else:
    if ask10:
        st.write("Please type yes or no")