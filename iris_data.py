import streamlit as st 
import pandas as pd
import plotly.express as px
st.header('Iris App')
df=px.data.iris()
#st.write(df)
with st.expander('See data'):
    st.write(df)

with st.sidebar:
 option1=st.selectbox('Select x axis',('sepal_length','petal_width'))

 option2=st.selectbox('Select y axis',('petal_length','sepal_width'))

 select=st.selectbox('Select histogram',('sepal_length','sepal_width','petal_length','petal_width'))

st.subheader('Scatter plot')
fig=px.scatter(df,x=option1,y=option2)
st.plotly_chart(fig)

st.subheader('Histogram')
fig1=px.histogram(df,select)
st.plotly_chart(fig1)
