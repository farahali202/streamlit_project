import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

def contact():
        from project import project
        from home import home
        from prediction import prediction
    # Display the selected page
        hide_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
        st.markdown(hide_style, unsafe_allow_html=True)

        st.title("Contact")
        contactr="""
                <style>
        .form-container {
                width: 400px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-family: Arial, sans-serif;
        }

        .form-container label {
                display: block;
                margin-bottom: 10px;
        }

        .form-container input,
        .form-container textarea {
                width: 100%;
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 3px;
                font-size: 14px;
        }

        .form-container button[type="submit"] {
                background-color: #4CAF50;
                color: #fff;
                border: none;
                padding: 10px 20px;
                border-radius: 3px;
                font-size: 16px;
                cursor: pointer;
        }

        .form-container button[type="submit"]:hover {
                background-color: #45a049;
        }
        </style>
        <div class="form-container">
                <form action="https://formsubmit.co/farahelhafi2020@gmail.com" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required><br>
                <label for="email">Email:</label>
                <input type="email" name="email" required><br>
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" cols="30" required></textarea>
                <button type="submit">Send</button>
                </form>
        </div>"""
        st.markdown(contactr,unsafe_allow_html=True)
# Run the app
if __name__ == "__main__":
        contact()

