import streamlit as st
import EDA, predict

with st.sidebar:
    st.title('Page Navigation')
    # input 
    page =st.radio('Page', ('EDA','Model Demo'))
    st.write('# About')
    st.write('''dadbabdabdabdbadbada''')

if page=='EDA':
    EDA.run()
else :
    predict.run()