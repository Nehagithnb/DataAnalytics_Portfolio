# Task 1 : Data Cleaning and Preprocessing
# Overview
# This project completes Task 1. The main objective is to clean and prepare a raw dataset from Kaggle, handling missing values, duplicates, inconsistent formats, and exporting a ready-to-use, clean CSV file. The steps below describe my workflow tools and the learning experience.

# Step-by-Step Process
# Install Setup Tools
# Download and install Visual Studio Code (VS Code)
# Install the Python extension within VS Code (search “Python” in  the Extensions tab).
# Open Terminal and ensure Python 3 is installed: python3 –version
# If missing, install Python from python.org
# Install pandas: pip3 install pandas

# Get the Dataset from Kaggle
# Open Kaggle on chrome. 
# Sign up/log in
# Search for and download the Medical Appointment No Shows dataset.
# Move the CSV file to the Downloads folder for easy access.

#  Write and Run the Cleaning Script
# Open VS Code and create a new Python file: internship_task1.py
# Copy and paste the Python script with step-by-step comments.
# Edit file paths if needed so they match your stream.
# Run the script in the VS Code terminal or form your system terminal.

#  Cleaned Data
# Removing missing values and duplicates.
# Standardizing column names.
# Formatting date column for CSV/Excel.
# Ensuring ‘age’ is integer type.
# The output is exported as cleaned_dataset.csv on the Desktop.

# Uploading to Github
# Create a new repository on GitHub.
# Upload the below files:
# Python script: internship_task1.py
# Output file / Cleaned dataset: cleaned_dataset.csv
# Instructions file: readme.doc

# Python Script Explanation
# import the pandas library for data manipulation
import pandas as pd

# Load the CSV file
df = pd.read_csv('/Users/neha-/Downloads/KaggleV2-May-2016.csv')

# Explore the structure
df.info()
df.head()

# Handle missing values
df.isnull().sum()
df = df.dropna()  

# Remove duplicates
df = df.drop_duplicates()

# Standardize and clean string columns
df['Gender'] = df['Gender'].str.strip().str.lower()

# Convert date columns to pandas datetime 
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Format dates as strings for output 
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay']).dt.strftime('%d-%m-%Y')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay']).dt.strftime('%d-%m-%Y')

# Standardize column names
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

# Convert ‘age’ to  integer 
df['age'] = df['age'].astype(int)

# Save the  cleaned dataset
df.to_csv('/Users/neha-/Desktop/cleaned_dataset.csv', index=False)

# Learnings
# Data Cleaning: Learned how to identify and fix missing values, format textual and date columns, and structure a dataset for further analysis.
# Tools: Practiced using VS Code, pandas, and GitHub
# Real-World Pipeline: Understood the importance of preprocessing before analysis to ensure high data quality and reliable results.

