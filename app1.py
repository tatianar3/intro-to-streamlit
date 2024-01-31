import streamlit as st
import datetime

st.title("My First Web App for HCI!")
st.header("User's Input")
st.subheader("Registration")

first_name = st.text_input("Enter first name:")
last_name = st.text_input("Enter last name:")
year_of_birth = st.number_input("Enter your year of birth:")
start_year_fiu = st.number_input("Enter the year you started at FIU:")

current_year = datetime.date.today().year
age = current_year - year_of_birth
years_at_fiu = current_year - start_year_fiu

if first_name and last_name and year_of_birth and start_year_fiu:
    st.success(f"Hi {first_name} {last_name}! You are {age} years old,"
               f"and you have been at FIU for {years_at_fiu} years.") # st.warning, st.info, etc

    # st.markdown for HTML and CSS stuff
