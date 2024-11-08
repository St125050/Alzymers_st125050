"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st


# Configure the app
st.set_page_config(
    page_title = 'Brain-MRI-Alzheimer',
    page_icon = 'brain',
    initial_sidebar_state = 'auto'
)

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, BT



# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "MRI / CT-Scan":BT
   
    
}




# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")



# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))


# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
