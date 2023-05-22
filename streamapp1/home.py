import streamlit as st
from contact import contact
from project import project
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import pandas as pd
import base64
def home():
    # Display the selected page
    menu_key = hash('option_menu_home')
    page = option_menu(
        menu_title=None,
        menu_icon=None,
        options=["home", "contact", "project"],
        orientation="horizontal",
        default_index=0,
        key=menu_key,  # Use the generated unique key
        styles = {
    "container": {
        "padding": "10px",
        "margin": "0",
        "background-color": "#0e1117",
        "border-radius": "5px",
    },
    "nav-link": {
        "font-size": "18px",
        "text-align": "center",
        "margin": "10px",
        "padding": "10px 20px",
        "color": "#ffffff",
        "background-color": "#0e1117",
        "border-radius": "5px",
    },
    "nav-link:hover": {
        "color": "#0e1117",
        "background-color": "#ffffff",
        "border-radius": "5px",
        "border-color":"blue"
    },
    "nav-link-selected": {
        "background-color": "#0e1117",
    },
}
    )

    if page == "contact":
        return contact()
    elif page == "project":
        return project()

    hide_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_style, unsafe_allow_html=True)
    st.title("Home")
    st.subheader('Description of data :')
    st.markdown(""" The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data. Predictive data analytics methods are easy to apply with this dataset.
    """)
    st.markdown("""**Attribute information:** """)
    Invoice_id=st.button("get information about nvoice_id:")
    if Invoice_id:
        st.write(""" Computer generated sales slip invoice identification number""")
    Branch=st.button("get information about Branch:")
    if Branch:
        st.markdown("""Branch of supercenter (3 branches are available identified by A, B and C).""")
    City=st.button("get information about City:")
    if City:
        st.markdown(""" Location of supercenters""")
    Customer=st.button("get information about Cstomer:")
    if Customer:
        st.markdown(""" Type of customers, recorded by Members for customers using member card and Normal for without member card.""")
    Gender=st.button("get information about Gender:")
    if Gender:
        st.markdown(""" Gender type of customer""")
    Product=st.button("get information about Product:")
    if Product:
        st.markdown(""" General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel""")
    Unit=st.button("get information about Unit:")
    if Unit :
        st.markdown("""Price of each product in $""")
    Quantity=st.button("get information about Quantity:")
    if Quantity:
        st.markdown("""Number of products purchased by customer""")
    Tax=st.button("get information about Tax:")
    if Tax:
        st.markdown("""5% tax fee for customer buying""")
    Total=st.button("get information about Total:")
    if Total:
        st.markdown("""Total price including tax""")
    Date=st.button("get information about Date:")
    if Date:
        st.markdown("""Date of purchase (Record available from January 2019 to March 2019)""")
    Time=st.button("get information about Time:")
    if Time:
        st.markdown("""Purchase time (10am to 9pm)""")
    Payment=st.button("get information about Payment:")
    if Payment:
        st.markdown("""Payment used by customer for purchase (3 methods are avail
        able – Cash, Credit card and Ewallet)""")
    COGS=st.button("get information about COGS:")
    if COGS:
        st.markdown("""Cost of goods sold""")
    Gross_margin_percentage=st.button("get information about Gross_margin_percentage:")
    if Gross_margin_percentage:
        st.markdown(""" Gross margin percentage""")
    Gross_income=st.button("get information about Gross_income:")
    if Gross_income:
        st.markdown("""  Gross income""")
    Rating=st.button("get information about Rating:")
    if Rating:
        st.markdown(""" Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)""")
    
    df=pd.read_csv('supermarkt_salesnew.csv')
    df.drop('Unnamed: 0',axis=1,inplace=True)
    df['hour']=pd.to_datetime(df['Time'],format="%H:%M").dt.hour
    df.drop('Time',axis=1,inplace=True)
    st.subheader("***Data market_sales :***")
    bt=st.button("display data")
    if bt:
        st.dataframe(df)
    st.subheader("***Upload file :***")
    if st.button('Download Data'):
        # Create a link to download the data
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    home()
#The line if __name__ == "__main__": is a common Python idiom that checks 
# whether the current script is being executed as the main module.
# In Python, when you run a script directly using the python command,
#  the special variable __name__ is set to "__main__" for that script. On the other hand, 
# if a script is imported as a module into another script, the __name__ variable is set to the name of the module.
