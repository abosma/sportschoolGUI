import tkinter as tk
from tkinter import messagebox
import pygubu


class Application:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('createUser.ui')
        self.mainwindow = builder.get_object('Frame_1', master)
        builder.connect_callbacks(self)

    def nextBtn(self):
        if (self.builder.tkvariables['naamVar'].get() == "" or 
            self.builder.tkvariables['geslachtVar'].get() == "" or
            self.builder.tkvariables['dagVar'].get() == "" or
            self.builder.tkvariables['maandVar'].get() == "" or
            self.builder.tkvariables['jaarVar'].get() == "" or
            self.builder.tkvariables['plaatsVar'].get() == "" or
            self.builder.tkvariables['pcodeVar'].get() == "" or
            self.builder.tkvariables['locatieVar'].get() == "" or
            self.builder.tkvariables['nummerVar'].get() == "" or
            self.builder.tkvariables['mailVar'].get() == "" or
            self.builder.tkvariables['abVar'].get() == ""):
            self.builder.tkvariables['errorBox'].set("Een van de velden is niet ingevuld")
        else:
            self.builder.tkvariables['errorBox'].set("Gebruiker aangemaakt")
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()