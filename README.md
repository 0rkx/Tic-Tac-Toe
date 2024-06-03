# Tic Tac Toe

This project is a simple Tic Tac Toe game implemented using Python's Tkinter library for the graphical user interface.

## Overview

The game allows two players to play Tic Tac Toe by taking turns. Player 1 uses 'X' and Player 2 uses 'O'. The game checks for a winner after each move and declares the result in a pop-up message box. If all squares are filled without a winner, the game declares a tie.

## Features

- Two-player functionality.
- Graphical user interface using Tkinter.
- Winner and tie detection with message box notifications.

## How to Run

To run the game, ensure you have Python installed on your system. You can then run the script directly.

```sh
python tic_tac_toe.py
```
## Code Explanation

### Global Variables

- `turn`: Keeps track of the current turn (Player 1 or Player 2).
- `x1y1, x1y2, x1y3, x2y1, x2y2, x2y3, x3y1, x3y2, x3y3`: Represent the state of each cell in the 3x3 Tic Tac Toe board.

### Functions

- `winner(l)`: Checks if the player using symbol `l` ('X' or 'O') has won.
- `isfull()`: Checks if the board is full.
- `checkScore()`: Checks the current state of the game and displays the result in a message box if there's a winner or a tie.
- `setXO_x1y1(), setXO_x1y2(), setXO_x1y3(), setXO_x2y1(), setXO_x2y2(), setXO_x2y3(), setXO_x3y1(), setXO_x3y2(), setXO_x3y3()`: Set the corresponding cell to 'X' or 'O' based on the current turn and update the board.
- `gameBoard()`: Initializes the game board and the GUI components.
