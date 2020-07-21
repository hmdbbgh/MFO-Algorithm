import tkinter as tk

from tkinter import ttk


class MFO_GUI:

    def __init__(self):

        self.window = tk.Tk(className='Moth-Flame Algorithm')
        
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))
        
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.create_fitnessfunction_combo()

        self.window.mainloop()
    
    def create_fitnessfunction_combo(self):

        self.fitnessfunction_label_combo = tk.Label(
                                            self.window,
                                            text = "Choose your favourite month"
                                        )

        self.fitnessfunction_label_combo.grid(column=0, row=0)

        self.fitnessfunction_commbo = ttk.Combobox(self.window, 
                                    values=[
                                            "January", 
                                            "February",
                                            "March",
                                            "April"])


        self.fitnessfunction_commbo.grid(column=0, row=1)
        self.fitnessfunction_commbo.current(1)

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

if __name__ == '__main__':
    app = MFO_GUI()