import streamlit  as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import ExploretaryDataAnalysis
data = pd.read_csv("../data/togo-dapaong_qc.csv")
eda=ExploretaryDataAnalysis(data)

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Dashboard")
st.markdown("This is a dashboard for exploring the data")

st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(5))
    st.write("File uploaded successfully")
else:
    st.write("Please upload a file")

st.dataframe(data)
st.write("This is a dashboard for exploring the data")
describe=eda.check_missing_value(data)
st.write(describe)
st.bar_chart(data)