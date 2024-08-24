import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from utils import ExploratoryDataAnalysis

# Function to display plots in Streamlit
def display_plot(fig):
    buf = BytesIO()
    plt.savefig(buf, format='png')
    st.image(buf.getvalue())
    plt.close(fig)

# Streamlit app
st.title("Exploratory Data Analysis Dashboard")

# Sidebar for file upload
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    eda = ExploratoryDataAnalysis(data)
    
    # Sidebar for EDA options
    st.sidebar.header("EDA Options")
    show_missing_values = st.sidebar.checkbox("Show missing values")
    show_description = st.sidebar.checkbox("Show data description")
    show_box_plot = st.sidebar.checkbox("Show box plot")
    show_histogram = st.sidebar.checkbox("Show histogram")
    show_scatter_plot = st.sidebar.checkbox("Show scatter plot")
    show_correlation_matrix = st.sidebar.checkbox("Show correlation matrix")

    # Display missing values
    if show_missing_values:
        st.subheader("Missing Values")
        st.write(eda.check_missing_values())

    # Display data description
    if show_description:
        st.subheader("Data Description")
        st.write(eda.describe_data())

    # Display box plot
    if show_box_plot:
        column = st.sidebar.selectbox("Select column for box plot", data.columns)
        fig = plt.figure()
        eda.box_plot(column)
        display_plot(fig)
        plt.close(fig)

    # Display histogram
    if show_histogram:
        column = st.sidebar.selectbox("Select column for histogram", data.columns)
        fig = plt.figure()
        eda.histogram(column)
        display_plot(fig)
        plt.close(fig)

    # Display scatter plot
    if show_scatter_plot:
        x = st.sidebar.selectbox("Select X column for scatter plot", data.columns)
        y = st.sidebar.selectbox("Select Y column for scatter plot", data.columns)
        fig = plt.figure()
        eda.scatter_plot(x, y)
        display_plot(fig)
        plt.close(fig)

    # Display correlation matrix
    if show_correlation_matrix:
        st.subheader("Correlation Matrix")
        st.write(eda.correlation_matrix())
