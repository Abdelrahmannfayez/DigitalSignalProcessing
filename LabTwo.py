import tkinter as tk
from tkinter import filedialog, messagebox

import matplotlib.pyplot as plt
import re
import comparesignals
import os

def read_signal(file):
    list_one = []
    list_two = []
    list_three = []
    with open(file, 'r') as f:
        line = f.readline()
        signal_type = int(line)  # 0 or 1
        line = f.readline()
        is_periodic = int(line)  # 0 or 1
        line = f.readline()
        n1 = int(line)  # no. of samples

        while True:
            line = f.readline()
            line = line.strip()
            line = re.split(r'[ ,]', line)
            if len(line) == 2:
                list_one.append(float(line[0]))
                list_two.append(float(line[1]))
            elif len(line) == 3:
                list_one.append(float(line[0]))
                list_two.append(float(line[1]))
                list_three.append(float(line[2]))
            else:
                break

    return signal_type, is_periodic, n1, list_one, list_two, list_three



# _______________________________________ [1] Adding any number of signals____________________________________________
def addSignals():
    scount = int(entry_num_signals.get())
    list_b = []
    list_a = []

    for i in range(scount):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        _, _, _, l1, b, _ = read_signal(file_path)
        if i == 0:
            list_b = b
        else:
            list_b = [sum(s) for s in zip(list_b, b)]  # Amplitude sum.

    l2 = list_b  # Sample Amplitude

    plt.plot(l1, l2)
    plt.title("Sum of Signals")
    plt.xlabel("Sample Index")
    plt.ylabel("Sample Amplitude")

    # Save the result to a text file on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_file_path = os.path.join(desktop_path, 'result_signal.txt')

    try:
        # Create the directory if it doesn't exist
        os.makedirs(desktop_path, exist_ok=True)

        with open(output_file_path, 'w') as output_file:
            for sample_index, sample_amplitude in zip(l1, l2):
                output_file.write(f"{sample_index} {sample_amplitude}\n")
        messagebox.showinfo("Success", "Result saved to the desktop as 'result_signal.txt'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing the file: {str(e)}")

    plt.show()

    # Rest of your code remains the same

    comparesignals.SignalSamplesAreEqual("Task_Files/TaskTwo_ Files/signal1+signal3.txt", l1, l2)


# ______________________________________________ [2] Subtracting 2 signals_____________________________________________

def subSignal():
    list_b = []
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, l1, b, _ = read_signal(file_path)

    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, l2, b2, _ = read_signal(file_path)

    list_b = [abs(k - l) for k, l in zip(b2, b)]

    l2 = list_b
    plt.plot(l1, l2)
    plt.title("Difference of Signals")
    plt.xlabel("Sample Index")
    plt.ylabel("Sample Amplitude")

    # Save the result to a text file on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_file_path = os.path.join(desktop_path, 'result_signal.txt')

    try:
        # Create the directory if it doesn't exist
        os.makedirs(desktop_path, exist_ok=True)

        with open(output_file_path, 'w') as output_file:
            for sample_index, sample_amplitude in zip(l1, l2):
                output_file.write(f"{sample_index} {sample_amplitude}\n")
        messagebox.showinfo("Success", "Result saved to the desktop as 'result_signal.txt'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing the file: {str(e)}")

    plt.show()

    # Rest of your code remains the same

    comparesignals.SignalSamplesAreEqual("Task_Files/TaskTwo_ Files/signal1-signal3.txt", l1, l2)


# ______________________________________________ [3]  Multiplying signal by constant _____________________________________________

def MultSignal():
    constant = int(const_num_signals.get())
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, l1, b, _ = read_signal(file_path)

    for i in range(len(b)):
        b[i] = b[i] * constant

    l2 = b  # Sample Amplitude

    plt.plot(l1, l2)
    plt.title(" Signal Multiplying")
    plt.xlabel("Sample Index")
    plt.ylabel("Sample Amplitude")

    # Save the result to a text file on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_file_path = os.path.join(desktop_path, 'result_signal.txt')

    try:
        # Create the directory if it doesn't exist
        os.makedirs(desktop_path, exist_ok=True)

        with open(output_file_path, 'w') as output_file:
            for sample_index, sample_amplitude in zip(l1, l2):
                output_file.write(f"{sample_index} {sample_amplitude}\n")
        messagebox.showinfo("Success", "Result saved to the desktop as 'result_signal.txt'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing the file: {str(e)}")

    plt.show()

    # Rest of your code remains the same

    comparesignals.SignalSamplesAreEqual("Task_Files/TaskTwo_ Files/MultiplySignalByConstant-Signal1 - by 5.txt", l1, l2)


# ------------------------------------------------------- [4] Squaring a Signal --------------------------------------------

