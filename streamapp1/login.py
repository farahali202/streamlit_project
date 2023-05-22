import pandas as pd
import plotly.express as px
import streamlit as st
from home  import  home
from contact import contact
from project import project
from prediction import prediction
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

# Setting up some basic configuration of our web app
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

    # Available usernames and passwords
usernames = ['fa', 'walmart']
passwords = {'fa': '123', 'walmart': 'phonepe'}
#login_successful is a variable or key used to represent the state of a successful 
# login in the Streamlit app you provided earlier. It is used to keep track of whether 
# the user has successfully logged in or not.
def main():
    #  The session state should be initialized before accessing it.
    #  You can do this by checking if a particular key exists in the st.
    # session_state dictionary and initializing it if it's not present.

    # Set up the initial state
    state = st.session_state.get('state', {'logged_in': False, 'page': 'home'})
    # Set up the initial state
    if not state['logged_in']:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            # Check the credentials and set the login state to True
            if username in usernames and password in passwords[username]:
                state['logged_in'] = True
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")

    # Display the selected page 
    # if logged in
    if state['logged_in']:
            home()


    hide_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
        """
    st.markdown(hide_style, unsafe_allow_html=True)

    # Save the state
    st.session_state['state'] = state

if __name__ == "__main__":
    main()


