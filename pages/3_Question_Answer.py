import io
import pandas as pd
import streamlit as st
from PIL import Image
import mysql.connector
import plotly.express as px
import matplotlib.pyplot as plt
import json
#---------------------Basic Insights -----------------#
conn = mysql.connector.connect(
                               host="localhost",
                               user="root",
                               password="rp#$9882",
                               database="phonepe_analysis"
                               )

cursor = conn.cursor()


st.title("Few Questions and Answers")
st.write("----")
st.subheader("Few questions and answers related to the phonepe pulse data")
options = ["--select--",
            "Top 10 State based on year and amount of transaction",
            "Least 10 State based on type and amount of transaction",
            "Top 5 Transaction_type based on Transaction_amount",
            "Top 10 Registered-users based on State and District",
            "Top 10 Districts based on State and Count of transaction",
            "Least 10 Districts based on State and amount of transaction",
            "Least 10 Transaction_count based on Districts and State",
            "Top 10 Registered_users based on State and District"]
    
            #1
               
select = st.selectbox("Select the option",options)
if select=="Top 10 State based on year and amount of transaction":
    cursor.execute("SELECT DISTINCT State, Year, SUM(Transaction_amount) AS Total_Transaction_amount FROM top_trans GROUP BY State, Year ORDER BY Total_Transaction_amount DESC LIMIT 10");
        
    df = pd.DataFrame(cursor.fetchall(), columns=['State','Year', 'Transaction_amount'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 10 State and amount of transaction")
        chart_data = df.sort_values('Transaction_amount', ascending=False)
        chart = chart_data.plot(kind='barh', x='State', y='Transaction_amount', legend=False)
        chart.set_xlabel("Transaction Amount")
        chart.set_ylabel("State")
        chart.set_title("Top 10 States and Amount of Transaction")
        chart.set_yticklabels(chart.get_yticklabels(), rotation=45)  # Rotate x-axis labels
        st.pyplot(plt)
            
        #2
            
elif select=="Least 10 State based on type and amount of transaction":
    cursor.execute("SELECT DISTINCT State, SUM(Transaction_count) as Total FROM top_trans GROUP BY State ORDER BY Total ASC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','Total_Transaction'])
    col1,col2 = st.columns(2)
    with col1:
         st.write(df)
    with col2:
        st.title("Least 10 State based on type and amount of transaction")
        df['Total_Transaction'] = pd.to_numeric(df['Total_Transaction'])  # Convert to numeric
        chart_data = df.sort_values('Total_Transaction', ascending=False)
        chart = chart_data.plot(kind='barh', x='State', y='Total_Transaction', legend=False)
        chart.set_xlabel("Total_Transaction")
        chart.set_ylabel("State")
        chart.set_title("Least 10 State based on type and amount of transaction")
        chart.set_yticklabels(chart.get_yticklabels(), rotation=45)  # Rotate x-axis labels
        st.pyplot(plt)
            
        #3
            
elif select=="Top 5 Transaction_type based on Transaction_amount":
    cursor.execute("SELECT DISTINCT Transaction_type, SUM(Transaction_amount) AS Amount FROM agg_trans GROUP BY Transaction_type ORDER BY Amount DESC LIMIT 5");
    df = pd.DataFrame(cursor.fetchall(),columns=['Transaction_type','Transaction_amount'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 5 Transaction_type based on Transaction_amount")
        chart_data = df.sort_values('Transaction_amount', ascending=False)
        chart = chart_data.plot(kind='barh', x='Transaction_type', y='Transaction_amount', legend=False)
        chart.set_xlabel("Transaction Amount")
        chart.set_ylabel("Transaction_type")
        chart.set_title("Top 5 Transaction_type based on Transaction_amount")
        chart.set_yticklabels(chart.get_yticklabels(), rotation=45)  # Rotate x-axis labels
        st.pyplot(plt)
            
        #4
            
elif select=="Top 10 Registered-users based on State and District":
    cursor.execute("SELECT DISTINCT State, Districts, SUM(Registered_users) AS Users FROM top_user GROUP BY State, Districts ORDER BY Users DESC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','Districts','Registered_users'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 10 Registered-users based on State and District")
        df['Registered_users'] = pd.to_numeric(df['Registered_users'])  # Convert to numeric
        chart_data = df.sort_values('Registered_users', ascending=False)
        chart = chart_data.plot(kind='barh', x='State', y='Registered_users', legend=False)
        chart.set_xlabel("Registered_users")
        chart.set_ylabel("State")
        chart.set_title("Top 10 Registered-users based on State and District")
        chart.set_yticklabels(chart.get_yticklabels(), rotation=45)  # Rotate x-axis labels
        st.pyplot(plt)

           
        #5
            
elif select=="Top 10 Districts based on State and Count of transaction":
    cursor.execute("SELECT DISTINCT State,District,SUM(Count) AS Counts FROM map_trans GROUP BY State,District ORDER BY Counts DESC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Count'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 10 Districts based on State and Count of transaction")
        df['Count'] = pd.to_numeric(df['Count'])  # Convert to numeric
        chart_data = df.sort_values('Count', ascending=False)
        chart = chart_data.plot(kind='barh', x='State', y='Count', legend=False)
        chart.set_xlabel("Count")
        chart.set_ylabel("State")
        chart.set_title("Top 10 Districts based on State and Count of transaction")
        chart.set_yticklabels(chart.get_yticklabels(), rotation=45)  # Rotate x-axis labels
        st.pyplot(plt)
            
        #6
            
elif select=="Least 10 Districts based on State and amount of transaction":
    cursor.execute("SELECT DISTINCT State,Year,SUM(Transaction_amount) AS Amount FROM agg_trans GROUP BY State, Year ORDER BY Amount ASC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','Year','Transaction_amount'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Least 10 Districts based on State and amount of transaction")
        chart_data = df.sort_values('Transaction_amount', ascending=False)
        chart = chart_data.plot(kind='barh', x='State', y='Transaction_amount', legend=False)
        chart.set_xlabel("Transaction Amount")
        chart.set_ylabel("State")
        chart.set_title("Least 10 Districts based on State and amount of transaction")
        chart.set_yticklabels(chart.get_yticklabels(), rotation=45)  # Rotate x-axis labels
        st.pyplot(plt)
            
        #7
            
elif select=="Least 10 Transaction_count based on Districts and State":
    cursor.execute("SELECT DISTINCT State, District, SUM(Count) AS Counts FROM map_trans GROUP BY State,District ORDER BY Counts ASC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Count'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Least 10 Transaction_count based on Districts and State")
        df['Count'] = pd.to_numeric(df['Count'])  # Convert to numeric
        chart_data = df.sort_values('Count', ascending=False)
        chart = chart_data.plot(kind='barh', x='State', y='Count', legend=False)
        chart.set_xlabel("Count")
        chart.set_ylabel("State")
        chart.set_title("Least 10 Transaction_count based on Districts and State")
        chart.set_yticklabels(chart.get_yticklabels(), rotation=45)  # Rotate x-axis labels
        st.pyplot(plt)
            
        #8
             
elif select=="Top 10 Registered_users based on State and District":
    cursor.execute("SELECT DISTINCT State,District, SUM(Registered_user) AS Users FROM map_users GROUP BY State,District ORDER BY Users DESC LIMIT 10");
    df = pd.DataFrame(cursor.fetchall(),columns = ['State','District','Registered_user'])
    col1,col2 = st.columns(2)
    with col1:
        st.write(df)
    with col2:
        st.title("Top 10 Registered_users based on State and District")
        df['Registered_user'] = pd.to_numeric(df['Registered_user'])  # Convert to numeric
        chart_data = df.sort_values('Registered_user', ascending=False)
        chart = chart_data.plot(kind='barh', x='State', y='Registered_user', legend=False)
        chart.set_xlabel("Registered_user")
        chart.set_ylabel("State")
        chart.set_title("Top 10 Registered-users based on State and District")
        chart.set_yticklabels(chart.get_yticklabels(), rotation=45)  # Rotate x-axis labels
        st.pyplot(plt)
cursor.close()
conn.close()