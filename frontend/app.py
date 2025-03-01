import streamlit as st
import requests

st.title("ProVision AI+ : Image Analysis")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/analyze-image/", files=files)

    if response.status_code == 200:
        response_data = response.json()
        if "description" in response_data:
            st.write("### AI-Generated Description")
            st.write(response_data["description"])
        else:
            st.error(f"Backend Error: {response_data}")
    else:
        st.error(f"Request Failed: {response.status_code}, {response.text}")
