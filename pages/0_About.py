import io
import pandas as pd
import streamlit as st
from PIL import Image



#----------------About-----------------------#


col1,col2 = st.columns(2)
with col1:
    st.image('Phonepe_images/pulse.gif', use_column_width = True)
with col2:
    st.image('Phonepe_images/PhonePe_Logo.jpg',width = 500)
    st.write("---")
    st.subheader("The Indian digital payments story has truly captured the world's imagination."
                " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
st.write("---")
col1,col2 = st.columns(2)
with col1:
    st.title("THE BEAT OF PHONEPE")
    st.write("---")
    st.subheader("Phonepe became a leading digital payments company")
    st.image('Phonepe_images/top.jpeg',width = 400)
    with open("C:\\Users\\prajw\\OneDrive\\Desktop\\phonep\\annual report.pdf","rb") as f:
        data = f.read()
    st.download_button("DOWNLOAD REPORT",data,file_name="annual report.pdf")
with col2:
    st.image('Phonepe_images/report.jpeg',width = 800)
