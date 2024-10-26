#import calendar  # Core Python Module
#from datetime import datetime  # Core Python Module
#import datetime
from datetime import datetime, timedelta
import streamlit as st  # pip install streamlit
import psutil


# -------------- SETTINGS --------------
page_title = "مريم ناصر"
page_icon = ":balloon:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Define a function to get the current CPU and memory usage of the system
def get_system_usage():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    return cpu_percent, mem_percent

# # Function to calculate age in years, months, and days
# def calculate_age(birthdate):
#     today = datetime.today()
#     years = today.year - birthdate.year
#     months = today.month - birthdate.month
#     days = today.day - birthdate.day
    
#     # Adjust for negative values
#     if days < 0:
#         months -= 1
#         # Calculate the number of days in the previous month
#         previous_month = (today.replace(day=1) - timedelta(days=1)).day
#         days += previous_month

#     if months < 0:
#         years -= 1
#         months += 12
    
#     return years, months, days

# Function to calculate age in years, months, and days, and time until next birthday
def calculate_age_and_next_birthday(birthdate):
    today = datetime.today()
    
    # Calculate age in years, months, and days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day
    
    # Adjust for negative values in the days and months
    if days < 0:
        months -= 1
        previous_month = (today.replace(day=1) - timedelta(days=1)).day
        days += previous_month

    if months < 0:
        years -= 1
        months += 12

    # Calculate the next birthday
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    
    # Calculate the time difference until the next birthday
    months_until_birthday = next_birthday.month - today.month
    days_until_birthday = next_birthday.day - today.day
    
    if days_until_birthday < 0:
        months_until_birthday -= 1
        previous_month_days = (next_birthday.replace(day=1) - timedelta(days=1)).day
        days_until_birthday += previous_month_days

    if months_until_birthday < 0:
        months_until_birthday += 12

    return (years, months, days), (months_until_birthday, days_until_birthday)

# Define a function to check if the app can serve a new user based on the current resource usage
def can_serve_user():
    cpu_percent, mem_percent = get_system_usage()
    # Check if the current CPU and memory usage are below the threshold
    if cpu_percent < 90 and mem_percent < 90:
        return True
    else:
        return False

def main():
# Check if the app can serve a new user
    if can_serve_user():    
        # Birthdate: October 21, 2010
        birthdate = datetime(2010, 10, 21)

        # Calculate age
        #age_years, age_months, age_days = calculate_age(birthdate)
        
        (age_years, age_months, age_days), (months_until_birthday, days_until_birthday) = calculate_age_and_next_birthday(birthdate)
        
        if (age_months == 0) and (age_days == 0):
            st.header("كل سنة وإنتي طيبة يا مريم")
        else:
            st.text("Time Until Next Birthday:")
            col2, col3 = st.columns(2)
            col2.metric("Months:", f"{months_until_birthday}")
            col3.metric("Days:", f"{days_until_birthday}")

            
            
        st.text("Your Age Now Is:")
        col4, col6, col7 = st.columns(3)
        # Display the metrics
        col4.metric("Years:", f"{age_years}")
        col6.metric("Months:", f"{age_months}")
        col7.metric("Days:", f"{age_days}")

    
main()