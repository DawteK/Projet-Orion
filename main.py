import tkinter as tk

from .projet.interface import Interface
from .projet.assistant import Assistant
from projet.interface import run_interface


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Assistant personnel")

        self.label = tk.Label(master, text="Dites quelque chose à votre assistant:")
        self.label.pack()

        self.textbox = tk.Text(master, height=10, width=50)
        self.textbox.pack()

        self.button = tk.Button(master, text="Parler", command=self.speech_recognition)
        self.button.pack()

        self.assistant = Assistant()

    def speech_recognition(self):
        text = self.assistant.listen()
        self.textbox.delete(1.0, tk.END)
        self.textbox.insert(tk.END, text)
        self.assistant.respond(text)

root = tk.Tk()
gui = GUI(root)
root.mainloop()


if __name__ == "__main__":
    run_interface()
