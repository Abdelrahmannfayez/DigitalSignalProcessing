import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import math
import cmath
import re
import comparesignal2
import LabTwo
read_signal = LabTwo.read_signal


root = tk.Tk()
root.title("Signal Visualization Tool")
root.geometry("500x500")



# ------------------ DCT ----------------------


def calc_instance(indx, amplitude, N):
    z = 0
    for i in range(N):
        z += amplitude[i] * cmath.cos((math.pi / (4 * N)) * (2 * i -1) * (2 * indx -1))
    z *= math.sqrt(2 / N)
    return z



def calc_x_of_k(file):
    _, _, N, index, amplitude, _ = read_signal(file)
    list_X = []

    for k in index:
        f = calc_instance(k, amplitude, N)
        list_X.append(f)
    return list_X


def DCT_output_representation(list_x):
    #list_x is the complex term
    amplitudes = []
    phase_shift = []
    for i in list_x:
        real = i.real
        img = i.imag
        amplitudes.append(math.sqrt(real ** 2 ))
        phase_shift.append(cmath.phase(i))
    return amplitudes, phase_shift
def construct_Graphs():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, N, index, amplitude, _ = read_signal(file_path)
    sample_frequency = int(samplefrequency.get())
    ts= 1/sample_frequency
    omega= 2*math.pi /N*ts

    list_x = calc_x_of_k(file_path)
    A, P =  DCT_output_representation(list_x)

    freqX = []
    for i in range(N):
        freqX.append(i * omega)
    plt.figure(figsize=(8, 4))
    plt.stem(freqX, A)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('DCT of the Signal')
    plt.grid()
    plt.show()
    plt.figure(figsize=(8, 4))
    plt.stem(freqX, P)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase shift')
    plt.title('DCT of the Signal')
    plt.grid()
    plt.show()
    print("DCT-Test:")
    print(A)
    print(P)
    #testing DCT output
    comparesignal2.SignalSamplesAreEqual("Task_Files/TaskFive_Files/DCT/DCT_output.txt" , list_x )
    save(A,P,"trial.txt")


def save (A , P , filename):
    with open (filename,'w') as f:
        f.write("0\n0\n")
        f.write(str(len(A)))
        f.write("\n")
        for i in range (len(A)):
            f.write(f"{float(P[i])} {float(A[i])} ")
            f.write("\n")

#TASK #2 : Removing DC component from a signal.

def remove_dc_component():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, N, index, amplitude, _ = read_signal(file_path)
    average = sum(amplitude) / len(amplitude)
    z= [value - average for value in amplitude]
    save(z, index, "DC_removed")
    print("removed DC component test:")
    print (z)
    comparesignal2.SignalSamplesAreEqual("Task_Files/TaskFive_Files/Remove DC component/DC_component_output.txt",z )




# GUI
def add_separator():
    separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)
label_samplefrequency = tk.Label(root, text="sample frequency:")
label_samplefrequency.pack()

samplefrequency = tk.Entry(root)
samplefrequency.pack()

button_dft = tk.Button(root, text="DCT for a signal", command=construct_Graphs)
button_dft.pack()
add_separator()
button_dft = tk.Button(root, text="Remove Dc component from a choosen signal", command=remove_dc_component)
button_dft.pack()

root.mainloop()