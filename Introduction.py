import io
import pandas as pd
import streamlit as st
from PIL import Image

# Set page title
st.title("INTRODUCTION")
st.write("----")
# PhonePe Pulse GIF
st.image('images_phonepe/Pulse.gif', use_column_width=True)

# PhonePe Logo
st.image('images_phonepe/PhonePe_Logo.jpg', width=500)

# Description
st.subheader("The Indian digital payments story has truly captured the world's imagination."
             " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
             " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
             "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
st.write("---")

# THE BEAT OF PHONEPE
st.title("THE BEAT OF PHONEPE")
st.write("---")

# PhonePe Image
st.image('images_phonepe/top.jpeg', width=400)

# Download Annual Report
with open("C:\\Users\\prajw\\OneDrive\\Desktop\\phone3\\annual report.pdf", "rb") as f:
    data = f.read()
st.download_button("DOWNLOAD REPORT", data, file_name="annual report.pdf")

# Report Image
st.image('images_phonepe/report.jpeg', width=800)