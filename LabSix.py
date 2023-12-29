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

import LabTwo
read_signal = LabTwo.read_signal
def separator():
    separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)
root = tk.Tk()
root.title("Lab 6")
root.geometry("500x500")


# function One: Smoothing

def smoothing():
    file_name = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, n1, index, Amplitude, _ = read_signal(file_name)
    numpoints = int(num_points.get())
    Output_smoothing = []
    for i in range(len(Amplitude)):
        # Calculate the moving average for the current point
        if i + numpoints <= len(Amplitude):
            sum = 0
            for j in range(i, i + numpoints):
                sum += Amplitude[j]
            Output_smoothing.append(sum / numpoints)
    print(Amplitude)
    print(Output_smoothing)
    # Plotting the original and smoothed signals for visualization
    plt.figure(figsize=(10, 6))
    plt.plot(Amplitude, label='Original Signal')
    plt.plot(Output_smoothing, label=f'Smoothed Signal (Moving Average with {numpoints} points)')
    plt.legend()
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.title('Original Signal vs Smoothed Signal')
    plt.grid(True)
    plt.show()
    comparesignal2.SignalSamplesAreEqual("Task_Files/TaskSix_Files/Moving Average/OutMovAvgTest2.txt", Output_smoothing)


# function Two: Delay and advance by k steps

def ShiftSignal():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, l1, b, _ = read_signal(file_path)
    plt.plot(l1, b)
    plt.title("Original signal")
    plt.xlabel("Index")
    plt.ylabel("Amplitude")
    plt.show()
    print(l1)
    k = int(const_shift_signals.get())
    flag = delayorAdvance.get()
    if flag == 1:
        k = k * -1
    l3 = l1
    for i in range(len(l3)):
        l3[i] = l3[i] + k

    l2 = b  # Amplitude

    plt.plot(l3, l2)
    plt.title("shifted Signal")
    plt.xlabel("Index")
    plt.ylabel("Amplitude")
    plt.show()
    print(l3)


# folding signal
# function Three: Folding a Signal

# Function to fold (reverse) a signal along the x-axis

def fold_signal():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, l1, b, _ = read_signal(file_path)

    folded_amplitudes = list(reversed(b))  # Reverse the order of amplitudes

    plt.figure(figsize=(8, 6))
    plt.subplot(2, 1, 1)
    plt.plot(l1, b)
    plt.title("Original Signal")
    plt.xlabel("Index")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    plt.plot(l1, folded_amplitudes)
    plt.title("Folded Signal")
    plt.xlabel("Index")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()
    comparesignal2.SignalSamplesAreEqual("Task_Files/TaskSix_Files/Shifting and Folding/Output_fold.txt",
                                         folded_amplitudes)

#Shifting a folded signal.

def shift_folded():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, index, Amplitudes, _ = read_signal(file_path)

    folded_amplitudes = list(reversed(Amplitudes))  # Reverse the order of amplitudes

    k_steps = int(const_shift_signals_2.get())
    flag = KK.get()
    if flag == 0:
        k_steps = k_steps * -1
    # shifting folded amplitudes
    for i in range(len(folded_amplitudes)): #iterate on indicies
        index[i] = index[i] + k_steps

    print(folded_amplitudes)
    print(index)
    Shift_Fold_Signal.Shift_Fold_Signal("Task_Files/TaskSix_Files/Shifting and Folding/Output_ShifFoldedby500.txt", index,
                                folded_amplitudes)

##############################################


def dft(signal, sampling_frequency):
    N = len(signal)
    frequencies = np.zeros(N)
    amplitude = np.zeros(N)
    phase = np.zeros(N)
    for k in range(N):
        frequencies[k] = 2 * np.pi * k * sampling_frequency / N
        dft_sum = 0
        for n in range(N):
            complex_exp = np.exp(-2j * np.pi * k * n / N)
            dft_sum += signal[n] * complex_exp

        amplitude[k] = np.sqrt(dft_sum.real ** 2 + dft_sum.imag ** 2)
        phase[k] = np.arctan2(dft_sum.imag, dft_sum.real)


    # Save amplitude and phase to a text file
    with open('amplitude_and_phase.txt', 'w') as file:

        file.write("0\n")
        file.write("1\n")
        file.write(f"{N}\n")
        for k in range(N):
            file.write(f"{amplitude[k]:.4f} {phase[k]:.4f}\n")
        plt.figure(figsize=(8, 4))
    plt.stem(frequencies, phase, basefmt="", label='samples')
    plt.xlabel('freq')
    plt.ylabel('phase')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.stem(frequencies, amplitude, basefmt="", label='samples')
    plt.xlabel('freq')
    plt.ylabel('amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

    return frequencies, amplitude, phase


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
    plt.figure(figsize=(8, 4))
    plt.plot(signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('IDFT: Reconstructed Signal')
    plt.show()
    return signal


def remove_dc():
    file=filedialog.askopenfilename(title="enter file")
    X, y,x1,x2,x3,x4 = read_signal(file)

    freq, amp, phase = dft(x3, 4)

    complex_numbers = []
    for i in range(len(amp)):
        real_part = amp[i] * np.cos(float(phase[i]))
        imaginary_part = amp[i] * np.sin(float(phase[i]))
        complex_number = real_part + 1j * imaginary_part
        complex_numbers.append(complex_number)

    complex_numbers[0] = complex(0, 0)
    x = idft(complex_numbers)
    filename_output = filedialog.askopenfilename(title="Select a Signal File")
    comparesignal2.SignalSamplesAreEqual(filename_output, x)












################################################


# GUI components

label_smoothing = tk.Label(root, text="Smoothing")
label_smoothing.pack()

label_num_points = tk.Label(root, text="number of points included in Smoothing")
label_num_points.pack()

num_points = tk.Entry(root)
num_points.pack()

button_smoothing = tk.Button(root, text="Smoothing Signal", command=smoothing)
button_smoothing.pack()

# Draw line after "button_smoothing"
separator()
DelayOradvance = tk.Label(root, text="Delay Or Advance Signal by K")
DelayOradvance.pack()

const_shift_signals = tk.Entry(root)
const_shift_signals.pack()

delayorAdvance = tk.IntVar()
delayorAdvance.set(0)

DorA1 = tk.Radiobutton(root, text="Delay", variable=delayorAdvance, value=0)
DorA1.pack()

DorA2 = tk.Radiobutton(root, text="Advance", variable=delayorAdvance, value=1)
DorA2.pack()

add_button = tk.Button(root, text="Shift Signals", command=ShiftSignal)
add_button.pack()
separator()
Fold_button = tk.Button(root, text="Fold Signal", command=fold_signal)
Fold_button.pack()
# shift folded signal
separator()
DD = tk.Label(root, text="Delay Or Advance FOLDED Signal by K")
DD.pack()

const_shift_signals_2 = tk.Entry(root)
const_shift_signals_2.pack()

KK = tk.IntVar()
KK.set(0)

DorA1 = tk.Radiobutton(root, text="Delay", variable=KK, value=0)
DorA1.pack()

DorA2 = tk.Radiobutton(root, text="Advance", variable=KK, value=1)
DorA2.pack()
submit_shift_fold = tk.Button(root, text="Shift Folded Signal", command=shift_folded)
submit_shift_fold.pack()
separator()
#remove DC component.
RemoveDC = tk.Button(root, text="Remove DC component", command=remove_dc)
RemoveDC.pack()
separator()

DER = tk.Button(root, text="Derivative Signal Test", command=DerivativeSignal.DerivativeSignal)
DER.pack()
root.mainloop()

############################################################################################################
