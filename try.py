import pandas as pd
import streamlit as st
import datetime

data = pd.read_csv(r'E:\assingement\stock Sentiment Analysis\Data\finance.csv')
df_ibm = pd.read_csv(r'Data\IBM_Sentiment.csv')
df_aapl = pd.read_csv(r'Data\AAPL_Sentiment.csv')
df_tsla = pd.read_csv(r'Data\TSLA_Sentiment.csv')
df_baba = pd.read_csv(r'Data\BABA_Sentiment.csv')
df_oracle = pd.read_csv(r'Data\oracle_Sentiment.csv')
df_amazon = pd.read_csv(r'Data\amazon_Sentiment.csv')
df_ma = pd.read_csv(r'Data\ma_Sentiment.csv')
df_microsoft = pd.read_csv(r'Data\microsoft_Sentiment.csv')
df_nike = pd.read_csv(r'Data\nike_Sentiment.csv')
df_nvda = pd.read_csv(r'Data\nvda_Sentiment.csv')

df_ibm['Date'] =  pd.to_datetime(df_ibm['Date'])
df_aapl['Date'] =  pd.to_datetime(df_aapl['Date'])
df_tsla['Date'] =  pd.to_datetime(df_tsla['Date'])
df_baba['Date'] =  pd.to_datetime(df_baba['Date'])
df_oracle['Date'] =  pd.to_datetime(df_oracle['Date'])
df_ma['Date'] =  pd.to_datetime(df_ma['Date'])
df_microsoft['Date'] =  pd.to_datetime(df_microsoft['Date'])
df_nike['Date'] =  pd.to_datetime(df_nike['Date'])
df_nvda['Date'] =  pd.to_datetime(df_nvda['Date'])
df_amazon['Date'] =  pd.to_datetime(df_amazon['Date'])

st.subheader('Twitter Tweets Sentiment Analysis on Stocks Data')
data = data.set_index('Date')
col = st.columns(2)
with col[0]:
    sel_symbol = st.selectbox('Select a Symbol for Trend Line', ('TSLA','AAPL','IBM','BABA','ORCL','NKE','AMZN','MSFT','NVDA','MA'))
with col[1]:
    sel_date = st.date_input('Select a Date for Sentiment Count',datetime.date(2022, 6, 21))
data = data[[sel_symbol]]
st.line_chart(data, use_container_width=True)

if sel_symbol == 'IBM':
    graph_data = (df_ibm['Date'] == str(sel_date))
    graph_data = df_ibm.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'AAPL':
    graph_data = (df_aapl['Date'] == str(sel_date))
    graph_data = df_aapl.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'TSLA':
    graph_data = (df_tsla['Date'] == str(sel_date))
    graph_data = df_tsla.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'BABA':
    graph_data = (df_baba['Date'] == str(sel_date))
    graph_data = df_baba.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'ORCL':
    graph_data = (df_oracle['Date'] == str(sel_date))
    graph_data = df_oracle.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'NKE':
    graph_data = (df_nike['Date'] == str(sel_date))
    graph_data = df_nike.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'AMZN':
    graph_data = (df_amazon['Date'] == str(sel_date))
    graph_data = df_amazon.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'MSFT':
    graph_data = (df_microsoft['Date'] == str(sel_date))
    graph_data = df_microsoft.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'NVDA':
    graph_data = (df_nvda['Date'] == str(sel_date))
    graph_data = df_nvda.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)
elif sel_symbol == 'MA':
    graph_data = (df_ma['Date'] == str(sel_date))
    graph_data = df_ma.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    st.bar_chart(bar_value)