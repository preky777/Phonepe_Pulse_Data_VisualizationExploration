import io
import pandas as pd
import streamlit as st
from PIL import Image
import mysql.connector
import plotly.express as px
#---------------------Basic Insights -----------------#
conn = mysql.connector.connect(
                               host="localhost",
                               user="root",
                               password="rp#$9882",
                               database="phonepe_pulse"
                               )

cursor = conn.cursor()


st.title("BASIC INSIGHTS")
st.write("----")
st.subheader("Let's know some basic insights about the data")
options = ["--select--",
            "Top 10 State based on year and amount of transaction",
            "List 10 State based on type and amount of transaction",
            "Top 5 Transaction_type based on Transaction_amount",
            "Top 10 Registered-users based on State and District",
            "Top 10 Districts based on State and Count of transaction",
            "List 10 Districts based on State and amount of transaction",
            "List 10 Transaction_count based on Districts and State",
            "Top 10 Registered_users based on State and District"]
    
            #1
               
select = st.selectbox("Select the option",options)
if select=="Top 10 State based on year and amount of transaction":
    cursor.execute("SELECT DISTINCT State, Year, SUM(Transaction_amount) AS Total_Transaction_amount FROM top_trans_dist GROUP BY State, Year ORDER BY Total_Transaction_amount DESC LIMIT 10");
        
    df = pd.DataFrame(cursor.fetchall(), columns=['State','Year', 'Transaction_amount'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 10 State and amount of transaction")
        st.bar_chart(data=df,x="Transaction_amount",y="State")
            
        #2
            
elif select=="List 10 State based on type and amount of transaction":
    cursor.execute("SELECT DISTINCT State, SUM(Transaction_count) as Total FROM top_trans_pin GROUP BY State ORDER BY Total ASC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','Total_Transaction'])
    col1,col2 = st.columns(2)
    with col1:
         st.write(df)
    with col2:
        st.title("List 10 State based on type and amount of transaction")
        st.bar_chart(data=df,x="Total_Transaction",y="State")
            
        #3
            
elif select=="Top 5 Transaction_type based on Transaction_amount":
    cursor.execute("SELECT DISTINCT Transaction_type, SUM(Transaction_amount) AS Amount FROM agg_user GROUP BY Transaction_type ORDER BY Amount DESC LIMIT 5");
    df = pd.DataFrame(cursor.fetchall(),columns=['Transaction_type','Transaction_amount '])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 5 Transaction_type based on Transaction_amount")
        st.bar_chart(data=df,x="Transaction_type",y="Amount")
            
        #4
            
elif select=="Top 10 Registered-users based on State and District":
    cursor.execute("SELECT DISTINCT State, District, SUM(Registered_users) AS Users FROM top_user_dist GROUP BY State, District ORDER BY Users DESC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Registered_users'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 10 Registered-users based on State and District")
        st.bar_chart(data=df,x="State",y="Registered_users")
            
        #5
            
elif select=="Top 10 Districts based on State and Count of transaction":
    cursor.execute("SELECT DISTINCT State,District,SUM(Transaction_count) AS Counts FROM map_trans GROUP BY State,District ORDER BY Counts DESC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_count'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 10 Districts based on State and Count of transaction")
        st.bar_chart(data=df,x="State",y="Transaction_count")
            
        #6
            
elif select=="List 10 Districts based on State and amount of transaction":
    cursor.execute("SELECT DISTINCT State,Year,SUM(Transaction_amount) AS Amount FROM agg_trans GROUP BY State, Year ORDER BY Amount ASC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','Year','Transaction_amount'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Least 10 Districts based on State and amount of transaction")
        st.bar_chart(data=df,x="State",y="Transaction_amount")
            
        #7
            
elif select=="List 10 Transaction_count based on Districts and State":
    cursor.execute("SELECT DISTINCT State, District, SUM(Transaction_count) AS Counts FROM map_trans GROUP BY State,District ORDER BY Counts ASC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_count'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("List 10 Transaction_count based on Districts and State")
        st.bar_chart(data=df,x="State",y="Transaction_count")
            
        #8
             
elif select=="Top 10 Registered_users based on State and District":
    cursor.execute("SELECT DISTINCT State,District, SUM(Registered_users) AS Users FROM map_user GROUP BY State,District ORDER BY Users DESC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns = ['State','District','Registered_users'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 10 Registered_users based on State and District")
        st.bar_chart(data=df,x="State",y="Registered_users")
cursor.close()
conn.close()