import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import math
import cmath
import re
import comparesignal2
import Shift_Fold_Signal
import DerivativeSignal
import numpy as np
import ConvTest
import LabTwo


read_signal = LabTwo.read_signal


root = tk.Tk()
root.title("Signal Visualization Tool")
root.geometry("500x500")


############### #########################################################

def convolution():
    file_name1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, index1, amplitude1, _ = read_signal(file_name1)

    file_name2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, index2, amplitude2, _ = read_signal(file_name2)

    max_index = index1[-1] + index2[-1]
    min_index = index1[0] + index2[0]
    signal1 = dict(zip(index1, amplitude1))
    signal2 = dict(zip(index2, amplitude2))
    indices = list(range(int(min_index), int(max_index + 1)))
    result = {i: 0 for i in indices}  # Initialize result with zeros

    for n in indices:
        for k in index2:
            if n - k in signal1:
               result[n] += signal1[n - k] * signal2[k]


    plt.plot(indices, list(result.values()))
    plt.title(" Convolution of 2 signals")
    plt.xlabel("Indices")
    plt.ylabel("Resulted of Amplitudes")
    plt.show()
    print(result)
    ConvTest.ConvTest(indices , list(result.values()))

    return indices, list(result.values())



# GUI


# GUI components
label = tk.Label(root, text="CONVOLUTION between 2 signals")
label.pack()

button_conv = tk.Button(root, text="conv of 2 Signal", command=convolution)
button_conv.pack()
root.mainloop()




