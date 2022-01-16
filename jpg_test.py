from tkinter.messagebox import showinfo

from PIL import Image, ImageTk
import PIL
import os
import glob
import math
import \
    tkinter as tk
# link: https://stackoverflow.com/questions/17466561/best-way-to-strucd yhn6ture-a-tkinter-application
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import tkinter.ttk as ttk
from tkinter import filedialog


root = tk.Tk()
root.title('Pictures to Onedrive')
root.geometry('1500x1000')

img_path = os.path.join(r'C:\Users\lukas\Pictures/', r'towar.jpg')
image_resized = Image.open(img_path)
image_resized = image_resized.resize((200, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image_resized)
img = tk.PhotoImage(file=img_path)
label1 = tk.Label(root, image=img)
label1.pack()


root.mainloop()