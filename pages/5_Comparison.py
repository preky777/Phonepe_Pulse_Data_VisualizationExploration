import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
from streamlit_extras.add_vertical_space import add_vertical_space



# Data Prep

trans_df1 = trans_df2 = st.session_state['agg_trans_df']
user_df = st.session_state["agg_user_df"]

trans_df1["Transaction_amount(B)"] = trans_df1["Transaction_amount"] / 1e9
year_order = sorted(trans_df1["Year"].unique())
trans_df1["Year"] = pd.Categorical(trans_df1["Year"], categories=year_order, ordered=True)

quarter_options = ["All"] + list(st.session_state['quarters'])
transaction_types = trans_df1['Transaction_type'].unique()


# App


st.set_page_config(
                   page_title = 'Comparitive Analysis',
                   layout = 'wide',
                   page_icon = 'Phonepe_images/Logo.png'
                   )
st.title(':blue[Comparitive Analysis]')
add_vertical_space(3)


#1


st.subheader(':blue[Regionwise Transaction volume comparison]')


fig1 = sns.catplot(
                    x="Year", y="Transaction_amount",
                    col="Region", data=trans_df1,
                    kind="bar", errorbar=None,
                    height=5, aspect=1.5, col_wrap=2,
                    sharex=False
                    )

for ax in fig1.axes.flat:
    ax.set_yticklabels(['₹. {:,.0f}B'.format(y/1e9) for y in ax.get_yticks()])
    ax.set_ylabel('Transaction Amount')

sns.set_style("white")
st.pyplot(fig1)


#2


st.subheader(':blue[Transaction breakdown by Transaction type]')


col1, col2, col3 = st.columns([5, 3, 1])

selected_states = col1.multiselect("Select state(s)", st.session_state['states'], key='selected_states')
year1 = col2.selectbox("Year", st.session_state['years'], key='year1')
quarter1 = col3.selectbox("Quarter", quarter_options, key='quarter1')

trans_df1 = trans_df1[(trans_df1["Year"] == year1)]

if quarter1 != "All":
    trans_df1 = trans_df1[(trans_df1["Quarter"] == quarter1)]

suffix1 = " quarters" if quarter1 == 'All' else "st" if quarter1 == 1 else "nd" if quarter1 == 2 else "rd" if quarter1 == 3 else "th"

title1 = f"Transaction details comparison of the selected states for {str(quarter1).lower()}{suffix1} {'' if quarter1 == 'All' else 'quarter'} of {year1}"

if len(selected_states) == 1:
    state_str = ''.join(selected_states)
    title1 = f"Transaction details of {state_str} for {str(quarter1).lower()}{suffix1} {'' if quarter1 == 'All' else 'quarter'} of {year1}"

if selected_states:
    
    trans_df1 = trans_df1[trans_df1["State"].isin(selected_states)]
    trans_df1 = trans_df1.sort_values("Transaction_count", ascending=False)
    
    fig2 = px.bar(
                  trans_df1, x="Transaction_type", y="Transaction_count", 
                  color="State",
                  color_discrete_sequence=px.colors.qualitative.Plotly,
                  barmode='group',
                  title=title1,
                  labels=dict(Transaction_count='Transaction Count', Transaction_type='Transaction Type'),
                  hover_data={'Quarter': True}
                  )

    fig2.update_layout(
                       width=900, height=550,
                       title={
                              'x': 0.5,
                              'xanchor': 'center',
                              'y': 0.9,
                              'yanchor': 'top'
                              }
                       )

    fig2.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

    st.plotly_chart(fig2)
    
else:
    
    column, buffer = st.columns([5,4])
    column.info("Please select atleast one state to display the plot.")
    add_vertical_space(8)


#3


st.subheader(':blue[Transaction amount comparison - Quarterwise]')

col4, col5, buff = st.columns([3, 2, 4])

region2 = col4.selectbox('Region', trans_df2['Region'].unique(), key = 'region2')
year2 = col5.selectbox('Year', st.session_state['years'], key = 'year2')

filtered_df = trans_df2[(trans_df2['Region'] == region2) & (trans_df2['Year'] == year2)]

filtered_df['Quarter'] = 'Quarter ' + filtered_df['Quarter'].astype(str)

fig3 = px.pie(
              filtered_df, values='Transaction_amount(B)',
              names='Quarter', color='Quarter',
              title=f'Transaction amount Comparison of {region2} for the year {year2}'
              )

fig3.update_layout(
                    width=850, height=550,
                    title={
                           'x': 0.45,
                           'xanchor': 'center',
                           'y': 0.9,
                           'yanchor': 'top'
                           }
                    )

fig3.update_traces(textposition='inside', textinfo='percent+label') 

st.plotly_chart(fig3)

filtered_df['Year'] = filtered_df["Year"].astype(int)

expander1 = st.expander('Detailed view')
expander1.dataframe(
                    filtered_df.groupby(
                                        [
                                         'Year','Quarter'
                                         ]
                                        ).agg(
                                              {
                                                'Transaction_amount(B)': sum
                                                }
                                              ).reset_index().sort_values(
                                                                          'Transaction_amount(B)',
                                                                          ascending = False
                                                                          ).loc[:,['Quarter','Transaction_amount(B)']].reset_index(drop = True)
                                              )