import streamlit as st
from sklearn.datasets import load_iris
import pandas as pd
st.write('hello world')
st.balloons()
data = load_iris(as_frame=True).frame
st.write(data.head())