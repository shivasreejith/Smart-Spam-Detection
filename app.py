import streamlit as st
import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Page settings
st.set_page_config(
    page_title="Smart Spam Detection",
    page_icon="📩",
    layout="centered"
)

# Title
st.title("📩 Smart Spam Detection System")
st.write("Enter a message below to check whether it is Spam or Ham.")

# Input box
message = st.text_area("Enter your message here:")

# Predict button
if st.button("Check Message"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)[0]

        if prediction == 1:
            st.error("🚫 This message is SPAM")
        else:
            st.success("✅ This message is HAM (Not Spam)")