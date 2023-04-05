
import tkinter
from tkinter import messagebox
turn = 0

x1y1 = " "
x1y2 = " "
x1y3 = " "
x2y1 = " "
x2y2 = " "
x2y3 = " "
x3y1 = " "
x3y2 = " "
x3y3 = " "


def winner(l):
  if ((x1y1 == l and x1y2 == l and x1y3 == l)
      or (x2y1 == l and x2y2 == l and x2y3 == l)
      or (x3y1 == l and x3y2 == l and x3y3 == l)
      or (x1y1 == l and x2y1 == l and x3y1 == l)
      or (x1y2 == l and x2y2 == l and x3y2 == l)
      or (x1y3 == l and x2y3 == l and x3y3 == l)
      or (x1y1 == l and x2y2 == l and x3y3 == l)
      or (x1y3 == l and x2y2 == l and x3y1 == l)):
    return True
  else:
    return False


def isfull():
  flag = True
  if (x1y1.count(" ") > 0 or x1y2.count(" ") > 0 or x1y3.count(" ") > 0
      or x2y1.count(" ") > 0 or x2y2.count(" ") > 0 or x2y3.count(" ") > 0
      or x3y1.count(" ") > 0 or x3y2.count(" ") > 0 or x3y3.count(" ") > 0):
    flag = False
  return flag


def checkScore():
  if winner("X"):
    box = messagebox.showinfo("Winner", "Player 1 won the game")
  elif winner("O"):
    box = messagebox.showinfo("Winner", "Player 2 won the game")
  elif (isfull()):
    box = messagebox.showinfo("Tie Game", "Tie Game")


def setXO_x1y1():
  global turn, x1y1
  if x1y1 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x1y1 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x1y1 = "O"
    turn += 1
    button11.config(text=x1y1)
  checkScore()


def setXO_x1y2():
  global turn, x1y2
  if x1y2 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x1y2 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x1y2 = "O"
    turn += 1
    button12.config(text=x1y2)
  checkScore()


def setXO_x1y3():
  global turn, x1y3
  if x1y3 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x1y3 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x1y3 = "O"
    turn += 1
    button13.config(text=x1y3)
  checkScore()


def setXO_x2y1():
  global turn, x2y1
  if x2y1 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x2y1 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x2y1 = "O"
    turn += 1
    button21.config(text=x2y1)
  checkScore()


def setXO_x2y2():
  global turn, x2y2
  if x2y2 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x2y2 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x2y2 = "O"
    turn += 1
    button22.config(text=x2y2)
  checkScore()


def setXO_x2y3():
  global turn, x2y3
  if x2y3 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x2y3 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x2y3 = "O"
    turn += 1
    button23.config(text=x2y3)
  checkScore()


def setXO_x3y1():
  global turn, x3y1
  if x3y1 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x3y1 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x3y1 = "O"
    turn += 1
    button31.config(text=x3y1)
  checkScore()


def setXO_x3y2():
  global turn, x3y2
  if x3y2 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x3y2 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x3y2 = "O"
    turn += 1
    button32.config(text=x3y2)
  checkScore()


def setXO_x3y3():
  global turn, x3y3
  if x3y3 == ' ':
    if turn % 2 == 0:
      l1.config(bg="red")
      l2.config(bg="green")
      x3y3 = "X"
    else:
      l2.config(bg="red")
      l1.config(bg="green")
      x3y3 = "O"
    turn += 1
    button33.config(text=x3y3)
  checkScore()
def gameBoard():
  global l1, l2, game_board, button11, button12, button13, button21, button22, button23, button31, button32, button33
  game_board = tkinter.Tk()
  game_board.title("Tic Tac Toe")
  l1 = tkinter.Button(game_board, text="Player 1 : X", width=10, bg="green")
  l2 = tkinter.Button(game_board, text="Player 2 : O", width=10, bg="red")
  button11 = tkinter.Button(game_board,
                            command=setXO_x1y1,
                            bd=5,
                            height=4,
                            width=8)
  button12 = tkinter.Button(game_board,
                            command=setXO_x1y2,
                            bd=5,
                            height=4,
                            width=8)
  button13 = tkinter.Button(game_board,
                            command=setXO_x1y3,
                            bd=5,
                            height=4,
                            width=8)
  button21 = tkinter.Button(game_board,
                            command=setXO_x2y1,
                            bd=5,
                            height=4,
                            width=8)
  button22 = tkinter.Button(game_board,
                            command=setXO_x2y2,
                            bd=5,
                            height=4,
                            width=8)
  button23 = tkinter.Button(game_board,
                            command=setXO_x2y3,
                            bd=5,
                            height=4,
                            width=8)
  button31 = tkinter.Button(game_board,
                            command=setXO_x3y1,
                            bd=5,
                            height=4,
                            width=8)
  button32 = tkinter.Button(game_board,
                            command=setXO_x3y2,
                            bd=5,
                            height=4,
                            width=8)
  button33 = tkinter.Button(game_board,
                            command=setXO_x3y3,
                            bd=5,
                            height=4,
                            width=8)
  l1.grid(row=1, column=1)
  l2.grid(row=2, column=1)
  button11.grid(row=3, column=0)
  button12.grid(row=3, column=1)
  button13.grid(row=3, column=2)
  button21.grid(row=4, column=0)
  button22.grid(row=4, column=1)
  button23.grid(row=4, column=2)
  button31.grid(row=5, column=0)
  button32.grid(row=5, column=1)
  button33.grid(row=5, column=2)
  game_board.mainloop()
gameBoard()
