import streamlit as st

with st.form('my_form'):
    name=st.text_input('Enter your name')
    age=st.slider('Enter you age',18,30,18)
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write(f'Hey {name} Welcome our new page')
        st.write('Enter any number and get square value')
    number = st.number_input('Enter a number')
    submit_number = st.form_submit_button('Submit number')
    if submit_number:
        st.write(f'The square of {number} is {number**2}')
        