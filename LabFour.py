import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import math
import cmath
import re
import LabTwo

read_signal = LabTwo.read_signal



root = tk.Tk()
root.title("Signal Visualization Tool")
root.geometry("500x500")


# ------------------ dft ----------------------
def calc_harmonic(indx, amplitude, N):
    z = 0
    for i in range(N):
        z += amplitude[i] * cmath.exp(-1j * 2 * math.pi * indx * i / N)
    return z


def calc_x_of_k(file):
    _, _, N, index, amplitude, _ = read_signal(file)
    list_X = []

    for k in index:
        f = calc_harmonic(k, amplitude, N)
        list_X.append(f)
    return list_X


def calc_amplitudes_phaseshifts(list_x):
    amplitudes = []
    phase_shift = []
    for i in list_x:
        real = i.real
        img = i.imag
        amplitudes.append(math.sqrt(real ** 2 + img ** 2))
        phase_shift.append(cmath.phase(i))
    return amplitudes, phase_shift


def construct_amplitudeXfreq():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, N, index, amplitude, _ = read_signal(file_path)
    sample_frequency = int(samplefrequency.get())
    ts= 1/sample_frequency
    omega= 2*math.pi /N*ts

    list_x = calc_x_of_k(file_path)
    A, P = calc_amplitudes_phaseshifts(list_x)

    freqX = []
    for i in range(N):
        freqX.append(i * omega)
    plt.figure(figsize=(8, 4))
    plt.stem(freqX, A)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('DFT of the Signal')
    plt.grid()
    plt.show()
    plt.figure(figsize=(8, 4))
    plt.stem(freqX, P)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase shift')
    plt.title('DFT of the Signal')
    plt.grid()
    plt.show()
    print(A)
    print(P)
    save(A,P,"trial.txt")

def save (A , P , filename):
    with open (filename,'w') as f:
        f.write("0\n0\n")
        f.write(str(len(A)))
        f.write("\n")
        for i in range (len(A)):
            f.write(f"{float(A[i])} {float(P[i])}")
            f.write("\n")
def modify( ):
    index=int(indx.get())
    amplitude=int(amp.get())
    phaseshift=int(p.get())
    signal_type, is_periodic, n1, A, P, _=read_signal("trial.txt")
    A[index]=amplitude
    P[index]=phaseshift
    save(A,P,"trial.txt")


# ----------------------- idft ------------------------------------
def prepare_idft(file):
    _, _, N, amplitude, phaseshift, _ = read_signal(file)
    real = []
    img = []
    for i, j in zip(amplitude, phaseshift):
        real.append(i * math.cos(j))
        img.append(i * math.sin(j))
    return real, img


def calc_harmonic_idft(n, real, img, N):
    z = 0
    for i in range(N):
        z += (real[i] + img[i] * 1j) * cmath.exp(1j * 2 * math.pi * i * n / N) #(real[i] + img[i] * 1j) -> x[k]
    return z


def calc_x_of_n(file):
    _, _, N, _, _, _ = read_signal(file)
    real, img = prepare_idft(file)
    list_X = []

    for n in range(N):
        f = calc_harmonic_idft(n, real, img, N)
        list_X.append(f)
    for i in range(N):
        list_X[i] = int(list_X[i].real / N)
        if list_X[i] % 2 == 0:
            list_X[i] += 1
    return list_X


def idft():
    file= filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    y = calc_x_of_n(file)
    _, _, N, _, _, _ = read_signal(file)
    x = [i for i in range(N)]
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.stem(x, y)
    plt.xlabel('time sample')
    plt.ylabel('Amplitude')
    plt.title('IDFT of the Signal')
    plt.grid()
    plt.show()
    print(y)



# GUI
def add_separator():
    separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)
label_samplefrequency = tk.Label(root, text="sample frequency:")
label_samplefrequency.pack()

samplefrequency = tk.Entry(root)
samplefrequency.pack()

button_dft = tk.Button(root, text="DFT for a signal", command=construct_amplitudeXfreq)
button_dft.pack()
add_separator()
button_idft = tk.Button(root, text="IDFT for a signal", command=idft)
button_idft.pack()

add_separator()

index = tk.Label(root, text="index")
index.pack()

indx = tk.Entry(root)
indx.pack()

amplitude = tk.Label(root, text="amplitude")
amplitude.pack()

amp = tk.Entry(root)
amp.pack()

phase  = tk.Label(root, text="phase shift")
phase.pack()

p = tk.Entry(root)
p.pack()

button_submit = tk.Button(root, text="Choose Signal to Modify these upper fields in ", command=modify)
button_submit.pack()
root.mainloop()
