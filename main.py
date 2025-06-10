import pandas as pd
from IPython.display import display
import load_results as load
import filter_results as filter_results

def main():

    print("Lab Results Module")
    print("This module is responsible for loading and processing lab results.")
    print("What file do you want to load?")
    file_path = input("Enter the path to the lab results CSV file: ")
    print("Loading lab results...")


    lab_results = load.load_lab_results(file_path)
    load.get_date(lab_results)

    #filter results
    print("These results can be filtered. What would you like fo filter by?")
    print("1. Patient ID")
    print("2. Date")
    print("3. Test Type")
    print("4. Flagged Results")
    filter_choice = input("Enter the number of your choice: ")
    if filter_choice == '1':
        filter_results.filter_id(lab_results)
    elif filter_choice == '2':
        filter_results.filter_date(lab_results)
    elif filter_choice == '3':
        filter_results.filter_test_type(lab_results)
    elif filter_choice == '4':
        filter_results.filter_result(lab_results)
    else:
        print("Invalid choice. No filtering applied.")
        filtered_results = lab_results

    
main()