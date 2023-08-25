import tkinter as tk
from PIL import Image, ImageTk 


class Main:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title("main.")
        img = ImageTk.PhotoImage(Image.open("src\img\mainicon.png"))
        self.root.iconphoto(False, img)
        self.canvas = tk.Canvas(width=500, height=500, bg="yellow").pack()


    def run(self):
        self.interface()
        self.root.mainloop()


    def interface(self):
        self.root.bind('<B1-Motion>', self.move)


    def move(self, event):
        x = event.x
        y = event.y

        print(x, y)


App = Main()
App.run()