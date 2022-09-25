from turtle import title
import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime


st.markdown('''
# Stock Price Monitor

**Author**
- App built by [Hambalieu Jallow]('https://github.com/Hambalieu')
- Build in Python using 'streamlit', 'yfinance', 'pandas', 'cufflinks', and 'datetime'.
''')

st.write('---')

#Slidebar to select the stock you want to see its prices
st.sidebar.subheader('Stock Listings')
start_date = st.sidebar.date_input('Start date', datetime.date(2022, 1, 1))
end_date = st.sidebar.date_input('End date', datetime.date(2022, 9,23))

#Retrieving ticket data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
#To select Ticker symbol
ticker_symbol = st.sidebar.selectbox('Stock Ticker', ticker_list)
#Get ticker data from yfinance
ticker_data = yf.Ticker(ticker_symbol)
#Get the price history of the ticker selected
ticker_history = ticker_data.history(period='1d',start=start_date, end=end_date )

#To get the ticker info to display on site
#Company logo image
string_logo = '<img src=%s>' % ticker_data.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)
#Company name
string_name = ticker_data.info['longName']
st.header('**%s**' % string_name)
#About the company
string_summary = ticker_data.info['longBusinessSummary']
st.info(string_summary)


#Bollinger Bands
st.header('**Chart**')
qf = cf.QuantFig(ticker_history,title='First Quant Figure', legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)



#Ticker data
st.header('**Ticker data**')
st.write(ticker_history)

