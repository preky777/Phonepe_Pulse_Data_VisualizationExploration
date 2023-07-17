import io
import pandas as pd
import streamlit as st
from PIL import Image
import mysql.connector
import plotly.express as px

# Set page title
st.title("APPLICATION")
st.write("----")
# PhonePe Image and Description
st.image(Image.open("C:\\Users\\prajw\\OneDrive\\Desktop\\phone2\\images_phonepe\\phonepe.png"), width=300)
st.subheader("PhonePe is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari, and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
st.video("C:\\Users\\prajw\\OneDrive\\Desktop\\phone2\\images_phonepe\\upi.mp4")
