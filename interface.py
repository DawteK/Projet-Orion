import tkinter as tk
from projet.assistant import Assistant

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Assistant personnel")

        self.label = tk.Label(master, text="Dites quelque chose à votre assistant:")
        self.label.pack()

        self.textbox = tk.Text(master, height=10, width=50)
        self.textbox.pack()

        self.assistant = Assistant()

        self.button = tk.Button(master, text="Parler", command=self.speech_recognition)
        self.button.pack()

        self.textbox.bind("<Return>", self.on_enter)

    def on_enter(self, event):
        self.speech_recognition()

    def speech_recognition(self):
        text = self.assistant.listen()
        self.textbox.delete(1.0, tk.END)
        self.textbox.insert(tk.END, text)
        self.assistant.respond(text)

def run_interface():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
