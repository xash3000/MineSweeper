#!/usr/bin/python3.4
from tkinter import *
from tkinter.messagebox import *
import random

class Game:

    def __init__(self, master, flags=50):

        self.flags = flags
        self.createButtons(master)

        self.bottomFrame = Frame(root)
        self.bottomFrame.grid(row=11, columnspan=10)

        self.flagRemainning = Label(self.bottomFrame, text='flag Remainning : '+str(self.flags))
        self.flagRemainning.grid(row=12)

        self.quitBtn = Button(self.bottomFrame, text='Quit', command=self.quit)
        self.quitBtn.grid(row=13, columnspan=2)

    def createButtons(self, parent):
        self.buttons = {}
        row = 0
        col = 0
        for x in range(0, 200):
            status = random.choice(['safe', 'danger'])
            self.buttons[x] = [
            Button(parent, bg='#8a8a8a'),
            status,
            row,
            col
            ]

            self.buttons[x][0].bind('<Button-1>', self.leftClick_w(x))
            self.buttons[x][0].bind('<Button-3>', self.rightClick_w(x))
            col += 1
            if col == 20:
                col = 0
                row += 1
            for k in self.buttons:
                self.buttons[k][0].grid(row= self.buttons[k][2], column= self.buttons[k][3])


    #i don't know why but you'll get error if you remove these two functions
    def leftClick_w(self, x):
        return lambda Button: self.leftClick(x)

    def rightClick_w(self, x):
        return lambda Button: self.rightClick(x)

    def leftClick(self, btn):
        end = False
        check = self.buttons[btn][1]
        if check == 'safe':
            self.buttons[btn][0].config(bg='green')
            self.buttons[btn][0].config(state='disabled', relief=SUNKEN)
            self.buttons[btn][1] = 'clicked'
            self.showNearby(btn)
            for i in self.buttons:
                if self.buttons[i][1] == 'safe':
                    end = False
            if end == True:
                self.victory()
        else:
            self.buttons[btn][0].config(bg='red')
            self.buttons[btn][0].config(state='disabled', relief=SUNKEN)
            self.lost()

    def rightClick(self, btn):
        if self.flags > 0:
            self.buttons[btn][0].config(bg='blue')
            self.buttons[btn][0].config(state='disabled', relief=SUNKEN)
            self.buttons[btn][1] = 'safe'
        self.flags -= 1
        self.flagRemainning.config(text= 'flag Remainning : '+str(self.flags))

    def showNearby(self, btn):
        if btn > 10 and btn < 190:
            self.possible = [btn-21,btn+21, btn-20, btn+20,btn-19, btn+19,btn+1, btn-1]
            for i in self.possible:
                if self.buttons[i][1] == 'safe':
                    self.buttons[i][0].config(bg='green')
                    self.buttons[i][0].config(state='disabled', relief=SUNKEN)

    def lost(self):
        global root
        msg = 'you lose ! do you want to play again?'
        answer = askquestion('play again',msg)
        if answer == 'yes':
            self.reset()
        else:
            self.quit()

    def victory(self):
        global root
        msg = 'congratulations you won ! do you want to play again?'
        answer = askquestion('play again',msg)
        if answer == 'yes':
            self.reset()
        else:
            self.quit()

    def reset(self):
        self.flags = 20
        for i in self.buttons:
            self.buttons[i][0].config(bg='#8a8a8a')
            self.buttons[i][0].config(state='normal', relief=RAISED)
            self.buttons[i][1] = random.choice(['safe', 'danger'])

    def quit(self):
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
