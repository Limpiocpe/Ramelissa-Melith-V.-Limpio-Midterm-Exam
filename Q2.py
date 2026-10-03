# Code for Question 2
import tkinter as tk


class ColorChanger:
    def __init__(self, root):
        self.root = root
        self.root.title("Special Midterm Exam in OOP")
        self.root.geometry("420x370")

        self.button = tk.Button(
            root,
            text="Click to Change Color",
            command=self.change_color
        )
        self.button.place(relx=0.5, rely=0.3, anchor="center")

    def change_color(self):
        self.button.config(bg="yellow")


root = tk.Tk()
app = ColorChanger(root)
root.mainloop()
