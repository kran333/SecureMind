import tkinter as tk
import os
from tkinter import filedialog



folder = "E:\\Archives\\AdobeProducts\\python\\test"
folder_path = ''

window = tk.Tk()
window.title(" Simple Windows App ")
window.geometry("700x500")

label = tk.Label(window, text="Click the Button to update this Text", font=('Calibri 15 bold'))
label.pack(pady=20)
def on_click_btn1():
    old = '.txt'
    new = '.bat'
    label["text"] = file_formator(folder, old, new)

def on_click_btn2():
    opt = select_file()
    print(opt)
    label["text"] = f"Selected path {opt}"

def file_formator(folder_path, old_format, new_formate):
    for filename in os.listdir(folder_path):
        infilename = os.path.join(folder_path, filename)
        if not os.path.isfile(infilename): continue
        os.path.splitext(filename)
        newname = infilename.replace(old_format, new_formate)
        os.rename(infilename, newname)

def select_file():
   folder_path = filedialog.askdirectory()
   return folder_path
   # Label(win, text=path, font=13).pack()









btn1 = tk.Button(window, text="Formate", command=on_click_btn1)
btn1.pack(pady=20)

btn2 = tk.Button(window, text="Browse Folder", command=on_click_btn2)
btn2.pack(pady=20)

window.mainloop()
