import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load data
@st.cache
def load_data():
    return pd.read_csv("data.csv")


data = load_data()

# Main title
st.title("Bike Sharing Analysis Dashboard")

# Sidebar
st.sidebar.title("Options")
selected_option = st.sidebar.selectbox(
    "Select Option", ["Overview", "Season Analysis", "Weather Analysis"]
)

# Overview page
if selected_option == "Overview":
    st.header("Overview Page")
    st.write("This is the overview page.")

# Season analysis page
elif selected_option == "Season Analysis":
    st.header("Season Analysis Page")
    st.write("This is the season analysis page.")
    # Bar plot of bike rental count by season
    plt.figure(figsize=(8, 6))
    sns.barplot(x="season", y="cnt", data=data, estimator="mean")
    plt.title("Average Bike Rental Count by Season")
    plt.xlabel("Season")
    plt.ylabel("Average Bike Rental Count")
    plt.xticks([0, 1, 2, 3], ["Spring", "Summer", "Fall", "Winter"])
    st.pyplot()

# Weather analysis page
elif selected_option == "Weather Analysis":
    st.header("Weather Analysis Page")
    st.write("This is the weather analysis page.")
    # Bar plot of bike rental count by weather condition
    plt.figure(figsize=(8, 6))
    sns.barplot(x="weathersit", y="cnt", data=data, estimator="mean")
    plt.title("Average Bike Rental Count by Weather Condition")
    plt.xlabel("Weather Condition")
    plt.ylabel("Average Bike Rental Count")
    plt.xticks([0, 1, 2, 3], ["Clear", "Mist", "Light Snow/Rain", "Heavy Rain/Snow"])
    st.pyplot()
