#import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
# Load the dataset
data = pd.read_csv('irish_wheat_forecast.csv', index_col='Year')

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


# Load the dataset
data_file = "worldwide_wheat.csv"  # Ensure this file is in the same folder as this script
wheat_data = pd.read_csv(data_file)

# Ensure 'Year' is treated as a categorical variable for animation
wheat_data['Year'] = wheat_data['Year'].astype(str)

# Dropdown for feature selection
features = ["Area harvested", "Production", "Yield", "Cluster"]
selected_feature = st.selectbox("Select a feature to visualize:", features)

# Create the choropleth map
fig = px.choropleth(
    wheat_data,
    locations="Area",
    locationmode="country names",
    color=selected_feature,
    hover_name="Area",
    animation_frame="Year",
    color_continuous_scale=px.colors.sequential.Plasma,
)

# Update layout for better visuals
fig.update_layout(
    title_text=f"Worldwide Wheat Data: {selected_feature}",
    geo=dict(projection={"type": "natural earth"}),
)

# Display the choropleth in Streamlit
st.title("Worldwide Wheat Data Visualization")
st.plotly_chart(fig)

# Load the dataset
data_file = "area_farmed.csv"  # Ensure this file is in the same folder as this script
area_farmed = pd.read_csv(data_file)

# Ensure 'Year' is treated as a numeric variable
area_farmed['Year'] = pd.to_numeric(area_farmed['Year'], errors='coerce')

# Create the line chart
fig = px.line(
    area_farmed,
    x="Year",
    y="Total wheat",
    color="Region",
    title="Estimated Area of Wheat Farmed Over Time by Region",
    labels={"Year": "Year", "Total wheat": "Area of Wheat Farmed"},
    template="plotly_white",
)

# Update layout for interactivity
fig.update_layout(
    legend_title="Region",
    xaxis=dict(title="Year"),
    yaxis=dict(title="Area of Wheat Farmed"),
    hovermode="x unified",
)

# Display the chart in Streamlit
st.title("Interactive Area of Wheat Farmed by Region")
st.plotly_chart(fig)