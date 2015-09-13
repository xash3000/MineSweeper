#!/usr/bin/python3.4
from tkinter import *
import random

class Game:

    def __init__(self, master, flags=20):
        self.flags = flags
        self.createButtons(master)

    def createButtons(self, parent):
        self.buttons = {}
        row = 0
        col = 0
        for x in range(0, 100):
            status = random.choice(['safe', 'danger'])
            self.buttons[x] = [
            Button(parent),
            status,
            row,
            col
            ]

            self.buttons[x][0].bind('<Button-1>', self.leftClick_w(x))
            self.buttons[x][0].bind('<Button-3>', self.rightClick_w(x))
            col += 1
            if col == 10:
                col = 0
                row += 1
            for k in self.buttons:
                self.buttons[k][0].grid(row= self.buttons[k][2], column= self.buttons[k][3])

    def leftClick_w(self, x):
        return lambda Button: self.leftClick(x)

    def rightClick_w(self, x):
        return lambda Button: self.rightClick(x)

    def leftClick(self, btn):
        end = False
        check = self.buttons[btn][1]
        if check == 'safe':
            self.buttons[btn][0].config(bg='green')
            self.buttons[btn][0].config(state='disabled')
            self.buttons[btn][1] = 'clicked'
            self.showNearby(btn)
            for i in self.buttons:
                if self.buttons[i][1] == 'safe':
                    end = False
                else:
                    end = True
            if end == True:
                self.victory()
        else:
            self.buttons[btn][0].config(bg='red')
            self.buttons[btn][0].config(state='disabled')
            self.lost()

    def rightClick(self, btn):
        if self.flags > 0:
            self.buttons[btn][0].config(bg='blue')
            self.buttons[btn][0].config(state='disabled')
            self.buttons[btn][1] = 'safe'
        self.flags -= 1

    def showNearby(self, btn):
        if btn > 10 and btn < 90:
            self.possible = [btn-11,btn+11, btn-10, btn+10,btn-9, btn+9,btn+1, btn-1]
            for i in self.possible:
                if self.buttons[i][1] == 'safe':
                    self.buttons[i][0].config(bg='green')
                    self.buttons[i][0].config(state='disabled')

    def lost(self):
        global root
        root.quit()

    def victory(self):
        global root
        root.quit()


def main():
    global root
    root = Tk()
    root.title('MiNeSwEePeR')
    game = Game(root)
    root.mainloop()

if __name__ == '__main__':
    main()
