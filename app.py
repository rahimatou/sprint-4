import streamlit as st
import pandas as pd
import plotly_express as pe

df = pd.read_csv('vehicles_us.csv')

#first visualization
st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distibution of price varies depending on 
transmission, fuel or type and condition
""")

import plotly.express as px

# Will create histograms with the split by parameter of choice: paint_color, transmission, type, conditon

#creating list of options to choose from
list_for_hist=['transmission','fuel','type','condition']

#creating selectbox
choice_for_hist = st.selectbox('Split for price distribution', list_for_hist)

#plotly histogram, where price is split by the choice made in the selectbox
fig1 = px.histogram(df, x="price", color=choice_for_hist)

#adding tittle
fig1.update_layout(
title="<b> Split of price by {}</b>".format(choice_for_hist))

#embedding into streamlit
st.plotly_chart(fig1)