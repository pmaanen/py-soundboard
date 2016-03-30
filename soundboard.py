import Tkinter as tki # Tkinter -> tkinter in Python 3
from tkFileDialog import askopenfilename, askopenfilenames
from math import sqrt,floor,ceil
import vlc

class myButton:
    def __init__(self,parent):
        self.parent=parent
        self.myButton=tki.Button(parent,text="",width=20,height=5, command=self.onLeftClick,bg='green')
        self.hasFile=False
        self.file=None
        self.isPlaying=False
        self.p=None
        self.myButton.bind("<Button-2>",self.onRightClick)

    def onRightClick(self,event):
        if(self.isPlaying):
            self.p.stop()
        if(self.file is None):
            self.parent.master.myButtons.remove(self)
            self.parent.master.drawButtons()
        self.file=None
        self.hasFile=False
        self.p=None
        self.isPlaying=False
        self.myButton.config(text="")
        
    def onLeftClick(self):
        if(not self.hasFile):
            self.file=askopenfilename()
            self.initFile()
        else:
            self.playFile()

    def initFile(self):
        self.p = vlc.MediaPlayer("file://"+self.file)
        self.hasFile=True
        self.myButton.config(text=self.file.split("/")[-1])

    def playFile(self):
        if(self.isPlaying):
            self.p.stop()
            self.isPlaying=False
            self.myButton.config(fg="red")
            self.myButton.config(bg="red")
            self.myButton.config(activeforeground="red")
        else:
            self.p.play()
            self.isPlaying=True
            self.myButton.config(fg="green")
            self.myButton.config(bg="green")
            self.myButton.config(activeforeground="green")

class GUI(tki.Tk):
    def __init__(self):
        tki.Tk.__init__(self)
        # create a frame
        self.aFrame = tki.Frame(self, width=512, height=512)
        self.aFrame.pack()
        self.menubar=tki.Menu(self.aFrame)
        # create a pulldown menu, and add it to the menu bar
        self.aMenu = tki.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.aMenu)
        self.aMenu.add_command(label="Add button", command=self.addButton,accelerator="Cmd+a")
        self.aMenu.add_command(label="Add files", command=self.addFiles,accelerator="Cmd+f")
        self.aMenu.add_command(label="Quit", command=exit,accelerator="Cmd+q")
        self.aMenu.bind_all("<Command-a>", self.addButton)
        self.aMenu.bind_all("<Command-f>", self.addFiles)
        # attach buttons to frame
        self.myButtons=[]
        for _ in range(9):
                self.myButtons.append(myButton(self.aFrame))
        self.drawButtons()
        self.config(menu=self.menubar)
        
    def addFiles(self,event=0):
        files=list(askopenfilenames())
        for file in files:
            for button in self.myButtons:
                if(button.hasFile==False and len(files)!=0):
                    button.file=files.pop()
                    button.initFile()
        for file in files:
            self.addButton()
            self.myButtons[-1].file=file
            self.myButtons[-1].initFile()

    def drawButtons(self):
        nY=int(ceil(sqrt((len(self.myButtons)))))
        ii=0
        for y in range(nY+1):
            for x in range(nY):
                if(ii<len(self.myButtons)):
                    self.myButtons[ii].myButton.grid(row=y, column=x)
                    ii+=1
    def addButton(self,event=None):
        self.myButtons.append(myButton(self.aFrame))
        self.drawButtons()
    

gui = GUI()
gui.mainloop()
