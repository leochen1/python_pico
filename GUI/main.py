import pytz
import streamlit as st
import pandas as pd
import datetime

taiwan_tz = pytz.timezone('Asia/Taipei')
now = datetime.datetime.now(taiwan_tz)
print(now)
st.write(now)

st.title("My Pico GUI")
st.header("Leo House :red[溫度] 和 :blue[光線]")
st.divider()