def SquareSignal():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, l1, b, _ = read_signal(file_path)

    b = [int(x) for x in b]
    for i in range(len(b)):
        b[i] = b[i] ** 2

    l2 = b  # Sample Amplitude

    plt.plot(l1, l2)
    plt.title(" Signal Squaring")
    plt.xlabel("Sample Index")
    plt.ylabel("Sample Amplitude")

    # Save the result to a text file on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_file_path = os.path.join(desktop_path, 'result_signal.txt')

    try:
        # Create the directory if it doesn't exist
        os.makedirs(desktop_path, exist_ok=True)

        with open(output_file_path, 'w') as output_file:
            for sample_index, sample_amplitude in zip(l1, l2):
                output_file.write(f"{sample_index} {sample_amplitude}\n")
        messagebox.showinfo("Success", "Result saved to the desktop as 'result_signal.txt'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing the file: {str(e)}")

    plt.show()

    # Rest of your code remains the same

    comparesignals.SignalSamplesAreEqual("Task_Files/TaskTwo_ Files/Output squaring signal 1.txt", l1, l2)


# -----------------------------------[5] Squaring a Signal----------------------------------------

def ShiftSignal():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    _, _, _, l1, b, _ = read_signal(file_path)

    l1 = [int(x) for x in l1]
    for i in range(len(l1)):
        l1[i] = l1[i] + int(const_shift_signals.get())

    l2 = b  # Sample Amplitude

    plt.plot(l1, l2)
    plt.title(" Signal Squaring")
    plt.xlabel("Sample Index")
    plt.ylabel("Sample Amplitude")

    # Save the result to a text file on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_file_path = os.path.join(desktop_path, 'result_signal.txt')

    try:
        # Create the directory if it doesn't exist
        os.makedirs(desktop_path, exist_ok=True)

        with open(output_file_path, 'w') as output_file:
            for sample_index, sample_amplitude in zip(l1, l2):
                output_file.write(f"{sample_index} {sample_amplitude}\n")
        messagebox.showinfo("Success", "Result saved to the desktop as 'result_signal.txt'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing the file: {str(e)}")

    plt.show()

    # Rest of your code remains the same

    comparesignals.SignalSamplesAreEqual("Task_Files/TaskTwo_ Files/output shifting by minus 500.txt", l1, l2)


# _________________________________________________[6]Normalization __________________________________________________________________


def normalize_signal():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    normalizeThreshold = normalization.get()

    _, _, _, l1, b, _ = read_signal(file_path)
    normalize_signal = b
    if normalizeThreshold == 0:
        min_val = min(b)
        max_val = max(b)
        normalized_signal = [(x - min_val) / (max_val - min_val) for x in b]
    else:
        min_val = min(b)
        max_val = max(b)
        normalized_signal = [(2 * (x - min_val) / (max_val - min_val)) - 1 for x in b]

    l2 = normalized_signal
    plt.plot(l1, l2)
    plt.show()
    comparesignals.SignalSamplesAreEqual("Task_Files/TaskTwo_ Files/normlize signal 2 -- output.txt", l1, l2)

# _________________________________________________[7]Accumalation of signals __________________________________________________________________
def acc_signal():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    _, _, _, l1, b, _ = read_signal(file_path)
    accumulated_signal = [sum(b[:i + 1]) for i in range(len(b))] # +1 ensures that i is included
    l2 = accumulated_signal
    plt.plot(l1, l2)
    plt.show()
    comparesignals.SignalSamplesAreEqual("Task_Files/TaskTwo_ Files/output accumulation for signal1.txt", l1, l2)



# _____________________________________________________________________________________________________________
# [Finally] Gui Code.
def add_separator():
    separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)
if __name__ == "__main__":
    root = tk.Tk( )
    root.title("LAB Two")
    root.geometry("700x500")

    signalsCount = tk.Label(root, text="Number of signals to add")
    signalsCount.pack()

    entry_num_signals = tk.Entry(root)
    entry_num_signals.pack()

    add_button = tk.Button(root, text="Add Signals", command=addSignals)
    add_button.pack()
    add_separator()
    signalsublabel = tk.Label(root, text="Subtract Two signals")
    signalsublabel.pack()

    sub_button = tk.Button(root, text="subtract Signals", command=subSignal)
    sub_button.pack()
    add_separator()

    signalsCount = tk.Label(root, text="Constant number for multiplication")
    signalsCount.pack()

    const_num_signals = tk.Entry(root)
    const_num_signals.pack()

    Multiply_button = tk.Button(root, text="Multiply Signal with constant", command=MultSignal)
    Multiply_button.pack()
    add_separator()

    square_button = tk.Button(root, text="square of signal", command=SquareSignal)
    square_button.pack()
    add_separator()

    signalsCount = tk.Label(root, text="Value to shift with")
    signalsCount.pack()

    const_shift_signals = tk.Entry(root)
    const_shift_signals.pack()

    add_button = tk.Button(root, text="Shift Signals", command=ShiftSignal)
    add_button.pack()
    add_separator()
    normalization = tk.IntVar()
    normalization.set(0)  # Default normalization choice

    normalize_label = tk.Label(root, text="Select normalization form:")
    normalize_label.pack()

    normalize_radio_0to1 = tk.Radiobutton(root, text="0 to 1", variable=normalization, value=0)
    normalize_radio_0to1.pack()

    normalize_radio_minus1to1 = tk.Radiobutton(root, text="-1 to 1", variable=normalization, value=1)
    normalize_radio_minus1to1.pack()

    normalization_button = tk.Button(root, text="Normalize signal", command=normalize_signal)
    normalization_button.pack()

    accumulation_button = tk.Button(root, text="accumulate signal", command=acc_signal)
    accumulation_button.pack()
    add_separator()

    root.mainloop()
