# Python Tkinter Tic-Tac-Toe

This repository contains a simple, local-multiplayer Tic-Tac-Toe game built with Python and the built-in `tkinter` graphical interface library. The project demonstrates an event-driven user interface where two players take turns marking spaces on a 3x3 grid, with real-time win and draw detection.

## Table of Contents

- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Folder Structure](#folder-structure)
- [Important Code Concepts](#important-code-concepts)
- [Architectural Decisions](#architectural-decisions)
- [Data Model](#data-model)
- [Main User Flows](#main-user-flows)
- [Setup Instructions](#setup-instructions)
- [Available Scripts](#available-scripts)
- [Configuration Notes](#configuration-notes)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Learning Outcomes](#learning-outcomes)
- [Screenshots](#screenshots)
- [License](#license)

## About the Project

This is a standalone desktop application that provides a visual interface for playing the classic game of Tic-Tac-Toe. It allows two players to share a single screen and take turns. The app automatically tracks whose turn it is, updates the UI to reflect valid moves, and evaluates the board after each action to declare a winner or a tie using simple popup dialogues.

Given the current implementation, this is a local-only application. It does not support online multiplayer or AI opponents. The main goal of this repository is to showcase a working desktop UI built purely with standard Python libraries.

## Key Features

**Two-Player Local Interface**
The UI includes a 3x3 grid of clickable buttons. Players take turns clicking available squares, and the application toggles between 'X' and 'O' automatically based on a global turn counter.

**Real-Time Win and Tie Detection**
After every valid move, the application explicitly checks the board state. If a player achieves three matching symbols in a row, column, or diagonal, the game triggers a modal alert declaring the winner. If all squares are filled without a winner, a tie game alert is shown.

**Active Turn Highlighting**
The top of the window features two labels ("Player 1 : X" and "Player 2 : O"). The background colors of these labels alternate between red and green to visually indicate whose turn it is next.

## Tech Stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| Application Language | Python | Core logic and execution environment |
| UI Framework | `tkinter` | Native window management, grids, buttons, and popups |
| Dependency Management | Poetry | Declared via `pyproject.toml` and `poetry.lock` |

## System Architecture

The application runs as a single-threaded, event-driven desktop window.

```txt
Player Input (Mouse Click)
  ↓
Tkinter Button Event Handler (e.g., setXO_x1y1)
  ↓
Global State Update (turn counter, grid cell variables)
  ↓
Board Evaluation (winner() and isfull())
  ↓
UI Update (Button text, player turn colors, or MessageBox popup)
```

## Folder Structure

```txt
.
  main.py           Main application entry point containing all GUI layout and logic
  pyproject.toml    Poetry configuration and dependency list
  poetry.lock       Locked dependency versions
```

## Important Code Concepts

**Event Handlers and Callbacks**
The UI is driven by callback functions assigned to the `command` attribute of each `tkinter.Button`. Currently, there are nine separate functions (like `setXO_x1y1` through `setXO_x3y3`), each hardcoded to a specific grid coordinate.

**Global State Mutation**
The application relies heavily on Python `global` variables to maintain state across the different button click events. The `turn` integer tracks how many moves have been made, while nine string variables (`x1y1`, etc.) store the current marker in each position.

## Architectural Decisions

**Using `tkinter` for the UI**
`tkinter` is included in the Python standard library, making it the most immediate choice for a simple desktop application prototype. It avoids the need for users to install external UI frameworks like PyQt or Kivy to run the application.

**Explicit State Variables over Collections**
The current implementation uses nine distinct global string variables to represent the board rather than a 2D array or list. This makes the `winner()` checking logic highly explicit, as it manually verifies all eight possible winning combinations using long `if/or` statements. While this is less scalable for larger board games, it works functionally for a fixed 3x3 Tic-Tac-Toe grid and avoids complex index calculations during the prototype stage.

**No Object-Oriented Encapsulation**
The codebase is currently written in a procedural style without classes. The `tkinter` components and game logic exist in the global scope. This keeps the file very short and readable for beginners, but it restricts the ability to easily restart the game or run multiple instances simultaneously without restarting the script.

## Data Model

The domain model is extremely simple and handled entirely via primitive global variables in `main.py`:

- **Turn Counter (`turn`):** An integer that increments on each valid move. If `turn % 2 == 0`, it is Player 1's turn ('X'); otherwise, it is Player 2's ('O').
- **Board Cells (`x1y1` ... `x3y3`):** Nine strings initialized with a single space `" "`. These update to `"X"` or `"O"` when a user interacts with the corresponding button.

## Main User Flows

**Playing a Match**
1. A user runs the script and the `tkinter` window opens.
2. Player 1 clicks an empty square. The button text updates to "X", and the UI updates the top labels to show it is Player 2's turn.
3. Player 2 clicks an empty square. The button updates to "O".
4. This continues until the `checkScore()` function detects a win condition or a full board.
5. A `messagebox` popup appears declaring the result.
6. Currently, the user must close and restart the application to play again, as there is no reset button implemented.

## Setup Instructions

### Prerequisites
- Python 3.10 or higher.
- `tkinter` (usually bundled with Python, but on some Linux distributions, it may require a separate package installation like `sudo apt-get install python3-tk`).

### Installation and Running Locally

Because the application relies entirely on the standard library for its runtime logic, you can run it directly without installing external packages:

```bash
git clone <repository-url>
cd <repository-folder>
python main.py
```

Alternatively, if you wish to use the declared Poetry environment:
```bash
poetry install
poetry run python main.py
```

### Environment Variables
No required environment variables were found in the current codebase.

## Available Scripts

There are no formal helper scripts defined in the current project root beyond the standard execution of the Python script.

## Configuration Notes

- `pyproject.toml`: Configures the Poetry environment. While it includes dependencies like `Flask` and `numpy`, these are not actually imported or utilized by `main.py`. The running game only requires `tkinter`.

## Testing

Automated tests are not currently included in the repository.

Given the tightly coupled nature of the global state and the UI components, writing unit tests would be challenging without refactoring. Realistic future test areas would involve:
- Extracting the `winner()` and `isfull()` logic into pure functions that accept a 2D array, allowing them to be unit tested independently of `tkinter`.

## Deployment

No deployment-specific configuration was found. As a native desktop UI application, it is intended to be run locally via the Python interpreter rather than deployed to a web server.

## Future Improvements

- **Game Reset Capability:** Adding a "Restart" button to clear the board variables and reset the turn counter without closing the application window.
- **Refactoring to a Class Component:** Wrapping the `gameBoard` and state variables into a Python class to avoid using `global` keywords and make the code more maintainable.
- **Dynamic Board State:** Converting the nine individual `xNyN` variables into a single 3x3 list or dictionary to simplify the win-checking logic and allow for iterative loops instead of long explicit conditionals.
- **Consolidated Event Handlers:** Passing the coordinates of the button click into a single `setXO(row, col)` function instead of using nine hardcoded functions.

## Learning Outcomes

This project demonstrates practical familiarity with event-driven programming and graphical user interfaces in Python. It shows how to bind user inputs to state changes, how to selectively re-render UI elements (like changing button text and label background colors), and how to logically evaluate application state after each user interaction.

## Screenshots

Screenshots can be added here to show the main playing grid, the turn indicators, and the winner popups.

## License

License information has not been specified yet.
