import pandas as pd
import streamlit as st
from streamlit import write
from transformers import pipeline
import os

#def app():
#
#    st.write("This is my first app:") #Affichage d'un titre dans l'app






if __name__ == '__main__':


    unmasker = pipeline('fill-mask', model='distilbert-base-uncased')
    input = st.text_input('Put your text')
    if len(input):
        st.write("Your input is :\n" + input)
        st.write(pd.DataFrame(unmasker(input)))
    #app()
    # test 