import streamlit as st
import requests
import pandas as pd

from json_reader import read_json

st.title("Language Vocabulary Importer")

category = st.text_input("Enter a thematic category for vocabulary generation:")

if 'vocabulary' not in st.session_state:
    st.session_state.vocabulary = None

if st.button("Generate Vocabulary"):
    if category:
        st.success("Vocabulary generated successfully!")
        words_response = document = read_json("api_response.json")
        group_name = list(words_response.keys())[0]
        words = words_response[group_name]
        st.session_state.vocabulary = pd.DataFrame(words)
        st.table(st.session_state.vocabulary)
        
    else:
        st.warning("Please enter a thematic category.")

# Add a button to submit the generated vocabulary
if st.session_state.vocabulary is not None:
    if st.button("Submit Vocabulary"):
        # Make a request to another API endpoint to submit the vocabulary
        submit_response = requests.post("http://localhost:8000/submit_vocabulary", 
                                        json={"category": category, 
                                              "vocabulary": st.session_state.vocabulary.to_dict(orient="records")})
        
        if submit_response.status_code == 200:
            st.success("Vocabulary submitted successfully!")
        else:
            st.error("Failed to submit vocabulary. Please try again.")