# import the pandas library for data manipulation
import pandas as pd

# Step 1: Read the CSV data downloaded from Kaggle
df = pd.read_csv('/Users/neha-/Downloads/KaggleV2-May-2016.csv')

# Step 2: Get a concise summary of the DataFrame: columns, datatypes, nulls 
df.info()

# Step 3: Display the first 5 rows to see sample data and column formatting
df.head()

# Step 4: Check for missing values in each column
df.isnull().sum()

# Step 5: Remove rows with any missing values (you could also fill instead)
df = df.dropna()  # Or fill with some value: df.fillna(value)

# Step 6: Remove duplicate rows, keeping only the first occurrence
df = df.drop_duplicates()

# Step 7: Standardize/clean the 'Gender' column values:
# - Removes spaces and converts everything to lowercase (example: Male -> male)
df['Gender'] = df['Gender'].str.strip().str.lower()

# Step 8: Convert 'ScheduleDay' and 'AppointmentDay' column to pandas datetime objects
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Step 9: Convert datatime objects to string format 'dd-mm-yyyy'
# - This makes it more readable in tools like Excel
# This is an optional step
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay']).dt.strftime('%d-%m-%Y')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay']).dt.strftime('%d-%m-%Y')

# Step 10: Standardize column names
# - Lowercase all letters and replace spaces with underscores for consistency
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

# Step 11: Make sure the 'age' column is stored as integer type
df['age'] = df['age'].astype(int)

# Step 12: Export the cleaned DataFrame to a new CSV file on the Desktop
df.to_csv('/Users/neha-/Desktop/cleaned_dataset.csv', index=False)