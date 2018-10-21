from tkinter import *
from tkinter import font
class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=50)
        police = font.Font(self, size=20, family='Times New Roman')
        self.t = Label(self, text="Blue's turn", font=police)
        self.t.grid(sticky=NSEW, pady=20)
class point(object):
    def __init__(self, x, y, can, colo="white"):
        self.can = can
        self.x = x
        self.y = y
        self.colo = colo
        self.tour = 1
        self.r = 50
        self.point = self.can.create_oval(self.x + 20, self.y + 20, self.x + 60, self.y + 60, fill=colo, outline="black")
    def changeColour(self, colo):
        self.can.itemconfigure(self.point, fill=colo)
        self.colo = colo
class Board(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=550, height=400, bg="Black")
        self.player = 1
        self.colo = "blue"
        self.p = []
        self.perm = True
        for i in range(0, 340, int(400 / 8)):
            liste_rangee = []
            for j in range(0, 440, int(500 / 8)):
                liste_rangee.append(point(j, i, self))
            self.p.append(liste_rangee)
        self.bind("<Button-1>", self.detCol)
    def detCol(self, event):
        if self.perm:
            col = int(event.x / 60)
            lig = 0

            lig = 0
            while lig < len(self.p):
                if self.p[0][col].colo == "red" or self.p[0][0].colo == "blue":
                    break
                if self.p[lig][col].colo == "red" or self.p[lig][col].colo == "blue":
                    self.p[lig - 1][col].changeColour(self.colo)
                    break
                elif lig == len(self.p) - 1:
                    self.p[lig][col].changeColour(self.colo)
                    break

                if self.p[lig][col].colo != "red" and self.p[lig][col].colo != "blue":
                    lig += 1
            if self.player == 1:
                self.player = 2
                info.t.config(text="Red's Turn")
                self.colo = "red"
            elif self.player == 2:
                self.player = 1
                info.t.config(text="blue's Turn")
                self.colo = "blue"
            self.HRZ()
            self.VRT()
            self.Diag1()
            self.Diag2()
    def HRZ(self):
        i = 0
        while (i < len(self.p)):
            j = 0
            while (j < 4):
                if (self.p[i][j].colo == self.p[i][j + 1].colo == self.p[i][j + 2].colo == self.p[i][j + 3].colo ==self.p[i][j + 4].colo == "red"):
                    info.t.config(text="Red Wins !")
                    self.perm = False
                    break
                elif (self.p[i][j].colo == self.p[i][j + 1].colo == self.p[i][j + 2].colo == self.p[i][j + 3].colo ==self.p[i][j + 4].colo =="blue"):
                    info.t.config(text="Blue Wins !")
                    self.perm = False
                    break
                j += 1
            i += 1
    def VRT(self):
        i = 0
        while (i < 3):
            j = 0
            while (j < len(self.p[i])):
                if (self.p[i][j].colo == self.p[i + 1][j].colo == self.p[i + 2][j].colo == self.p[i + 3][j].colo ==self.p[i + 4][j].colo =="red"):
                    info.t.config(text="Red Wins !")
                    self.perm = False
                    break
                
                elif (self.p[i][j].colo == self.p[i + 1][j].colo == self.p[i + 2][j].colo == self.p[i + 3][j].colo ==self.p[i + 4][j].colo =="blue"):
                    info.t.config(text="Blue Wins !")
                    self.perm = False
                    break
                j += 1
            i += 1

    def Diag1(self):
        i = 0
        while (i < 3):
            j = 0
            while (j < 3):
                if (self.p[i][j].colo == self.p[i + 1][j + 1].colo == self.p[i + 2][j + 2].colo == self.p[i + 3][j + 3].colo =="red"):
                    info.t.config(text="Red Wins !")
                    self.perm = False
                    break
                elif (self.p[i][j].colo == self.p[i + 1][j + 1].colo == self.p[i + 2][j + 2].colo == self.p[i + 3][j + 3].colo =="blue"):
                    info.t.config(text="Blue Wins !")
                    self.perm = False
                    break
                j += 1
            i += 1
    def Diag2(self):
        i = 0
        while (i < 3):
            j = len(self.p[i]) - 1
            while (j > len(self.p) - 4):
                if (self.p[i][j].colo == self.p[i + 1][j - 1].colo == self.p[i + 2][j - 2].colo == self.p[i + 3][j - 3].colo == "red"):
                    info.t.config(text="Red Wins !")
                    self.perm = False
                    break
                elif (self.p[i][j].colo == self.p[i + 1][j - 1].colo == self.p[i + 2][j - 2].colo == self.p[i + 3][j - 3].colo =="blue"):
                    info.t.config(text="Blue Wins !")
                    self.perm = False
                    break
                j -= 1
            i += 1


root = Tk()
root.geometry("500x550")
root.title("connect4 project.")

info = Info(root)
info.grid(row=0, column=0)

t = Board(root)
t.grid(row=1, column=0)


def res():
    global info
    info.t.config(text="")

    info = Info(root)
    info.grid(row=0, column=0)
    t = Board(root)
    t.grid(row=1, column=0)
Button(root, text="Restart", command=res).grid(row=2, column=0, pady=30)
root.mainloop()

