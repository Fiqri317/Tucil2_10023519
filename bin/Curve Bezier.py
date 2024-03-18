import tkinter as tk
import subprocess

def run_bruteforce():
    subprocess.Popen("bruteforce.bat", shell=True)

def run_divide_conquer():
    subprocess.Popen("divide_and_conquer.bat", shell=True)

root = tk.Tk()
root.title("Pilih Program")

label = tk.Label(root, text="Silakan pilih program yang ingin dijalankan:")
label.pack()

bruteforce_button = tk.Button(root, text="Brute Force", command=run_bruteforce)
bruteforce_button.pack()

divide_conquer_button = tk.Button(root, text="Divide and Conquer", command=run_divide_conquer)
divide_conquer_button.pack()

quit_button = tk.Button(root, text="Keluar", command=root.quit)
quit_button.pack()

root.mainloop()
