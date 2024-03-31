import streamlit as st
import pandas as pd
import time 
from datetime import datetime
import os

st.title('Attendance Report')

count = st.number_input("Enter a number:", value=0, step=1)

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

# Check if the attendance file for today exists, if not, create it
attendance_file = "Attendance/Attendance_" + date + ".csv"
if not os.path.exists(attendance_file):
    with open(attendance_file, "w") as file:
        file.write("NAME,TIME\n")
    st.write("Attendance file created for today.")

try:
    df = pd.read_csv(attendance_file)
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    st.write("No attendance data available for today.")
