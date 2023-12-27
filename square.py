import streamlit as st

def get_square(num):
    return num*num

number = st.number_input("Insert a number", value=None, placeholder = "Type a number ...")
if st.button("Submit"):
    st.write("The current Number is: ", number)
    st.write("Square of the number is: ", get_square(number))
else:
    st.write("Please enter the number and click submit button")
    