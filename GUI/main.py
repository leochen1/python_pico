import streamlit as st
import pandas as pd
import time


st.title("My Pico GUI")
st.header("Leo House :red[溫度] 和 :blue[光線]")
localtime = time.localtime()
st.divider()
st.write("現在時間: ", time.strftime("%Y-%m-%d %H:%M:%S", localtime))