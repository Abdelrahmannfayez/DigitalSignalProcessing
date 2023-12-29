import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import matplotlib.pyplot as plt
import numpy as np

import comparesignals

root = tk.Tk()
root.title("LAB One")
root.geometry("500x500")


# Customized style for labels and buttons
custom_label_style = ("Arial", 12)
custom_button_style = ("Arial", 12)

# Task 1
list_one = []
list_two = []
list_three = []

def read_values(file):
    list_one.clear()
    list_two.clear()
    list_three.clear()
    with open(file, 'r') as f:
        line = f.readline()
        signal_type = int(line)  # 0 or 1
        line = f.readline()
        is_periodic = int(line)  # 0 or 1
        line = f.readline()
        n1 = int(line)  # no. of samples
        line = f.readline()

        while True:
            line = f.readline()
            line = line.strip()
            line = line.split(' ')
            # in case of time domain.
            if len(line) == 2:
                list_one.append(float(line[0]))
                list_two.append(float(line[1]))
            # in case of frequency domain.
            elif len(line) == 3:
                list_one.append(float(line[0]))
                list_two.append(float(line[1]))
                list_three.append(float(line[2]))
            else:
                break

    return signal_type, is_periodic, n1

def signal_output(signal_type, l1, l2):
    if signal_type == 0:
        # first diagram in case time domain:

        plt.plot(l1, l2)
        plt.title("Time-domain (continuous)")
        plt.xlabel("Index")
        plt.ylabel("Amplitude")
        plt.show()

        # second diagram in case time domain:

        plt.stem(l1, l2)
        plt.title("Time-domain (discrete)")
        plt.xlabel("Sample Index")
        plt.ylabel("Sample Amplitude")
        plt.show()

    else:
        # first diagram in case frequency domain:

        plt.plot(l1, l2)
        plt.title("Frequency-domain (continuous)")
        plt.xlabel("Frequency")
        plt.ylabel("Amplitude")
        plt.show()
        # second diagram in case frequency domain:

        plt.stem(l1, l2)
        plt.title("Frequency-domain (discrete)")
        plt.xlabel("Frequency")
        plt.ylabel("Sample Amplitude")
        plt.show()

# Task 2
def signal_generation(signal_sign, A, analog_frequency, sampling_frequency, theta):
    if sampling_frequency!=0:
        time = np.arange(0, 1, (1 / sampling_frequency))
    else:
        time = np.linspace(0, 1, (1/analog_frequency)) #continuous.
    if signal_sign == "sin":
        sin_signal = A * np.sin(2 * np.pi * analog_frequency * time + theta)
        return time, sin_signal
    elif signal_sign == "cos":
        cos_signal = A * np.cos(2 * np.pi * analog_frequency * time + theta)
        return time, cos_signal

def displaySignal(z):
    x = read_values(z)
    signal_output(x[0], list_one, list_two)

def create_sin_wave():
    try:
        A = float(entry_amplitude.get())
        sampling_frequency = float(entry_sampling_frequency.get())
        analog_frequency = float(entry_analog_frequency.get())
        theta = float(entry_phase_shift.get())

        t, s = signal_generation("sin", A, analog_frequency, sampling_frequency, theta)
        plt.stem(t, s)
        plt.plot(t, s)

        plt.title("Sin Wave")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.show()
        comparesignals.SignalSamplesAreEqual("Task_Files/TaskOne_Files/Sin_Cos/SinOutput.txt", t, s)




    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

def create_cos_wave():
    try:
        A = float(entry_amplitude.get())
        sampling_frequency = float(entry_sampling_frequency.get())
        analog_frequency = float(entry_analog_frequency.get())
        theta = float(entry_phase_shift.get())

        t, s = signal_generation("cos", A, analog_frequency, sampling_frequency, theta)
        plt.plot(t, s)
        plt.title("Cos Wave")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.show()
        comparesignals.SignalSamplesAreEqual("Task_Files/TaskOne_Files/Sin_Cos/CosOutput.txt", t, s)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

# Labels and Entries
label_amplitude = tk.Label(root, text="Amplitude:", font=custom_label_style)
label_amplitude.pack()
entry_amplitude = tk.Entry(root, font=custom_label_style)
entry_amplitude.pack()

label_analog_frequency = tk.Label(root, text="Analog Frequency:", font=custom_label_style)
label_analog_frequency.pack()
entry_analog_frequency = tk.Entry(root, font=custom_label_style)
entry_analog_frequency.pack()

label_sampling_frequency = tk.Label(root, text="Sampling Frequency:", font=custom_label_style)
label_sampling_frequency.pack()
entry_sampling_frequency = tk.Entry(root, font=custom_label_style)
entry_sampling_frequency.pack()

label_phase_shift = tk.Label(root, text="Phase Shift:", font=custom_label_style)
label_phase_shift.pack()
entry_phase_shift = tk.Entry(root, font=custom_label_style)
entry_phase_shift.pack()

# Buttons
button_create_sin_wave = tk.Button(root, text="Create Sine Wave", command=create_sin_wave, font=custom_button_style)
button_create_sin_wave.pack()

button_create_cos_wave = tk.Button(root, text="Create Cosine Wave", command=create_cos_wave, font=custom_button_style)
button_create_cos_wave.pack()

# Browse Files
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    displaySignal(filename)

#Frame and Separator for Line:
line_frame = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
line_frame.pack(fill=tk.X, padx=5, pady=5)

# Insert Signal Button
button_explore = tk.Button(root, text="Insert Signal to Be Displayed", command=browseFiles, font=custom_button_style)
button_explore.pack()

# Place a line below the Insert Signal Button
separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=5)


root.mainloop()
