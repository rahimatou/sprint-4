import streamlit as st
import pandas as pd
import plotly_express as pe

df = pd.read_csv('vehicles_us.csv')

st.header('Market of used cars. Original data')
st.write("""
##### Filter the data below to see the ads by model
""")
show_new_cars = st.checkbox('Include new cars from dealers')

#first visualization
st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distibution of price varies depending on 
transmission, fuel or type and condition
""")



# Will create histograms with the split by parameter of choice: paint_color, transmission, type, conditon

#creating list of options to choose from
list_for_hist=['transmission','fuel','type','condition','model']

#creating selectbox
choice_for_hist = st.selectbox('Split for price distribution', list_for_hist)

#plotly histogram, where price is split by the choice made in the selectbox
fig1 = pe.histogram(df, x="price", color=choice_for_hist)

#adding tittle
fig1.update_layout(
title="<b> Split of price by {}</b>".format(choice_for_hist))

#embedding into streamlit
st.plotly_chart(fig1)


st.write("""
###### Now let's check how price is affected by odometer, cylinders in the adds
""")

#Distribution of price depending on odometer,cylinders
#with the split by age category
list_for_scatter=['odometer','cylinders']
choice_for_scatter = st.selectbox('Price dependency on ', list_for_scatter)
fig2 = pe.scatter(df, x="price", y=choice_for_scatter,hover_data=['model_year'])

fig2.update_layout(
title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)
 
