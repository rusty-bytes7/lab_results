import pandas as pd
import load_results as load

def main():

    print("Lab Results Module")
    print("This module is responsible for loading and processing lab results.")
    print("What file do you want to load?")
    file_path = input("Enter the path to the lab results CSV file: ")
    print("Loading lab results...")


    load.load_lab_results(file_path)
    
main()