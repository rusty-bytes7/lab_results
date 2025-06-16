#this code allows the user to filter the data in the database
import pandas as pd
def filter_id(df):
    #filter by patient ID- rows
    patient_id = int(input("Enter the Patient ID to filter by: "))
    #check if patient ID exists
    if patient_id not in df['PatientID'].values:
        print(f"Patient ID {patient_id} does not exist in the data.")
        return df  # Return original dataframe if patient ID does not exist
    filtered_df = df[df['PatientID'] == patient_id]
    return filtered_df

def filter_date(df):
    #filter by date
    date = input("Enter the date to filter by (YYYY-MM-DD): ")
    #check if date exists
    try:
        pd.to_datetime(date)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return df  # Return original dataframe if date is invalid
    filtered_df = df[df['Date'] == date]
    return filtered_df

def filter_test_type(df):
    #filter by test type
    test_type = input("Enter the test type to filter by: ")
    #check if test type exists
    if test_type not in df['Test'].values:
        print(f"Test type '{test_type}' does not exist in the data.")
        return df  # Return original dataframe if test type does not exist
    filtered_df = df[df['Test'] == test_type]
    return filtered_df

