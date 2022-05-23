import streamlit as st
import requests
import json
import time
import pandas as pd

# define urls
add_data_url = 'http://py-backend:8000/add_data/'
get_data_url = 'http://py-backend:8000/get_data'
get_trigger_url = 'http://py-backend:8000/db-alerts-stocks'
del_data_url = 'http://py-backend:8000/delete_data'

st.set_page_config(page_title="Alerts Stock",layout="wide",
     initial_sidebar_state="expanded",)

st.title("Alerts Stock")

st.sidebar.image("https://miro.medium.com/max/1000/1*B_R11J_9G4U3lac0omktLQ.png", width=100,
                 channels='BGR', output_format='PNG')

# define fetch function to get data
def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}
session = requests.Session()

# add options to select the operation
option = st.sidebar.selectbox(
         'Add or remove stocks',
        ('Add stock', 'Remove stock'))

# add stocks
if option == "Add stock":
    st.sidebar.subheader("Add new stock...")
    form =  st.sidebar.form("add", clear_on_submit =True)
    name_of_stock = form.text_input("Enter name of the stock")
    trend = form.radio("Select the Trend: ", ('Up Trend', 'Down Trend'))
    price_trigger = form.text_input("Enter the price trigger")
    submit = form.form_submit_button('Submit')
    if submit:
        if name_of_stock == None or trend == None or price_trigger == None:
            st.sidebar.error('Please input all the fields!')
        else:
            if trend == 'Up Trend':
                up_trend = True
            else: up_trend = False
            data = {
                "stock_name":name_of_stock,
                "up_trends":up_trend, 
                "price_trigger":float(price_trigger)
            }
            response = requests.post(add_data_url, data = json.dumps(data))
            if response:
                placeholder = st.empty()
                sta = st.sidebar.write(f"⏳ Data is submitting")
                time.sleep(3)
                st.sidebar.success("✔️ ' Stock added succesfully!")
                placeholder.empty()

# remove stocks
elif option == "Remove stock":
    st.sidebar.subheader("Add new stock...")
    form =  st.sidebar.form("del", clear_on_submit =True)
    del_name_of_stock = form.text_input("Enter name of the stock")
    submit = form.form_submit_button('Remove')
    if submit:
        del_data = {
                "stock_name":del_name_of_stock
            }
        response = requests.post(del_data_url, data = json.dumps(del_data))
        time.sleep(3)
        del_name_of_stock = ''
        st.sidebar.success("✔️ Stock removed succesfully!")

# get stock data
stock_data = fetch(session, get_data_url)
df = pd.json_normalize(stock_data) 
df['price_trigger'].round(2)
df.rename(columns = {'stock_name':'Name of the stoks', 'up_trends':'Trend', 'price_trigger': 'Price Trigger'}, inplace = True)
df["Trend"].replace({True: 'Up trend', False: 'Down trend'}, inplace=True)
df['Price Trigger'] = df['Price Trigger'].round(2)
st.table(df)
st.write('')
st.write('')
st.write('')
col1, col2 = st.columns([1,1])

with col1:
    st.write("See what's in trigger...")
with col2:
    refresh = st.button('Refresh')

# refresh function
if refresh:
    trigger = fetch(session, get_trigger_url)
    print (trigger)
    trigger_df = pd.json_normalize(trigger)
    for x, y in trigger.items():
        message = x + y 
        st.info(message)
