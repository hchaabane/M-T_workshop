import pandas as pd
import streamlit as st
from streamlit import write
from transformers import pipeline
from google.cloud import firestore
import os

#def app():
#
#    st.write("This is my first app:") #Affichage d'un titre dans l'app






if __name__ == '__main__':

    db = firestore.Client.from_service_account_info(st.secrets["gcp_service_account"])
    unmasker = pipeline('fill-mask', model='distilbert-base-uncased')
    input = st.text_input('Put your text')
    if len(input):
        st.write("Your input is :\n" + input)
        result = unmasker(input)
        st.write(pd.DataFrame(result))

    if st.button("Store result in the database"):
        data = {
            u"table_results": result
        }
        db.collection("posts").document(input).set(data)
    #app()
    # test