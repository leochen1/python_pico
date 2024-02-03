import streamlit as st
import pandas as pd
import datetime


st.title("My Pico GUI")
st.header("Leo House :red[溫度] 和 :blue[光線]")
st.divider()

print(datetime.datetime.now())
st.write(datetime.datetime.now())