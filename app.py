import streamlit as st
import pandas as pd



df = pd.read_csv('vehicles_us.csv')

st.header('Market of used cars. Original data')
st.write("""
##### Filter the data below to see the ads by model
""")
show_new_cars = st.checkbox('Include new cars from dealers')
#creating options for filter  from all model and different years
model_choice = df['model'].unique()
make_choice_man = st.selectbox('Select model:', model_choice)

#next let's create a slider for years, so that users can filter cars by model years
#creating min and max years as limits for sliders
min_year, max_year=int(df['model_year'].min()), int(df['model_year'].max())

#creating slider 
year_range = st.slider( "Choose years",
     value=(min_year,max_year),min_value=min_year,max_value=max_year )
#creating actual range  based on slider that will be used to filter in the dataset

#creating actual range  based on slider that will be used to filter in the dataset
actual_range=list(range(year_range[0],year_range[1]+1))
#filtering dataset on chosen model and chosen year range
filtered_type=df[(df.model==make_choice_man) & (df.model_year.isin(list(actual_range)))]

#showing the final table in streamlit
st.table(filtered_type)

#first visualization
st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distibution of price varies depending on 
transmission, fuel or type, model and condition
""")



# Will create histograms with the split by parameter of choice: paint_color, transmission, type, conditon

#creating list of options to choose from
list_for_hist=['transmission','fuel','type','condition','model']

#creating selectbox
choice_for_hist = st.selectbox('Split for price distribution', list_for_hist)

#plotly histogram, where price is split by the choice made in the selectbox
fig1 = px.histogram(df, x="price", color=choice_for_hist)

#adding tittle
fig1.update_layout(
title="<b> Split of price by {}</b>".format(choice_for_hist))

#embedding into streamlit
st.plotly_chart(fig1)


st.header('model production and model production analysis')
st.write(""""
###### let's analyse what influence model production and model year. we will check how distribution of model
production varies depending on model,condition,cylinder,model_year,state
""")

import plotly.express as px

#creating list of options to choose from
list_for_scatter = ['model','cylinders','model_year','state']



choice_for_scatter = st.selectbox('split for model production', list_for_scatter)

#Plotly histogram
fig2 = px.scatter(df, x = 'odometer', color = choice_for_scatter)

fig2.update_layout(
title = '<b> Comparing the model and year the cars were produced by {}</b>'. format(choice_for_scatter))

st.plotly_chart(fig2)

st.header('Analysis type production and 4wd production')
st.write(""""
###### let's analyse what influence type production and 4wd production. we will check how distribution of how the two 
prodtction varies depending on manufacturer,type,fuel,is_4wd,condition
""")

import plotly.express as px

#creating list of options to choose from
list_for_bar = ['model','type','fuel','is_4wd','condition']

choice_for_bar = st.selectbox('split for type production', list_for_bar)

choice_for_bar = st.selectbox('split for is_4wd production', list_for_bar)


#Plotly histogram
fig3 = px.bar(df, x = 'condition', color = choice_for_bar)

fig3.update_layout(
title = '<b> Comparing type and 4wd cars production  by {}</b>'. format(choice_for_bar))

st.plotly_chart (fig3)
 