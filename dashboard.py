import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

import plotly.graph_objs as go  # Add this import statement
import plotly.offline as py  # Add this import statement


st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')



st.title("Kaggle Dataset Loader")

# Allow the user to upload a dataset
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the dataset using pandas
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)  # Display the dataset
    
    
