import streamlit as st
from PIL import Image  
img = Image.open("logo1.jpg") 
st.image(img, width=100) # Display the image with a specified width
st.title("gemini chatbot")

name = st.text_input("ASK THE QUESTION")

st.sidebar.header("chatbot")

# st.header("This is a header") 
# st.subheader("This is a subheader")

# st.success("Success")

# st.info("Information")

# st.warning("Warning")

# st.error("Error")

# exp = ZeroDivisionError("Trying to divide by Zero")
# st.exception(exp)