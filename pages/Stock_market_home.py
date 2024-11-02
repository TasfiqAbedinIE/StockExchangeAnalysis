import pandas as pd
import streamlit as st
from streamlit import columns

import data_scrapping
from navigation import Side_Bar
from streamlit_autorefresh import st_autorefresh
from data_scrapping import extracting_stock_data


class streamlit_page_config:
    st.set_page_config(
        page_title="STOCK EXCHANGE",
        layout= "wide",
        initial_sidebar_state='auto',

    )
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

    hide_footer_style = '''<style>.reportview-container .main footer {visibility: hidden;} </style>'''
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    hide_menu_style = '''<style> #MainMenu {visibility: hidden;} </style>'''
    st.markdown(hide_menu_style, unsafe_allow_html=True)


streamlit_page_config()
side_bar = Side_Bar()
side_bar.make_sidebar()

st_autorefresh(interval=30000, key="dataframefresh")

url = 'https://www.dse.com.bd/latest_share_price_scroll_l.php'
stock_data, page_title, date_obj, time_obj = extracting_stock_data(url)
stock_dataframe = pd.DataFrame(stock_data)
print(stock_dataframe)

st.markdown(f"<p style='font-size:28px; font-weight: bold; text-align: center'>{page_title}</p>", unsafe_allow_html=True)
r1c1, r1c2, r1c3 = st.columns([2,4,2])
with r1c1:
    st.markdown(f"<p style='font-size:24px;'>DATE: {date_obj}</p>", unsafe_allow_html=True)
with r1c3:
    st.markdown(f"<p style='font-size:24px;'>LAST UPDATE: {time_obj}</p>",
                unsafe_allow_html=True)


# st.markdown(data_scrapping.price_data_list)


with st.container():

    stock_dataframe["PRICE_CHANGE"] = stock_dataframe['CLOSEP*'] - stock_dataframe['YCP*']
    stock_dataframe["Date"] = date_obj
    stock_dataframe["Time"] = time_obj
    # stock_dataframe = stock_dataframe['Date', 'Time', 'TRADING CODE', 'LTP*', 'HIGH', 'LOW', 'CLOSEP*', 'YCP*', 'PRICE_CHANGE', 'TRADE', 'VALUE (mn)', 'VOLUME']
    columns_order = ['Date', 'Time', 'TRADING CODE', 'LTP*', 'HIGH', 'LOW', 'CLOSEP*', 'YCP*', 'PRICE_CHANGE', 'TRADE', 'VALUE (mn)', 'VOLUME']
    st.dataframe(stock_dataframe, column_order=columns_order ,use_container_width=True, hide_index=True, height=500)
