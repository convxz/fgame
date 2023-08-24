import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 

# создание окна
window = tk.Tk()
# размеры окна
window.geometry("600x400+200+100")
# название окна
window.title("main.")
# создание иконки
img = ImageTk.PhotoImage(Image.open("D:\code\game\src\img\mainicon.png"))
window.iconphoto(False, img)
# создание кадра
frame = ttk.Frame(window, padding=10)
frame.grid()
ttk.Label(frame, text="Hello, World!").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=window.destroy).grid(column=1, row=0)

window.mainloop()
