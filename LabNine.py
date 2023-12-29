import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import math
import cmath
import re
import comparesignal2
import numpy as np
import ConvTest
import CompareSignal
import LabTwo
read_signal = LabTwo.read_signal



root = tk.Tk()
root.title("Signal Visualization Tool")
root.geometry("500x500")


# ---------------------------------------- DFT --------------------------------------------------
def calc_harmonic(indx, amplitude, N):
    z = 0
    for i in range(N):
        z += amplitude[i] * cmath.exp(-1j * 2 * math.pi * indx * i / N)
    return z


def calc_x_of_k(amplitude):
    list_X = []

    for k in range(len(amplitude)):
        f = calc_harmonic(k, amplitude, len(amplitude))
        list_X.append(f)
    return list_X


def calc_amplitudes_phaseshifts(list_x):
    amplitudes = []
    phase_shift = []
    complex = []
    for i in list_x:
        real = i.real
        img = i.imag
        amplitudes.append(math.sqrt(real ** 2 + img ** 2))
        phase_shift.append(cmath.phase(i))
        complex.append(i)
    return amplitudes, phase_shift, complex


def dft(amplitude):
    list_x = calc_x_of_k(amplitude)
    A, P, C = calc_amplitudes_phaseshifts(list_x)
    return A, P, C


# ---------------------------------------- IDFT ----------------------------------------------------
def idft(complex_nums):
    N = len(complex_nums)
    signal = np.zeros(N, dtype=complex)

    for n in range(N):
        idft_sum = 0
        for k in range(N):
            complex_exp = np.exp(2j * np.pi * k * n / N)
            idft_sum += complex_nums[k] * complex_exp

        signal[n] = idft_sum / N

    signal = np.round(np.real(signal), 3)
    return signal


# ------------------------------------ Fast convoltion ------------------------------------------

def fast_convolution():
    # [1] Read files
    signal1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, index1, amplitude1, _ = read_signal(signal1)

    signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, index2, amplitude2, _ = read_signal(signal2)

    max_index = index1[-1] + index2[-1]
    min_index = index1[0] + index2[0]

    # [2] Assign new length
    New_length = len(amplitude1) + len(amplitude2) - 1
    while len(amplitude1) < New_length:
        amplitude1.append(0)
    while len(amplitude2) < New_length:
        amplitude2.append(0)

    # [3] Apply DFT for both signals
    A1, _, C1 = dft(amplitude1)
    A2, _, C2 = dft(amplitude2)

    # [4] Multiply complex numbers element-wise
    C3 = [C1[i] * C2[i] for i in range(len(C1))]

    # Apply IDFT on the product
    Final = idft(C3)

    indices = list(range(int(min_index), int(max_index + 1)))
    print( "Indicies: ", indices)
    print("Result: " , Final)
    ConvTest.ConvTest(indices , Final)
    return indices, Final

# ------------------------------------ Fast Correlation ------------------------------------------

def Cross_correlation():
    # [1] Read files
    signal1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, index1, amplitude1, _ = read_signal(signal1)

    signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, index2, amplitude2, _ = read_signal(signal2)

    # [2] Apply DFT for both signals
    A1, _, C1 = dft(amplitude1)
    A2, _, C2 = dft(amplitude2)

    # [3] Get conjugate of the First Complex list C1
    C1_conjugate = [np.conjugate(c) for c in C1]
    # [4] Multiply complex numbers element-wise
    C3 = [C1_conjugate[i] * C2[i] for i in range(len(C1))]

    # Apply IDFT on the product
    F = idft(C3)
    # normalize the output.

    Final = []
    for i in (F):
        Final.append(i / len(F))
    print(Final)
    CompareSignal.Compare_Signals("Task_Files/TaskNine_Files/Fast Correlation/Corr_Output.txt" , index1 , Final)
    return Final


def Auto_correlation():
    # auto correlation -> One signal , same steps....

    # [1] Read files
    signal1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, index1, amplitude1, _ = read_signal(signal1)

    _, _, _, index2, amplitude2, _ = read_signal(signal1)

    # [2] Apply DFT for both signals
    A1, _, C1 = dft(amplitude1)
    A2, _, C2 = dft(amplitude2)

    # [3] Get conjugate of the First Complex list C1
    C1_conjugate = [np.conjugate(c) for c in C1]
    # [4] Multiply complex numbers element-wise
    C3 = [C1_conjugate[i] * C2[i] for i in range(len(C1))]

    # Apply IDFT on the product
    F = idft(C3)
    # normalize the output.

    Final = []
    for i in (F):
        Final.append(i / len(F))
    print(Final)
    return Final
# ------------------------------------ GUI ------------------------------------------
# GUI
A = tk.Label(root, text=" LAB 9")
A.pack()



B = tk.Button(root, text="Fast Convolution", command=fast_convolution)
B.pack()

C = tk.Button(root, text="Cross Correlation", command=Cross_correlation)
C.pack()

D = tk.Button(root, text="Auto Correlation", command=Auto_correlation)
D.pack()

root.mainloop()