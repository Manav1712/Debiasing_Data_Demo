import streamlit as st
import pandas as pd
import numpy as np
from annotated_text import annotated_text
from test_demo import head, insert_input1, insert_input2, output

head()

s = st.selectbox('Pick a Task',['Click A Task Inside','Task 1', 'Task 2'])
if s == 'Task 1':
    text = insert_input1()
    
    if st.button('Submit'):
        output(text)
        
   

elif s == 'Task 2':
   text = insert_input2()
   if st.button('Submit'):
        st.subheader('Input:')
        st.write(text)
        output(text)


#st.write('Output:')



    
    


