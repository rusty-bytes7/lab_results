import pandas as pd

def load_lab_results(file_path):
    try:
        lab_results = pd.read_csv(file_path)
        print("Lab results loaded successfully.")
        return lab_results
    except Exception as e:
        print(f"Error loading lab results: {e}")
        return None

def get_date(lab_results):
    #sort the dataframe by date
    lab_results['Date'] = pd.to_datetime(lab_results['Date'])
    lab_results = lab_results.sort_values(by='Date')
    print(lab_results)