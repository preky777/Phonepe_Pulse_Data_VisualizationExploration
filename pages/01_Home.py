import io
import pandas as pd
import streamlit as st
from PIL import Image
import mysql.connector
import plotly.express as px

#----------------Home----------------------#
conn = mysql.connector.connect(
                               host="localhost",
                               user="root",
                               password="rp#$9882",
                               database="phonepe_pulse"
                               )

cursor = conn.cursor()


# execute a SELECT statement
cursor.execute("SELECT * FROM agg_trans")

# fetch all rows
rows = cursor.fetchall()

col1,col2, = st.columns(2)
col1.image(Image.open("C:\\Users\\prajw\\OneDrive\\Desktop\\phonep\\Phonepe_images\\phonepe.png"),width = 300)
with col1:
    st.subheader("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
    st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
with col2:
    st.video("C:\\Users\\prajw\\OneDrive\\Desktop\\phonep\\Phonepe_images\\upi.mp4")
        
        
df = pd.DataFrame(rows, columns=['States', 'Transaction_Year', 'Quarters', 'Transaction_Type', 'Transaction_Count','Transaction_Amount','Reigons'])
fig = px.choropleth(df, locations="States", scope="asia", color="States", hover_name="States",
        title="Live Geo Visualization of India")
st.plotly_chart(fig)
cursor.close()
conn.close()