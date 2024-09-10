import streamlit as st
import pandas as pd
import plotly.express as px
st.header('University Data')
data=pd.read_csv('/workspaces/University_data/mentornow/timesData.csv')
#st.write(data)  or dataframe

expander=st.expander('See data')
expander.write(data)

#OR
#with st.expander('see data'):
 #st.write(data)

  

with st.sidebar:

 options=st.multiselect("select the option",['research','citations','year'])
 st.write(options)
#options=st.sidebar.selectbox("select the option",['research','citations','year'])
#st.write(options)

fig=px.line(data.head(100),x='world_rank',y=options)
st.plotly_chart(fig) 

