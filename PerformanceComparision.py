import streamlit as st
import random as rd
import pandas as pd
import os
import string as s
import time
import matplotlib.pyplot as plt
st.markdown("<h1 style='text-align:center; color:rgb(153,242,196)'>Performance Comparision</h1>",unsafe_allow_html=True)
st.markdown("<p style='text-align:center'><b>Upload Your Codes</b></p>",unsafe_allow_html=True)
filee=st.file_uploader("",accept_multiple_files = True)
print(filee)
if filee !=[]:
    c=st.multiselect('Select Languages to Compare(MultiSelect)',['C','C++','Python','Java'])
    # st.markdown('**Name:** ')