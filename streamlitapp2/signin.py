import streamlit as st
import pymongo as py
from pymongo.server_api import ServerApi
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import time

def main():
    # Display a loading message while the data is being loaded
    with st.spinner("Loading data..."):
    # Refresh the app after a specified time interval
        st.text("This app will refresh in 5 seconds.")
        time.sleep(2)  # Delay for 10 seconds
        st.experimental_rerun()
def mainclose():
    # Display a loading message while the data is being loaded
    with st.spinner("..."):
    # Refresh the app after a specified time interval
        time.sleep(2)  # Delay for 10 seconds
        st.experimental_rerun()

def apppen(name):

    st.info(f"You are logged as {name}")

    st.write("""
    # Penguin Prediction App

    This app predicts the **Palmer Penguin** species!

    Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
    """)

    st.sidebar.header('User Input Features')

    st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
    """)

    # Collects user input features into dataframe
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
    else:
        def user_input_features():
            island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
            sex = st.sidebar.selectbox('Sex',('male','female'))
            bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
            bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
            flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
            body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
            data = {'island': island,
                    'bill_length_mm': bill_length_mm,
                    'bill_depth_mm': bill_depth_mm,
                    'flipper_length_mm': flipper_length_mm,
                    'body_mass_g': body_mass_g,
                    'sex': sex}
            features = pd.DataFrame(data, index=[0])
            return features
        input_df = user_input_features()

    # Combines user input features with entire penguins dataset
    # This will be useful for the encoding phase
    penguins_raw = pd.read_csv('penguins_cleaned.csv')
    penguins = penguins_raw.drop(columns=['species'])
    df = pd.concat([input_df,penguins],axis=0)

    # Encoding of ordinal features
    # https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
    encode = ['sex','island']
    for col in encode:
        dummy = pd.get_dummies(df[col], prefix=col)
        df = pd.concat([df,dummy], axis=1)
        del df[col]
    df = df[:1] # Selects only the first row (the user input data)

    # Displays the user input features
    st.subheader('User Input features')

    if uploaded_file is not None:
        st.write(df)
    else:
        st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
        st.write(df)
    # Reads in saved classification model
    load_clf = pickle.load(open('peng.pkl', 'rb'))

    # Apply model to make predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)


    st.subheader('Prediction')
    penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
    st.write(penguins_species[prediction])

    st.subheader('Prediction Probability')
    st.write(prediction_proba)

def conn():
        mydb = py.MongoClient("mongodb://localhost:27017/")
        db = mydb.get_database('users')
        return db.users

user_db = conn()

# Initialize Session States.
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'form' not in st.session_state:
    st.session_state.form = ''

def select_signup():
    st.session_state.form = 'signup_form'
def deselect_signup():
    st.session_state.form = ''

def user_update(name):
    st.session_state.username = name

if st.session_state.username != '':
    apppen(st.session_state.username.upper())
# Initialize Sing In or Sign Up forms
if st.session_state.form == 'signup_form' and st.session_state.username == '':
    signup_form = st.form(key='signup_form', clear_on_submit=True)
    new_username = signup_form.text_input(label='Enter Username*')
    new_user_email = signup_form.text_input(label='Enter Email Address*')
    new_user_pas = signup_form.text_input(label='Enter Password*', type='password')
    user_pas_conf = signup_form.text_input(label='Confirm Password*', type='password')
    note = signup_form.markdown('**required fields*')
    signup = signup_form.form_submit_button(label='Sign Up')
    
    if signup:
        if any([new_username == '', new_user_email == '', new_user_pas == '']):
            st.error('Some fields are missing')
        else:
            if user_db.find_one({'log' : new_username}):
                st.error('Username already exists')
            if user_db.find_one({'email' : new_user_email}):
                st.error('Email is already registered')
            else:
                if new_user_pas != user_pas_conf:
                    st.error('Passwords do not match')
                else:
                    user_update(new_username)
                    user_db.insert_one({'log' : new_username, 'email' : new_user_email, 'pass' : new_user_pas})
                    st.success('You have successfully registered!')
                    main()
                    del new_user_pas, user_pas_conf
                    
                    #st.set_page_config(page_title="Penguin Classification",page_icon=":bar_chart:", layout="wide")
                    
                    
                    
elif st.session_state.username == '':
    login_form = st.form(key='signin_form', clear_on_submit=True)
    username = login_form.text_input(label='Enter Username')
    user_pas = login_form.text_input(label='Enter Password', type='password')
    
    if user_db.find_one({'log' : username, 'pass' : user_pas}):
        login = login_form.form_submit_button(label='Sign In', on_click=user_update(username))
        if login:
            st.success('You have successfully registered!')
            main()
            del user_pas
            
            #st.set_page_config(page_title="Penguin Classification",page_icon=":bar_chart:", layout="wide")
            
    else:
        login = login_form.form_submit_button(label='Sign In')
        if login:
            st.error("Username or Password is incorrect. Please try again or create an account.")
else:
    logout = st.sidebar.button(label='Log Out')
    if logout:
        user_update('')
        st.session_state.form = ''
        mainclose()

# 'Create Account' link
if st.session_state.username == "" and st.session_state.form != 'signup_form':
    st.markdown("Don't have an account?")
    signup_request = st.empty()
    signup_request.button('Create Account', on_click=select_signup)
if st.session_state.username == "" and st.session_state.form == 'signup_form':
    st.markdown("Already have an account?  ")
    signup_request = st.empty()
    signup_request.button('Sign in', on_click=deselect_signup)


