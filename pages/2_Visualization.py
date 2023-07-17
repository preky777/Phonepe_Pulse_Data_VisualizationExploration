import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import requests
import json
import os
import sqlalchemy
import mysql.connector as mysql
from mysql.connector import Error
import streamlit as st
import plotly.express as px
from  PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots

mydb = mysql.connect(host="localhost",
                   user="root",
                   password="rp#$9882",
                   database= "phonepe_visualization"
                  )
mycursor = mydb.cursor(buffered=True)


def set_page_config():
    
  st.set_page_config(
      page_title="Visualization",
      page_icon="chart_with_upwards_trend"
    
    )
  st.title("VISUALIZATION")
  st.write("----")
  st.subheader("select topic from the menu to visualize")

def selection():
   
     selected = st.selectbox("Menu", ["map_analysis","transaction_analysis","users_analysis","overall_analysis","top_analysis"], 
                           
                            index=0,
                            key="menu",
                            help="Select an option from the menu")
    
     return selected
                       
            


table_name = 'agg_trans'
query = f"SELECT * FROM {table_name}"

mycursor.execute(query)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
Data_Aggregated_Transaction_df = pd.DataFrame(data, columns=columns)


table_n = 'map_trans'
q = f"SELECT * FROM {table_n}"

mycursor.execute(q)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
Data_Map_Transaction_df = pd.DataFrame(data, columns=columns)



table_n1 = 'agg_users'
q1 = f"SELECT * FROM {table_n1}"

mycursor.execute(q1)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
Data_Aggregated_User_df = pd.DataFrame(data, columns=columns)



table_n2 = 'map_users'
q2 = f"SELECT * FROM {table_n2}"

mycursor.execute(q2)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
Data_Map_User_Table = pd.DataFrame(data, columns=columns)







table_n4 = 'longitude_latitude_state_table'
q4 = f"SELECT * FROM {table_n4}"

mycursor.execute(q4)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
long_lat_df = pd.DataFrame(data, columns=columns)



table_n5 = 'districts_longitude_latitude_table'
q5 = f"SELECT * FROM {table_n5}"

mycursor.execute(q5)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
dist_long_lat_df = pd.DataFrame(data, columns=columns)


table_n6 = 'top_user'
q6 = f"SELECT * FROM {table_n6}"
mycursor.execute(q6)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
tudf = pd.DataFrame(data, columns=columns)


table_n7 = 'top_trans'
q7 = f"SELECT * FROM {table_n7}"
mycursor.execute(q7)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
ttdf = pd.DataFrame(data, columns=columns)


table_n8 = 'agg_urs_sum'
q8 = f"SELECT * FROM {table_n8}"
mycursor.execute(q8)
columns = [column[0] for column in mycursor.description]
data = mycursor.fetchall()
Data_Aggregated_User_Summary_df = pd.DataFrame(data, columns=columns)









