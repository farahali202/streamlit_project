import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import seaborn as sns
def project():
        from contact import contact
        from prediction import prediction
        from home import home
# Run the app
        st.title("Dashboard supermarkt sales of data")
        @st.cache
        def get_data():
                        df=pd.read_csv('supermarkt_salesnew.csv')
                        df.drop('Unnamed: 0',axis=1,inplace=True)
                        df['hour']=pd.to_datetime(df['Time'],format="%H:%M").dt.hour
                        df.drop('Time',axis=1,inplace=True)
                        return df
            #to prevent streamlit to not return our entire script and load dataframe  again and again and agin--solution
            #we can avoid this by caching the dataframe(into a shortterm memory)   
        df=get_data()
            #df=pd.read_csv('supermarkt_sales.csv')
            #df['hour']=pd.to_datetime(df['Time'],format="%H:%M").dt.hour

            #authenticator.logout("Logout",'sidebar')
            #st.sidebar.title(f"Welcome {name}")
            #sidebar
        st.sidebar.header('Please Filter Here:')
        City=st.sidebar.multiselect('Select City: ',options=df['City'].unique(),default=df['City'].unique())

        Customer_type=st.sidebar.multiselect('Select Customer_type: ',options=df['Customer_type'].unique(),default=df['Customer_type'].unique())

        Gender=st.sidebar.multiselect('Select Gender: ',options=df['Gender'].unique(),default=df['Gender'].unique())

        df_selection=df.query(
                'City == @City & Customer_type==@Customer_type & Gender==@Gender'
            )
        st.dataframe(df_selection)


            #display KPI's(MAINPAGE)
        st.title(":bar_chart: Sales Dashboard")
        st.markdown("##")##use other paragraph

            #top KPi's
        total_sales=round(df_selection['Total'].sum(),2)

        
        aver_rat=round(df_selection['Rating'].mean(),1)
        star_rating=":star:" * int(round(aver_rat,0))
        average_sale_by_transaction=round(df_selection['Total'].mean(),2)
    #display
        left_column,middle_column,right_column=st.columns(3)

        with left_column:
                st.subheader('Total Sales:')
                st.subheader(f' {total_sales} $')
        with middle_column:
                st.subheader('Average Rating:')
                st.subheader(f"{aver_rat}{star_rating}")
        with right_column:
                st.subheader('Average Sales Per Transaction :')
                st.subheader(f"{average_sale_by_transaction}$")

        st.markdown('---')

        st.subheader("**City**")
        revenue_by_City = df_selection.groupby(by=['City']).sum()[['Total']]

        fig = px.bar(revenue_by_City, x='Total', y=revenue_by_City.index,
             title='Sales Revenue by City',template='plotly_white',
                color_discrete_sequence=["#C18173 "]*len(revenue_by_City))

        fig.update_layout(xaxis_title='City', yaxis_title='Total Revenue')
        st.plotly_chart(fig,use_container_width=True)

        data=(df_selection.groupby('City')[['Unit price','Quantity','Total']].sum()).sort_values(by='Total')
        left_column,right_column=st.columns(2)

        with left_column:
                st.dataframe(data)
        with right_column:
                st.subheader("Notice")
                st.markdown("""
                The supermarket in Naypyitaw has higher sales compared to the markets in Mandalay and Yangon.
                """)


        st.markdown('---')

        st.subheader("**Customer type**")

        fig_c = px.histogram(df_selection, x="Customer_type", color="Branch", title='Branch by customer', 
                             
                    color_discrete_map={"Supermarket Type1": "#C18173", "Supermarket Type2": "#7F7F7F", "Supermarket Type3": "#1F77B4"},
                    histfunc="count",
                     nbins=10,
                     width=800, height=500)
        fig_c.update_layout(xaxis_title='Customer type', yaxis_title='Branch')

        left_column, right_column = st.columns(2)
        with left_column:
                left_column.plotly_chart(fig_c,use_container_width=True)
        with right_column:
            st.subheader("Notice")
            st.markdown(""" The regular customers tend to make more purchases in Branch A and B, while the members make purchases in all branches equally.
    """) 
        st.markdown('---')

        st.subheader("**Branch and Rating**")

        fig_B = px.box(df_selection, x="Branch", y="Rating", title="Ratings by Branch",color="Branch")

        fig_B.update_layout(xaxis_title='Branch', yaxis_title='Rating')

        left_column, right_column = st.columns(2)
        with left_column:
                left_column.plotly_chart(fig_B,use_container_width=True)
        with right_column:
            st.subheader("Notice")
            st.markdown(""" Branch B has the lowest rating among all the branches
    """)
            
        st.markdown('---')

        st.subheader("***Product Analysis***")
        st.markdown("""Let's look at the various products' performance.""")

            #visualization:
        sales=(df_selection.groupby(by=['Product line']).sum()[['Total'] ].sort_values(by='Total'))

        fig_prod=px.bar(
                sales,
                x='Total',
                y=sales.index,
                orientation='h',
                title="<b>Sales by product</b>",
                template='plotly_white',
                color_discrete_sequence=["#C18173 "]*len(sales),

            )
            #kifach nhyed backgroung limora barchart

        fig_prod.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=(dict(showgrid=False))
            )

            #second plot(sales by hour)
        sales_hour=df_selection.groupby(by=['hour']).sum()[['Total']]
        fig_hour=px.bar(
                sales_hour,
                x=sales_hour.index,
                y='Total',
                title="<b>Sales by Hours</b>",
                color_discrete_sequence=["#C18173 "]*len(sales_hour),
                template="plotly_white",
            )
        fig_hour.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(tickmode='linear'),
                yaxis=(dict(showgrid=False)),)
        left_column,right_column=st.columns(2)

        with left_column:
                left_column.plotly_chart(fig_hour,use_container_width=True)
        with right_column:
                right_column.plotly_chart(fig_prod,use_container_width=True)

        boxenplot = px.box(df_selection, x='Rating', y='Product line', title='Ratings by Product Line',color="Product line")

