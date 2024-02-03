import pytz
import streamlit as st
import pandas as pd
import datetime
import requests

taiwan_tz = pytz.timezone('Asia/Taipei')
now = datetime.datetime.now(taiwan_tz)
print(now)
st.write(now)

st.title("My Pico GUI")
st.header("Leo House :red[溫度] 和 :blue[光線]")
st.divider()

url = 'https://blynk.cloud/external/api/get?token=emVG_7OpSVh0rsC0GrOmsXTGAF3-T7TK&v0&v1'

response = requests.get(url)
if response.status_code == 200:
    all_data = response.json()
    st.info(f"光線:{all_data['v0']}")
    st.warning(f"可變電阻:{all_data['v1']}")
else:
    st.error("傳送失敗")
