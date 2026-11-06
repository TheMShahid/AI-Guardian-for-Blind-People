
import streamlit as st

from ai_guardian.perception.image_reader import read_image


# Page configuration
st.set_page_config(
    page_title="AI Guardian",
    page_icon="👁️",
    layout="centered"
)

# Application heading
st.title("AI Guardian")
st.subheader("Reading Text with OCR")

st.write(
    "Upload an image containing printed text. "
    "AI Guardian will extract and display the recognized text."
)

# Image upload
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"]
)

# Process image after explicit user action
if st.button("Read Text"):

    if uploaded_file is None:
        st.warning("Please upload an image first.")

    else:
        image_bytes = uploaded_file.getvalue()

        with st.spinner("Reading image..."):
            result = read_image(image_bytes)

        if result["status"] == "SUCCESS":
            st.success("Text recognition completed.")
            st.text_area(
                "Recognized Text",
                value=result["text"],
                height=200
            )

        elif result["status"] == "NO_TEXT":
            st.info("No readable text was found in this image.")

        elif result["status"] == "INVALID_IMAGE":
            st.error(result["error"])

        else:
            st.error("Text recognition failed. Please try again.")
