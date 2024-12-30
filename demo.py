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
st.title("Irish wheat data with predictions")
st.plotly_chart(fig)


# Load the dataset
data_file = "worldwide_wheat.csv" 
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

# new plot, line graph with toggles 

# List of features to choose from
features = ['Area harvested', 'Production', 'Yield']

# Dropdown for feature selection
selected_feature = st.selectbox("Select a feature to visualize:", features)

# Filter dataset to include only Ireland by default
default_countries = ['Ireland']
country_options = wheat_data['Area'].unique().tolist()

# Allow users to toggle countries
selected_countries = st.multiselect(
    "Select countries to display:",
    options=country_options,
    default=default_countries  # Ireland is selected by default
)

# Filter the dataset to include only the selected countries
filtered_data = wheat_data[wheat_data['Area'].isin(selected_countries)]

# Create the line chart
fig = px.line(
    filtered_data,
    x="Year",
    y=selected_feature,
    color="Area",  # Differentiate countries by color
    title=f"{selected_feature} over Time by Area",
    labels={"Year": "Year", selected_feature: selected_feature},
    template="plotly_white",
)

# Update layout for interactivity and legend customization
fig.update_layout(
    legend_title="Area",
    xaxis=dict(title="Year"),
    yaxis=dict(title=selected_feature),
    hovermode="x unified",  # Show values for all areas at the same year when hovering
)

# Display the chart in Streamlit
st.title(f"Interactive Plot for {selected_feature}")
st.plotly_chart(fig)

# Load the dataset
data_file = "area_farmed.csv"  
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
st.title("Area of Wheat Farmed by Region")
st.plotly_chart(fig)

# Load the dataset
data_file = "cost_base.csv"  
melted_cost = pd.read_csv(data_file)

# Create the line chart
fig = px.line(
    melted_cost,
    x="Year",
    y="Cost",
    color="Cost Type",
    title="Costs Fluctuations in Irish Wheat Farming (Base 2015)",
    labels={"Year": "Year", "Cost": "Cost (Base 2015)"},
    template="plotly_white",
)

# Update layout to adjust legend placement and interactivity
fig.update_layout(
    legend_title="Cost Type",
    legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.05),  # Move legend outside
    xaxis=dict(title="Year"),
    yaxis=dict(title="Cost"),
    hovermode="x unified",
)

# Display the chart in Streamlit
st.title("Cost Fluctuations in Irish Wheat Farming")
st.plotly_chart(fig)


# Load the dataset
data_file = "fra_uk_irl.csv"  
fra_uk_irl = pd.read_csv(data_file)

# List of features to choose from
features = [
    "(SE110) Yield of wheat (q/ha)",
    "(SE295) Fertilisers (€/farm)",
    "(SE345) Energy (€/farm)",
]

# Dropdown for feature selection
selected_feature = st.selectbox("Select a feature to visualize:", features)

# Create the line chart
fig = px.line(
    fra_uk_irl,
    x="Year",
    y=selected_feature,
    color="Member State",  # "Member State" will be used to differentiate countries
    title=f"{selected_feature} over Time",
    labels={"Year": "Year", selected_feature: selected_feature},
    template="plotly_white",
)

# Update layout for interactivity and legend customization
fig.update_layout(
    legend_title="Member State",
    xaxis=dict(title="Year"),
    yaxis=dict(title=selected_feature),
    hovermode="x unified",  # Show values for all countries at the same year when hovering
)

# Display the chart in Streamlit
st.title(f"Interactive Plot for {selected_feature}")
st.plotly_chart(fig)