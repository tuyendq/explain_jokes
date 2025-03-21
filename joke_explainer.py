import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

# print(token)

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Set your OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")  # You can set it in your environment

# Function to call OpenAI API and get explanation for the joke
def explain_joke_with_openai(joke):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "user", 
                    "content": f"Explain this joke: {joke}"
                }
            ]
        )
        explanation = response['choices'][0]['message']['content']
        return explanation
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit App
st.title("Yet Another Joke Explainer")

# Input box for the user to enter the joke
user_joke = st.text_input("Enter your joke below:")

# Submit button
if st.button("Submit"):
    if user_joke:
        explanation = explain_joke_with_openai(user_joke)
        st.write("**Explanation:**", explanation)
    else:
        st.warning("Please enter a joke before submitting.")

# Encourage users to submit more jokes
st.write("Feel free to submit another joke to see if I can explain it!")