import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.myCanvas=tk.Canvas(self.mainWin, bg='purple', width=400, height=300)
        self.myCanvas.grid(row=0, column=0)
        self.text1=self.myCanvas.create_text(200,150, fill='white', text='Dory')
        self.mainWin.bind("<Return>", self.move_callback)
        self.mainWin.bind("<w>", self.move_callback)
        self.mainWin.bind("<a>", self.move_callback)
        self.mainWin.bind("<s>", self.move_callback)
        self.mainWin.bind("<d>", self.move_callback)
        self.mainWin.bind("<Up>", self.move_callback)
        self.mainWin.bind("<Down>", self.move_callback)
        self.mainWin.bind("<Left>", self.move_callback)
        self.mainWin.bind("<Right>", self.move_callback)
    def run(self):
        self.mainWin.mainloop()
    def move_callback(self, event):
        thing=event.keysym
        if thing == "Up" or thing == "w":
            self.myCanvas.move(self.text1, 0, -10)
        elif thing == "Down" or thing == "s":
            self.myCanvas.move(self.text1, 0, 10)
        elif thing == "Left" or thing == "a":
            self.myCanvas.move(self.text1, -10, 0)
        elif thing == "Right" or thing == "d":
            self.myCanvas.move(self.text1, 10, 0)




# ----- Main program -----
myGui = BasicGui()
myGui.run()