# Update layout and axis labels
        boxenplot.update_layout(
    xaxis_title='Rating',
    yaxis_title='Product Line',
    title='Ratings by Product Line'
)
        left_column,right_column=st.columns(2)

        with left_column:
                left_column.plotly_chart(boxenplot,use_container_width=True)
        with right_column:
                st.subheader("Notice")
                st.markdown(""" Food and Beverages have the highest average rating while sports and travel the lowest


    """)
                

        st.markdown('---')

        st.subheader("**Payment Channel**")
        st.markdown("""How customers make payment in this business""")

        fig_p= px.histogram(df_selection, x="Payment", color="Payment", title='Payment Channel', 
                             
                    color_discrete_map={"Supermarket Type1": "#C18173", "Supermarket Type2": "#7F7F7F", "Supermarket Type3": "#1F77B4"},
                    histfunc="count",
                     nbins=10,
                     width=800, height=500)
        fig_p.update_layout(xaxis_title='Payment', yaxis_title='count')
        fig_b = px.histogram(df_selection, x="Payment", color="Branch",title='Payment by Branch', 
                    color_discrete_map={"Supermarket Type1": "#C18173", "Supermarket Type2": "#7F7F7F", "Supermarket Type3": "#1F77B4"},
                    histfunc="count",
                     nbins=10,
                     width=800, height=500)
        fig_b.update_layout(xaxis_title='Payment', yaxis_title='count')

        left_column, right_column = st.columns(2)
        with left_column:
                st.plotly_chart(fig_p,use_container_width=True)
        with right_column:
                st.plotly_chart(fig_b,use_container_width=True)
        
                
        st.subheader("Notice")
        st.markdown(""" Most of the customers prefer to pay through Ewallet and Cash Payment, while fewer of them choose to pay with their credit card
    """) 
        
        st.markdown('---')

        st.header("**Correlations between values**")
        left_column, right_column = st.columns(2)
        with left_column:
                st.subheader("**Correlation Matrix:**")
                numeric_columns = df_selection.select_dtypes(include='number')
                correlation_matrix = numeric_columns.corr()
                st.dataframe(correlation_matrix)
        with right_column:
                st.subheader("**CONCLUSION:**")
                st.markdown(""" 

1-Unit price, Quantity, Tax 5%, Total, cogs, and gross income are highly positively correlated with each other. This indicates that these variables have a strong linear relationship and tend to increase or decrease together.

2-Rating has a weak negative correlation with Unit price, Quantity, Tax 5%, Total, cogs, gross income, and hour. This suggests that as the rating decreases, these variables may slightly decrease as well.

2-There is a weak positive correlation between hour and Unit price, indicating a slight tendency for the unit price to increase with the hour.

3-The variable "gross margin percentage" has missing values (NaN) and does not contribute to the correlation analysis.


    """)





        

            #styling:remove streamlit icone
        hide_style="""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
        st.markdown(hide_style,unsafe_allow_html=True)
if __name__ == "__main__":
        project()
        
    