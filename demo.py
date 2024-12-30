#import libraries
!pip install streamlit plotly pandas
import streamlit as st
import pandas as pd
import plotly.express as px
# Load the dataset
data = pd.read_csv('irish_wheat_forecast.csv', index_col='Year')

# Display the dataframe (optional)
st.write(data.head())

# Dropdown for feature selection
features = data.columns.tolist()
selected_feature = st.selectbox("Select a feature to plot:", features)

# Create a line graph
fig = px.line(data, x=data.index, y=selected_feature, 
              labels={'x': 'Year', 'y': selected_feature},
              title=f"{selected_feature} over Time")

# Enable hover interaction
fig.update_traces(mode='lines+markers', hovertemplate='%{x}: %{y:.2f}')

# Display the plot
st.plotly_chart(fig)