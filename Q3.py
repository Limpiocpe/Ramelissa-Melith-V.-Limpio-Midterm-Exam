# Code for Question 3
import tkinter as tk

class FullnameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Midterm in OOP")
        self.root.geometry("410x250")

        self.label = tk.Label(root, text="Enter your fullname:", fg="red", font=("Arial", 7))
        self.label.place(x=40, y=120)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.place(x=210, y=120, width=165, height=22)

        self.button = tk.Button(
            root,
            text="Click to display your Fullname",
            fg="red",
            font=("Arial", 7),
            command=self.display_name
        )
        self.button.place(x=40, y=155)

        self.output = tk.Entry(root, font=("Arial", 12))
        self.output.place(x=210, y=155, width=165, height=22)

    def display_name(self):
        self.output.delete(0, tk.END)
        self.output.insert(0, self.entry.get())


root = tk.Tk()
app = FullnameApp(root)
root.mainloop()
