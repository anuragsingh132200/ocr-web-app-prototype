# app.py
import streamlit as st
from ocr import extract_text_from_image
from search import search_keywords

def main():
    st.title("OCR and Document Search Web Application")
    
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        with open("uploaded_image.png", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.image("uploaded_image.png", caption="Uploaded Image", use_column_width=True)
        
        extracted_text = extract_text_from_image("uploaded_image.png")
        st.subheader("Extracted Text")
        st.write(extracted_text)
        
        keyword = st.text_input("Enter keyword to search")
        if keyword:
            search_results = search_keywords(extracted_text, keyword)
            st.subheader("Search Results")
            for result in search_results:
                st.write(result)

if __name__ == "__main__":
    main()