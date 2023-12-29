import CompareSignal_Correlation
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import math
import cmath
import re
import comparesignal2
import numpy as np
import LabTwo
read_signal = LabTwo.read_signal

root = tk.Tk()
root.title("Signal Visualization Tool")
root.geometry("500x500")

#re-order the list
def move_first_to_end(lst):
    if lst:  # Ensure the list is not empty
        first_element = lst.pop(0)
        lst.append(first_element)
    return lst

# Function to compute the normalized cross-correlation directly
def normalized_cross_correlation_direct(signal1, signal2):
    # Compute the normalization factor


    N = len(signal1)
    norm_factor =  math.sqrt(sum(x ** 2 for x in signal1) * sum(y ** 2 for y in signal2)) / N

    corr = []

    for j in range(N):
        result = sum(x * y for x, y in zip(signal1, signal2))
        corr.append(result/N)
        signal2=move_first_to_end(signal2)
    normalized_corr= []
    

    for x in corr:
        normalized_corr.append(x/norm_factor)    #x / norm factor
    return normalized_corr

def compute_correlation():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, N, index, signal1, _ = read_signal(file_path)
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, N, index, signal2, _ = read_signal(file_path)
    corr_with_normalization = normalized_cross_correlation_direct(signal1, signal2)

    print(" normalized Cross-Correlation Result:", corr_with_normalization)

    CompareSignal_Correlation.Compare_Signals("Task_Files/TaskEight_Files/Point1_Correlation/CorrOutput.txt", index,corr_with_normalization)



phase_8  = tk.Label(root, text="Correlation: compute normalized cross-correlation of two signals.")
phase_8.pack()



button_submit = tk.Button(root, text="cross-correlation of two signals.", command=compute_correlation)
button_submit.pack()

root.mainloop()