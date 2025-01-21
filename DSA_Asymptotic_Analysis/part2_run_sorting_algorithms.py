#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The initial versions of the code portions below were generated by GPT-4o 
or Gemini 2.0. These were then corrected, assembled, and tested by BT.
"""

import os
import random
import string
import time
import sys
import argparse
import pandas as pd
from module_merge_sort import merge_sort
from module_bubble_sort import bubble_sort
from module_heap_sort import heap_sort
from module_quick_sort import quick_sort
# from module_insertion_sort import insertion_sort
from module_selection_sort import selection_sort
from module_counting_sort import counting_sort

# In the previous step we generated many files that contain a variable number of patients :

# test_patients_diseases_100000000.txt
# test_patients_diseases_10000000.txt
# test_patients_diseases_1000000.txt
# test_patients_diseases_100000.txt
# test_patients_diseases_1500000.txt
# test_patients_diseases_200000000.txt
# test_patients_diseases_20000000.txt
# test_patients_diseases_2000000.txt
# test_patients_diseases_30000000.txt
# test_patients_diseases_3000000.txt
# test_patients_diseases_400000000.txt
# test_patients_diseases_40000000.txt
# test_patients_diseases_4000000.txt
# test_patients_diseases_50000000.txt
# test_patients_diseases_500000.txt
# test_patients_diseases_60000000.txt
# test_patients_diseases_6000000.txt
# test_patients_diseases_70000000.txt
# test_patients_diseases_7000000.txt
# test_patients_diseases_80000000.txt
# test_patients_diseases_8000000.txt
# test_patients_diseases_9000000.txt

# In this step of the analysis, we apply the sorting algorithms on almost each of the files describe above.
# In a pilot experiment, test the algorithms on 1000 patients :
# test_patients_diseases_10000.txt

# file_pathway = "/home/tanasa/Desktop/DSA_asymptotic_analysis/test_patients_diseases_10000.txt"
# file_name = os.path.basename(file_pathway)
# print(f"The file name is: {file_name}")

# Set the current working directory
os.chdir('/home/tanasa/Desktop/DSA_asymptotic_analysis/')

# Verify the current working directory
print("Current working directory:", os.getcwd())

# Check if the file path is provided as a command-line argument

if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
        sys.exit()

# Get the file pathway from the command-line argument

file_pathway = sys.argv[1]

# Check if the file exists

if not os.path.exists(file_pathway):
        print(f"Error: The file '{file_pathway}' does not exist.")
        sys.exit()

# Extract the file name

file_name = os.path.basename(file_pathway)
print(f"The file name is: {file_name}")

# Read and print the content of the file (first 10 lines)
try:
    with open(file_pathway, 'r') as file:
    
        print("\nFile contents:")
        for i, line in enumerate(file):
            if i >= 10:  # Print only the first 10 lines
                    break
            print(line.strip())
except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        

try:
    # Read the tab-separated file into a DataFrame
    data = pd.read_csv(file_pathway, sep="\t")
    
    # Display the first few rows of the data

    print("File successfully loaded. First few rows:")
    print(data.head(2))
    print("File successfully loaded. Last few rows:")
    print(data.tail(2)) 

    # Display summary statistics
    print("\nSummary of numeric columns:")
    print(data.describe())

    # Check for missing values
    print("\nMissing values in each column:")
    print(data.isnull().sum())
    
    file_name = os.path.basename(file_pathway)
    print(f"The file name is: {file_name}")

    print("\n The number of patients: ")
    print(f"Number of patients in the file: {data.shape[0]}")
    

except FileNotFoundError:
    print(f"File not found: {file_pathway}")
    sys.exit()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")  
    sys.exit()

# Sorting by TreatmentCost :

if 'treatmentCost' not in data.columns:
   raise ValueError("'TreatmentCost' column not found in the file")    
   sys.exit()


################################################################## 

# Create a file that records the running times
timing_file = f"{file_name}_execution_times.txt"

# Extract the 'TreatmentCost' column and apply sorting algorithms

treatment_costs = data['treatmentCost'].tolist()


################################################################## MERGE SORT


# Record the execution time in a file    

start_time_mergeSort = time.time()
sortedMerge_treatment_costs = merge_sort(treatment_costs)
end_time_mergeSort = time.time()
execution_time_mergeSort = end_time_mergeSort - start_time_mergeSort

with open(timing_file, 'a') as f:
        f.write(f"Execution Time for Merge Sort: {execution_time_mergeSort:.6f} seconds\n")

# Create a new DataFrame with sorted treatment costs

sortedMerge_data = data.loc[data['treatmentCost'].isin(sortedMerge_treatment_costs)].sort_values(by='treatmentCost')
print("File successfully sorted based on 'TreatmentCost'. First few rows:")
print(sortedMerge_data.head())
        
sortedMerge_data.to_csv("sortedMerge_patients_diseases.txt", sep="\t", index=False)


################################################################## BUBBLE SORT


# Record the execution time in a file   

start_time_bubbleSort = time.time()
sortedBubble_treatment_costs = bubble_sort(treatment_costs)
end_time_bubbleSort = time.time()
execution_time_bubbleSort = end_time_bubbleSort - start_time_bubbleSort

with open(timing_file, 'a') as f:
        f.write(f"Execution Time for Bubble Sort: {execution_time_bubbleSort:.6f} seconds\n")

# Create a new DataFrame with sorted treatment costs

sortedBubble_data = data.loc[data['treatmentCost'].isin(sortedBubble_treatment_costs)].sort_values(by='treatmentCost')
print("File successfully sorted based on 'TreatmentCost'. First few rows:")
print(sortedBubble_data.head())
        
sortedBubble_data.to_csv("sortedBubble_patients_diseases.txt", sep="\t", index=False)


################################################################## HEAP SORT


# Record the execution time in a file   

start_time_heapSort = time.time()
sortedHeap_treatment_costs = heap_sort(treatment_costs)
end_time_heapSort = time.time()
execution_time_heapSort = end_time_heapSort - start_time_heapSort

with open(timing_file, 'a') as f:
        f.write(f"Execution Time for Heap Sort: {execution_time_heapSort:.6f} seconds\n")

# Create a new DataFrame with sorted treatment costs

sortedHeap_data = data.loc[data['treatmentCost'].isin(sortedHeap_treatment_costs)].sort_values(by='treatmentCost')

# Display the first few rows of the sorted data
print("Sorted DataFrame based on 'treatmentCost':")
print(sortedHeap_data.head())

sortedHeap_data.to_csv("sortedHeap_patients_diseases.txt", sep="\t", index=False)


################################################################## QUICK SORT


# Record the execution time in a file   

start_time_quickSort = time.time()
sortedQuick_treatment_costs = quick_sort(treatment_costs)
end_time_quickSort = time.time()
execution_time_quickSort = end_time_quickSort - start_time_quickSort

with open(timing_file, 'a') as f:
        f.write(f"Execution Time for Quick Sort: {execution_time_quickSort:.6f} seconds\n")

# Create a new DataFrame with sorted treatment costs

sortedQuick_data = data.loc[data['treatmentCost'].isin(sortedQuick_treatment_costs)].sort_values(by='treatmentCost')

# Display the first few rows of the sorted data
print("Sorted DataFrame based on 'treatmentCost':")
print(sortedQuick_data.head())

sortedQuick_data.to_csv("sortedQuick_patients_diseases.txt", sep="\t", index=False)


################################################################## INSERTION SORT


# Record the execution time in a file   

# start_time_insertionSort = time.time()
# sortedInsertion_treatment_costs = insertion_sort(treatment_costs)
# end_time_insertionSort = time.time()
# execution_time_insertionSort = end_time_insertionSort - start_time_insertionSort

# with open(timing_file, 'a') as f:
#        f.write(f"Execution Time for Insertion Sort: {execution_time_insertionSort:.6f} seconds\n")

# Create a new DataFrame with sorted treatment costs

# sortedInsertion_data = data.loc[data['treatmentCost'].isin(sortedInsertion_treatment_costs)].sort_values(by='treatmentCost')

# Display the first few rows of the sorted data
# print("Sorted DataFrame based on 'treatmentCost':")
# print(sortedInsertion_data.head())

# sortedInsertion_data.to_csv("sortedInsertion_patients_diseases.txt", sep="\t", index=False)


################################################################## SELECTION SORT


# Record the execution time in a file   

start_time_selectionSort = time.time()
sortedSelection_treatment_costs = selection_sort(treatment_costs)
end_time_selectionSort = time.time()
execution_time_selectionSort = end_time_selectionSort - start_time_selectionSort

with open(timing_file, 'a') as f:
        f.write(f"Execution Time for Selection Sort: {execution_time_selectionSort:.6f} seconds\n")

# Create a new DataFrame with sorted treatment costs

sortedSelection_data = data.loc[data['treatmentCost'].isin(sortedSelection_treatment_costs)].sort_values(by='treatmentCost')

# Display the first few rows of the sorted data
print("Sorted DataFrame based on 'treatmentCost':")
print(sortedSelection_data.head())

sortedSelection_data.to_csv("sortedSelection_patients_diseases.txt", sep="\t", index=False)


################################################################## COUNTING SORT


# Record the execution time in a file   

start_time_countingSort = time.time()
sortedCounting_treatment_costs = counting_sort(treatment_costs)
end_time_countingSort = time.time()
execution_time_countingSort = end_time_countingSort - start_time_countingSort

with open(timing_file, 'a') as f:
        f.write(f"Execution Time for Counting Sort: {execution_time_countingSort:.6f} seconds\n")

# Create a new DataFrame with sorted treatment costs

sortedCounting_data = data.loc[data['treatmentCost'].isin(sortedCounting_treatment_costs)].sort_values(by='treatmentCost')

# Display the first few rows of the sorted data
print("Sorted DataFrame based on 'treatmentCost':")
print(sortedCounting_data.head())

sortedCounting_data.to_csv("sortedCounting_patients_diseases.txt", sep="\t", index=False)

##################################################################

# other sorting algorithms can be implemented as well. 

##################################################################      