def ma():
    query1 = 'select * from agg_trans'
    df = Data_Aggregated_Transaction_df
    query2 = 'select * from longitude_latitude_state_table'
    state = long_lat_df
    query3 = 'select * from districts_longitude_latitude_table'
    districts = dist_long_lat_df
    query4 = 'select * from map_trans'
    districts_tran = Data_Map_Transaction_df
    query5 = 'select * from map_users'
    app_opening = Data_Map_User_Table
    query6 = 'select * from agg_users'
    user_device = Data_Aggregated_User_df


    state = state.sort_values(by='state')
    state = state.reset_index(drop=True)
    df2 = df.groupby(['State']).sum()[['Transaction_count', 'Transaction_amount']]
    df2 = df2.reset_index()

    choropleth_data = state.copy()

    for column in df2.columns:
        choropleth_data[column] = df2[column]
    choropleth_data = choropleth_data.drop(labels='State', axis=1)

    df.rename(columns={'State': 'state'}, inplace=True)
    sta_list = ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                'uttarakhand', 'west-bengal']
    state['state'] = pd.Series(data=sta_list)
    state_final = pd.merge(df, state, how='outer', on='state')
    districts_final = pd.merge(districts_tran, districts,
                            how='outer', on=['State', 'District'])
    
    st.subheader(':violet[Transaction analysis->State and Districtwise:]')
    st.write(' ')
    c1,c2=st.columns([1,1])
    with c1:
        Year = st.radio('Please select the Year',
                    ('2018', '2019', '2020', '2021', '2022'))
    with c2:
        Quarter = st.radio('Please select the Quarter',
                       ('1', '2', '3', '4'))
    
    st.write(' ')
    Year = int(Year)
    Quarter = int(Quarter)
    plot_district = districts_final[(districts_final['Year'] == Year) & (
        districts_final['Quarter'] == Quarter)]
    plot_state = state_final[(state_final['Year'] == Year)
                             & (state_final['Quarter'] == Quarter)]
    plot_state_total = plot_state.groupby(
        ['state', 'Year', 'Quarter', 'Latitude', 'Longitude']).sum()
    plot_state_total = plot_state_total.reset_index()
    state_code = ['AN', 'AD', 'AR', 'AS', 'BR', 'CH', 'CG', 'DNHDD', 'DL', 'GA',
                  'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH',
                  'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TS',
                  'TR', 'UP', 'UK', 'WB']
    plot_state_total['code'] = pd.Series(data=state_code)
    # ------------------------------------------- Geo-visualization of transacion data ------------------------------------------------------
    fig1 = px.scatter_geo(plot_district,
                          lon=plot_district['Longitude'],
                          lat=plot_district['Latitude'],
                          color=plot_district['Amount'],
                          size=plot_district['Count'],
                          hover_name="District",
                          hover_data=["State", 'Amount', 'Amount',
                                      'Count', 'Year', 'Quarter'],
                          title='District',
                          size_max=22,)
    fig1.update_traces(marker={'color': "#CC0044",
                               'line_width': 1})
    fig2 = px.scatter_geo(plot_state_total,
                          lon=plot_state_total['Longitude'],
                          lat=plot_state_total['Latitude'],
                          hover_name='state',
                          text=plot_state_total['code'],
                          hover_data=['Transaction_count',
                                      'Transaction_amount', 'Year', 'Quarter'],
                          )
    fig2.update_traces(marker=dict(color="#D5FFCC", size=0.3))
    fig = px.choropleth(
        choropleth_data,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='Transaction_amount',
        color_continuous_scale='twilight',
        hover_data=['Transaction_count', 'Transaction_amount']
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.add_trace(fig1.data[0])
    fig.add_trace(fig2.data[0])
    st.write("### **:blue[PhonePe India Map]**")
    fig.update_layout(height=500, width=1000)
    st.plotly_chart(fig,use_container_width=True)



    # Create the 'Show Bar Graph' button
    show_bar_graph = st.button('Show The Bar Graphs')

    if show_bar_graph:
        # Extract the required data for the transaction amount bar graph
        plot_state_total_grouped_amount = plot_state_total.groupby('state').sum().sort_values('Transaction_amount')
        states_amount = plot_state_total_grouped_amount.index.tolist()
        transaction_amounts = plot_state_total_grouped_amount['Transaction_amount'].tolist()

        # Create the transaction amount bar graph
        fig_amount = go.Figure(data=go.Bar(x=states_amount, y=transaction_amounts))
        fig_amount.update_layout(xaxis_title='State', yaxis_title='Transaction Amount',
                                title='PhonePe Transactions by State (Increasing Order - Amount)')

        # Extract the required data for the transaction count bar graph
        plot_state_total_grouped_count = plot_state_total.groupby('state').sum().sort_values('Transaction_count')
        states_count = plot_state_total_grouped_count.index.tolist()
        transaction_counts = plot_state_total_grouped_count['Transaction_count'].tolist()

        # Create the transaction count bar graph
        fig_count = go.Figure(data=go.Bar(x=states_count, y=transaction_counts))
        fig_count.update_layout(xaxis_title='State', yaxis_title='Transaction Count',
                                title='PhonePe Transactions by State (Increasing Order - Count)')

        # Display the bar graphs
        st.plotly_chart(fig_amount)
        st.plotly_chart(fig_count)

def tr_a():
    st.write('# :blue[TRANSACTIONS ANALYSIS]')
    tab1, tab2, tab3, tab4 = st.tabs(["PAYMENT ANALYSIS", "STATE ANALYSIS", "DISTRICT ANALYSIS", "YEAR ANALYSIS"])
    #==================================================T FIGURE1 STATE ANALYSIS=======================================================

    with tab2:
        st.subheader(':violet[Transaction analysis->Statewise:]')
        a1,a2,a3,a4=st.columns([2,1,1,1])
        with a1:
            transac_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                            'uttarakhand', 'west-bengal'), index=10, key='transac')
        with a2:
            transac__quater = int(st.radio('Please select the Quarter',
                                    ('1', '2', '3', '4'), key='trans_quater'))
        with a3:
            transac_type = st.radio('Please select the Mode',
                                    ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services', 'Others'), key='transactype')
        with a4:
            transac_values = st.radio('Please select the values to visualize', 
                                      ('Transaction_count', 'Transaction_amount'), key='transacvalues')

            

        #payment_mode_yearwise = pd.read_csv('csv/Agg_Trans.csv', index_col=0)

        querypay_year = 'select * from agg_transaction_table'
        payment_mode_yearwise = Data_Aggregated_Transaction_df

        new_df = payment_mode_yearwise.groupby(
            ['State', 'Year', 'Quarter', 'Transaction_type']).sum()
        new_df = new_df.reset_index()
        chart = new_df[(new_df['State'] == transac_state) &
                    (new_df['Transaction_type'] == transac_type) & (new_df['Quarter'] == transac__quater)]
        # ------------------------------- Bar chart analysis of transacion data statewise --------------------------------------------------------
        year_fig = px.bar(chart, x=['Year'], y=transac_values, color=transac_values, color_continuous_scale='Viridis',
                        title='Transaction analysis '+transac_state + ' regarding to '+transac_type)
        st.plotly_chart(year_fig)

    #=============================================T FIGURE2 DISTRICTS ANALYSIS=============================================
    with tab3:
        col1, col2, col3,col4= st.columns([1,1,1,1])
        with col2:
            Year =int(st.radio('Please select the Year',
                    ('2018', '2019', '2020', '2021', '2022'),key='y1'))
            
        with col1:
            transac_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                            'uttarakhand', 'west-bengal'), index=10, key='y2')
            

        with col3:
            transac__quater = int(st.radio('Please select the Quarter',
                                    ('1', '2', '3', '4'), key='y3'))
        with col4:
            transac_values = st.radio('Please select the values to visualize', 
                                      ('Count', 'Amount'), key='y4')
            
      
        payment_mode_distwise = Data_Map_Transaction_df

        new_df1 = payment_mode_distwise.groupby(
            ['State','District','Year','Quarter']).sum()
        new_df1 = new_df1.reset_index()
        chart1 = new_df1[(new_df1['State'] == transac_state) &
                    (new_df1['Year'] == Year) & (new_df1['Quarter'] == transac__quater)]
        # ------------------------------- Bar chart analysis of transaction data districtwise --------------------------------------------------------
        year_fig1 = px.bar(chart1, x='District', y=transac_values, color=transac_values, color_continuous_scale='Viridis',
                        title='Transaction analysis of the districts of '+transac_state)
        st.plotly_chart(year_fig1)

    #=============================================T FIGURE3 YEAR ANALYSIS===================================================
    with tab4:
        Data_Aggregated_Transaction=Data_Aggregated_Transaction_df.copy()
        Data_Aggregated_Transaction.drop(Data_Aggregated_Transaction.index[(Data_Aggregated_Transaction["State"] == "india")],axis=0,inplace=True)
        State_PaymentMode=Data_Aggregated_Transaction.copy()
        #st.write('### :green[PaymentMode and Year]')
        k1, k2,k3,k4= st.columns(4)
        with k3:
            M = st.radio(
                'Please select the Mode',
                ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services','Others'),key='D')
        with k1:
            Y = int(st.radio(
            'Please select the Year',
            ('2018', '2019', '2020','2021','2022'),key='F'))
        with k2:
            Q = int(st.radio('Please select the Quarter',
                                    ('1', '2', '3', '4'), key='H'))
        with k4:
            V = st.radio('Please select the values to visualize', 
                                      ('Transaction_count', 'Transaction_amount'), key='G')

        st.write(' ')
        st.write(' ')
        st.write(' ')
        


        new_df2 = payment_mode_yearwise.groupby(
            ['State', 'Year', 'Quarter', 'Transaction_type']).sum()
        new_df2 = new_df2.reset_index()
        chart2 = new_df2[(new_df2['Year'] == Y)&
                    (new_df2['Transaction_type'] == M) & (new_df2['Quarter'] == Q)]
        # ------------------------------- Bar chart analysis of transacion data statewise --------------------------------------------------------
        year_fig2 = px.bar(chart2, x='State', y=V, color=V, color_continuous_scale='Viridis',
                        title='Analysis of Year '+str(Y)+' and Quarter '+str(Q))
        st.plotly_chart(year_fig2)


    #=============================================T FIGURE4 PAY ANALYSIS=============================================
    with tab1:
        st.subheader(':violet[Payment type Analysis -> 2018 - 2022:]')
        payment_mode = Data_Aggregated_Transaction_df
        m1, m2,m3,m4= st.columns(4)
        with m1:
            pie_pay_mode_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                                'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                                'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                                'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                                'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                                'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                                'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                                'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                                'uttarakhand', 'west-bengal'), index=10, key='pie_pay_mode_state')
        with m2:
            pie_pay_mode_year = int(st.radio('Please select the Year',
                                        ('2018', '2019', '2020', '2021', '2022'),key='pie_pay_year'))
        with m3:
            pie_pay_mode__quater = int(st.radio('Please select the Quarter',
                                            ('1', '2', '3', '4'),key='pie_pay_quater'))
        with m4:
            pie_pay_mode_values = st.radio(
            'Please select the values to visualize', ('Transaction_count', 'Transaction_amount'),key='pie_pay_mode_val')

        pie_payment_mode = payment_mode[(payment_mode['Year'] == pie_pay_mode_year) & (
            payment_mode['Quarter'] == pie_pay_mode__quater) & (payment_mode['State'] == pie_pay_mode_state)]
        # -------------------------------- Pie chart analysis of Payment mode --------------------------------------------------------------------
        pie_pay_mode = px.pie(pie_payment_mode, values=pie_pay_mode_values,
                            names='Transaction_type', hole=.5, hover_data=['Year'])
        # ------------------------------------- Bar chart analysis of payment mode ----------------------------------------------------------------
        pay_bar = px.bar(pie_payment_mode, x='Transaction_type',
                        y=pie_pay_mode_values, color='Transaction_type')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write('# <span style="font-size:32px; color:green;">PIE CHART ANALYSIS</span>', unsafe_allow_html=True)
        st.plotly_chart(pie_pay_mode)
        with st.expander("See Bar graph for the same data"):
            st.plotly_chart(pay_bar)

def urs_a():
    st.write('# :blue[USERS DATA ANALYSIS ]')
    tab1, tab2, tab3, tab4 = st.tabs(["STATE ANALYSIS", "DISTRICT ANALYSIS","YEAR ANALYSIS","BRAND ANALYSIS"])

    # =================================================U STATE ANALYSIS ========================================================
    with tab1:
        st.write('### :green[State & Userbase]')
        n1, n2,n3= st.columns(3)
        with n1:
            state = st.selectbox(
                'Please select the State',
                ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
                'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
                'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
                'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                'uttarakhand', 'west-bengal'),key='W')
        with n2:
            Qr = int(st.radio('Please select the Quarter',
                                    ('1', '2', '3', '4'), key='X1'))
        with n3:
            T = st.radio(
            'Please select the values to visualize', ('Registered_user', 'App_opens'),key='X2')



        g = Data_Map_User_Table

        g1 = g.groupby(
            ['State', 'Year', 'Quarter']).sum()
        g1 = g1.reset_index()
        ch = g1[(g1['State'] == state) &
                    (g1['Quarter'] == Qr)]
        # ------------------------------- Bar chart analysis of transacion data statewise --------------------------------------------------------
        yf = px.bar(ch, x=['Year'], y=T, color=T, color_continuous_scale='Viridis',
                        title='User analysis of '+state)
        st.plotly_chart(yf)

    # ==================================================U DISTRICT ANALYSIS ====================================================
    with tab2:
        r1, r2, r3,r4= st.columns(4)
        with r2:
            Y1 = int(st.radio(
                'Please select the Year',
                ('2018', '2019', '2020', '2021', '2022'),key='y12'))
        with r1:
            s1 = st.selectbox(
            'Please select the State',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
            'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
            'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
            'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
            'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal'),key='dk2')
        with r3:
            Qr1 = int(st.radio(
                'Please select the Quarter',
                ('1', '2', '3','4'),key='qwe2'))
        
        with r4:
            T1 = st.radio(
            'Please select the values to visualize', ('Registered_user', 'App_opens'),key='X3')



        g2 = g.groupby(
            ['State','District','Year','Quarter']).sum()
        g2 = g2.reset_index()
        ch1 = g2[(g2['State'] == s1) &
                    (g2['Year'] == Y1) & (g2['Quarter'] == Qr1)]
        # ------------------------------- Bar chart analysis of transaction data districtwise --------------------------------------------------------
        yf1 = px.bar(ch1, x='District', y=T1, color=T1, color_continuous_scale='Viridis',
                        title='User analysis of the districts of '+s1)
        st.plotly_chart(yf1)

    # ==================================================U YEAR ANALYSIS ========================================================
    with tab3:
        st.write('### :orange[YEAR ANALYSIS] ')
        u1, u2, u3= st.columns(3)
        with u1:
            Y2 = int(st.radio(
                'Please select the Year',
                ('2018', '2019', '2020', '2021', '2022'),key='y123'))
            
        with u2:
            Qr2 = int(st.radio(
                'Please select the Quarter',
                ('1', '2', '3','4'),key='qwe23'))
        
        with u3:
            T2 = st.radio(
            'Please select the values to visualize', ('Registered_user', 'App_opens'),key='X4')



        g3 = g.groupby(
            ['State','Year','Quarter']).sum()
        g3 = g3.reset_index()
        ch2 = g3[
                    (g3['Year'] == Y2) & (g3['Quarter'] == Qr2)]
        # ------------------------------- Bar chart analysis of transaction data yrwise --------------------------------------------------------
        yf2 = px.bar(ch2, x='State', y=T2, color=T2, color_continuous_scale='Viridis',
                        title='User Analysis of Year '+str(Y2)+' and Quarter '+str(Qr2))
        st.plotly_chart(yf2)
    # ===================================================U BRAND ANALYSIS ====================================================

        with tab4:
            st.subheader(':violet[BRAND ANALYSIS:]')
            v1, v2, v3= st.columns(3)
            with v1:
                tree_map_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                                'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                                'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                                'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                                'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                                'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                                'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                                'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                                'uttarakhand', 'west-bengal'), index=10, key='tree_map_state')
            with v2:
                tree_map_state_year = int(st.radio('Please select the Year',
                                            ('2018', '2019', '2020', '2021', '2022'), key='tree_map_state_year'))
            with v3:
                tree_map_state_quater = int(st.radio('Please select the Quarter',
                                                ('1', '2', '3', '4'), key='tree_map_state_quater'))
            

            user_device=Data_Aggregated_User_df
            user_device_treemap = user_device[(user_device['State'] == tree_map_state) & (user_device['Year'] == tree_map_state_year) &
                                            (user_device['Quarter'] == tree_map_state_quater)]
            user_device_treemap['Count'] = user_device_treemap['Count'].astype(
                str)
            
            # ----------------------------------------- Treemap view of user device ----------------------------------------------------------------
            user_device_treemap_fig = px.treemap(user_device_treemap, path=['State', 'Brands'], values='Count', hover_data=['Year', 'Quarter','Percentage'],
                                                color='Brands',
                                                title='User device distribution in ' + tree_map_state +
                                                ' in ' + str(tree_map_state_year)+' at '+str(tree_map_state_quater)+' quater',)
            
            # ---------------------------------------- Barchart view of user device -----------------------------------------------------------------
            bar_user = px.bar(user_device_treemap, x='Brands', y='Count', color='Brands',
                            title='Bar chart analysis', color_continuous_scale='sunset',)
            st.plotly_chart(bar_user)

            # ---------------------------------------- Pie chart view of user device -----------------------------------------------------------------
            pie_user = px.pie(user_device_treemap, values='Count', names='Brands',
                            title='Pie chart analysis', color='Brands',
                            color_discrete_sequence=px.colors.qualitative.Set3)

            j1,j2=st.columns(2)
            with j1:
                with st.expander("Pie chart for the same data"):
                    st.plotly_chart(pie_user)
            with j2:
                with st.expander("Tree map for the same data"):
                    st.plotly_chart(user_device_treemap_fig)

def oa():
    Data_Aggregated_Transaction=Data_Aggregated_Transaction_df.copy()
    Data_Aggregated_Transaction.drop(Data_Aggregated_Transaction.index[(Data_Aggregated_Transaction["State"] == "india")],axis=0,inplace=True)

    st.markdown("<p style='font-size: 42px; color: orange;'>OVERALL TRANSACTIONS</p>", unsafe_allow_html=True)


    
    years=Data_Aggregated_Transaction.groupby('Year')
    years_List=Data_Aggregated_Transaction['Year'].unique()
    years_Table=years.sum()
    del years_Table['Quarter']
    years_Table['year']=years_List
    total_trans=years_Table['Transaction_count'].sum() # this data is used in sidebar 


    st.markdown("<p style='font-size: 30px; color: pink;'>LINE GRAPH ANALYSIS</p>", unsafe_allow_html=True)
    quarters = Data_Aggregated_Transaction.groupby(['Year', 'Quarter']).sum().reset_index()

    fg1 = px.line(quarters, x='Quarter', y='Transaction_count', color='Year',
                labels={'Quarter': 'Quarter', 'Transaction_count': 'Transaction Count'},
                title='Total Transaction count for each Quarter (2018 to 2022)')
    # Modify x-axis tick settings
    fg1.update_xaxes(tickmode='linear', dtick=1)
    st.write('### :green[Drastic Increase in Transaction count]')
    st.plotly_chart(fg1)



    fig1 = px.pie(years_Table, values='Transaction_count', names='year',color_discrete_sequence=px.colors.sequential.Viridis, title='TOTAL TRANSACTION COUNT (2018 TO 2022)')
    with st.expander("Pie chart for the same data"):
            st.write('### :green[Drastical Increase in Transaction count]')
            st.plotly_chart(fig1)



    fg2 = px.line(quarters, x='Quarter', y='Transaction_amount', color='Year',
                labels={'Quarter': 'Quarter', 'Transaction_amount': 'Transaction Amount'},
                title='Total Transaction amount for each Quarter (2018 to 2022)')
    # Modify x-axis tick settings
    fg2.update_xaxes(tickmode='linear', dtick=1)
    st.write('### :green[Drastic Increase in Transaction amount]')
    st.plotly_chart(fg2)


    fig2 = px.pie(years_Table, values='Transaction_amount', names='year',color_discrete_sequence=px.colors.sequential.Viridis, title='TOTAL TRANSACTION AMOUNT (2018 TO 2022)')
    with st.expander("Pie chart for the same data"):
            st.write('### :green[Drastical Increase in Transaction amount]')
            st.plotly_chart(fig2)

    


    with st.expander("Data Table"):
            st.write('#### :green[Year Wise Transaction Analysis in INDIA]')      
            st.markdown(years_Table.style.hide(axis="index").to_html(), unsafe_allow_html=True)


    

    st.markdown("<p style='font-size: 42px; color: orange;'>OVERALL USERS</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 30px; color: pink;'>LINE GRAPH ANALYSIS</p>", unsafe_allow_html=True)


    years = Data_Aggregated_User_Summary_df.groupby('Year')
    years_List = Data_Aggregated_User_Summary_df['Year'].unique()
    years_Table = years.sum()
    del years_Table['Quarter']
    years_Table['year'] = years_List
    total_trans = years_Table['Registered_Users'].sum()  # this data is used in sidebar

    quar = Data_Aggregated_User_Summary_df.groupby(['Year', 'Quarter']).sum().reset_index()

    # Create a line graph for Registered Users
    fgi1 = px.line(quar, x='Quarter', y='Registered_Users', color='Year',
                labels={'Quarter': 'Quarter', 'Registered_Users': 'Registered Users'},
                title='TOTAL REGISTERED USERS (2018 TO 2022)')

    # Create a line graph for App Openings
    
    fgi2 = px.line(quar, x='Quarter', y='AppOpenings', color='Year',
                labels={'Quarter': 'Quarter', 'AppOpenings': 'App Openings'},
                title='TOTAL APP OPENINGS (2018 TO 2022)')



    # Add line graphs and pie chart to the page
    # Modify x-axis tick settings
    fgi1.update_xaxes(tickmode='linear', dtick=1)
    fgi2.update_xaxes(tickmode='linear', dtick=1)
    st.write('### :green[Drastic Increase in Registered Users]')
    st.plotly_chart(fgi1)


    # Create pie chart for Registered Users
    pie_registered_users = px.pie(quar, values='Registered_Users', names='Year',
                                title='Percentage of Registered Users (2018 to 2022)')
    
    with st.expander("Pie chart for the same data"):
        st.plotly_chart(pie_registered_users)
    

    st.write('### :green[Drastic Increase in App Openings]')
    st.plotly_chart(fgi2)


    # Create pie chart for App Openings
    pie_app_openings = px.pie(quar, values='AppOpenings', names='Year',
                            title='Percentage of App Openings (2018 to 2022)')
    
    with st.expander("Pie chart for the same data"):
        st.plotly_chart(pie_app_openings)

    
    with st.expander("Data Table"):
        st.write('#### :green[Year Wise User Analysis in INDIA]')      
        st.markdown(years_Table.style.hide(axis="index").to_html(), unsafe_allow_html=True)


    




def topa():
    st.write('# :blue[TOP DATA ANALYSIS ]')
    t1, t2 = st.tabs(["STATE ANALYSIS", "DISTRICT ANALYSIS"])
    with t1:
            st.write('# :red[TOP 6 STATES DATA]')
            c1,c2=st.columns(2)
            with c1:
                Year = int(st.radio(
                        'Please select the Year',
                        ('2018', '2019','2020','2021','2022'),key='y1h2k'))
            with c2:
                Quarter = int(st.radio(
                        'Please select the Quarter',
                        ('1', '2', '3','4'),key='qgwe2'))
            Data_Map_User_df=Data_Aggregated_User_Summary_df.copy() 
            top_states=Data_Map_User_df.loc[(Data_Map_User_df['Year'] == int(Year)) & (Data_Map_User_df['Quarter'] ==int(Quarter))]
            top_states_r = top_states.sort_values(by=['Registered_Users'], ascending=False)
            top_states_a = top_states.sort_values(by=['AppOpenings'], ascending=False) 

            top_states_T=Data_Aggregated_Transaction_df.loc[(Data_Aggregated_Transaction_df['Year'] == int(Year)) & (Data_Aggregated_Transaction_df['Quarter'] ==int(Quarter))]
            topst=top_states_T.groupby('State')
            x=topst.sum().sort_values(by=['Transaction_count'], ascending=False)
            y=topst.sum().sort_values(by=['Transaction_amount'], ascending=False)


            
            
            rt=top_states_r[1:7]
            st.markdown("#### :orange[Registered Users]")
            st.markdown(rt[[ 'State','Registered_Users']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
            
            at=top_states_a[1:7]
            st.markdown("#### :orange[PhonePeApp Openings]")
            st.markdown(at[['State','AppOpenings']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
            
            st.markdown("#### :orange[Total Transactions]")
            st.write(x[['Transaction_count']].head(6))
            
            st.markdown("#### :orange[Total Amount]")
            st.write(y['Transaction_amount'].head(6))

            # Create a bar chart
            i1 = px.bar(rt, x='State', y='Registered_Users', color='State',
                        labels={'State': 'State', 'Registered_Users': 'Registered Users'},
                        title='Top 6 State by Registered Users (Decreasing Order)')

            st.plotly_chart(i1)

            # Create a bar chart
            i2 = px.bar(at, x='State', y='AppOpenings', color='State',
                        labels={'State': 'State', 'AppOpenings': 'App_opening'},
                        title='Top 6 State by App opened (Decreasing Order)')

            st.plotly_chart(i2)

            
            
            # Group by district and sort by 'Count' and 'Amount'
            xr = top_states_T.groupby('State').sum().sort_values(by='Transaction_count', ascending=False).reset_index().head(6)
            yr = top_states_T.groupby('State').sum().sort_values(by='Transaction_amount', ascending=False).reset_index().head(6)

            # Create bar charts
            fig_count = px.bar(xr, x='State', y='Transaction_count', color='State',
                            labels={'State': 'State', 'Transaction_count': 'Total Transactions'},
                            title='Top 6 State by Total Transactions (Decreasing Order)')

            fig_amount = px.bar(yr, x='State', y='Transaction_amount', color='State',
                                labels={'State': 'State', 'Transaction_amount': 'Total Amount'},
                                title='Top 6 State by Total Amount (Decreasing Order)')

            # Display the bar charts
            st.plotly_chart(fig_count)
            st.plotly_chart(fig_amount)

    with t2:
            st.write('# :red[TOP 6 DISTRICTS DATA]')
            c1,c2=st.columns(2)
            with c1:
                Year = int(st.radio(
                        'Please select the Year',
                        ('2018', '2019','2020','2021','2022'),key='y1h2k2'))
            with c2:
                Quarter = int(st.radio(
                        'Please select the Quarter',
                        ('1', '2', '3','4'),key='qgwe22'))
            Data_Map_User_df=Data_Map_User_Table.copy() 
            top_states=Data_Map_User_df.loc[(Data_Map_User_df['Year'] == int(Year)) & (Data_Map_User_df['Quarter'] ==int(Quarter))]
            top_states_r = top_states.sort_values(by=['Registered_user'], ascending=False)
            top_states_a = top_states.sort_values(by=['App_opens'], ascending=False) 

            top_states_T=Data_Map_Transaction_df.loc[(Data_Map_Transaction_df['Year'] == int(Year)) & (Data_Map_Transaction_df['Quarter'] ==int(Quarter))]
            topst=top_states_T.groupby('District')
            xr=topst.sum().sort_values(by=['Count'], ascending=False)
            yr=topst.sum().sort_values(by=['Amount'], ascending=False)

            

            
            rt=top_states_r.head(6)
            st.markdown("#### :orange[Registered Users]")
            st.markdown(rt[[ 'District','Registered_user']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
            
            at=top_states_a.head(6)
            st.markdown("#### :orange[PhonePeApp Openings]")
            st.markdown(at[['District','App_opens']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
            
            st.markdown("#### :orange[Total Transactions]")
            st.write(xr[['Count']].head(6))
            
            st.markdown("#### :orange[Total Amount]")
            st.write(yr['Amount'].head(6))

        
            
            # Create a bar chart
            i1 = px.bar(rt, x='District', y='Registered_user', color='District',
                        labels={'District': 'District', 'Registered_user': 'Registered Users'},
                        title='Top 6 District by Registered Users (Decreasing Order)')

            st.plotly_chart(i1)

            # Create a bar chart
            i2 = px.bar(at, x='District', y='App_opens', color='District',
                        labels={'District': 'District', 'App_opens': 'App_opening'},
                        title='Top 6 District by App opened (Decreasing Order)')

            st.plotly_chart(i2)

            
            
            # Group by district and sort by 'Count' and 'Amount'
            xr = top_states_T.groupby('District').sum().sort_values(by='Count', ascending=False).reset_index().head(6)
            yr = top_states_T.groupby('District').sum().sort_values(by='Amount', ascending=False).reset_index().head(6)

            # Create bar charts
            fig_count = px.bar(xr, x='District', y='Count', color='District',
                            labels={'District': 'District', 'Count': 'Total Transactions'},
                            title='Top 6 Districts by Total Transactions (Decreasing Order)')

            fig_amount = px.bar(yr, x='District', y='Amount', color='District',
                                labels={'District': 'District', 'Amount': 'Total Amount'},
                                title='Top 6 Districts by Total Amount (Decreasing Order)')

            # Display the bar charts
            st.plotly_chart(fig_count)
            st.plotly_chart(fig_amount)


        
            



        
    






     
if __name__ == '__main__':
    set_page_config()
    
    selected=selection()
    if selected == "map_analysis":
        ma()
    elif selected == "transaction_analysis":
        tr_a()
    elif selected == "users_analysis":
        urs_a()
    elif selected == "overall_analysis":
        oa()
    elif selected == "top_analysis":
        topa()
    