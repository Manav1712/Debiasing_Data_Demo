import streamlit as st
import pandas as pd
import numpy as np
from annotated_text import annotated_text
import random

text = ""
def head():
    st.markdown("""
            <h1 style='text-align: center; margin-bottom: -35px;'>
            Insert Title Here
            </h1>
        """, unsafe_allow_html=True
        )
        
    st.caption("""
            <p style='text-align: center'>
            Insert Subtitle Here
            </p>
        """, unsafe_allow_html=True
        )
        
    

def choose_task():
    st.multiselect('Pick a Task',['Task 1', 'Task 2'])

def insert_input1():
    text = st.text_input("Type your Query")
    st.select_slider('Pick a value', ['1', '2', '3','4','5'])
    return text

def insert_input2():
    text = st.text_input("Type your Query")
    val = st.select_slider('Pick a value', ['1', '2', '3','4','5'])
    return text

def output(text):
    s = []
    if(" " in text):
        s = text.split(" ")
    
    st.subheader('Output: ')

    s = text.split(" ")
    print(s)

    l = []
    temp = ["","",""]
    x = 0
    for i in s:
        temp[0] = i
        temp[1] = "#"+''.join(random.choice('0123456789ABCDEF'))
        l.append(tuple(temp))
        x = x+1
        temp = ["","",""]

    st.subheader('Prediction')
    annotated_text(*l)
    st.subheader('TR')
    annotated_text(*l)
    st.subheader('PR')
    annotated_text(*l)


    
    
    


    






    