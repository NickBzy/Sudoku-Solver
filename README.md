# Sudoku Solver

## Overview
This project is a **Sudoku Solver** written in Python that utilizes a **backtracking algorithm** to solve Sudoku puzzles efficiently. The program takes an unsolved Sudoku board, fills in the missing numbers while ensuring that all Sudoku rules are followed, and prints the solved board.

## Features
- Implements the **backtracking algorithm** to find a solution.
- Handles multiple board inputs.
- Prints the Sudoku board before and after solving.
- Validates numbers based on Sudoku rules:
  - No duplicate numbers in the same **row**.
  - No duplicate numbers in the same **column**.
  - No duplicate numbers in the same **3×3 sub-grid**.

## How It Works
1. The program starts by displaying **two pre-defined Sudoku boards**.
2. The user selects a board to solve.
3. The **backtracking algorithm** is applied to find a valid solution.
4. The solved Sudoku board is displayed.

## Usage
### **Requirements**
- Python 3.x

### **Run the Program**
1. Clone the repository or download `sudokuSolver.py`.
2. Open a terminal and navigate to the script's directory.
3. Run the script:
   ```bash
   python sudokuSolver.py
4. Select which board you want to solve (1 or 2).
5. View the solved Sudoku board in the console.

## Code Breakdown
### **Key Functions:**
- `print_board(board)`: Displays the Sudoku board with proper formatting.
- `find_empty(board)`: Locates the next empty cell (represented by `0`).
- `valid(board, num, pos)`: Checks if a number placement is valid.
- `solve(board)`: Implements the **backtracking algorithm** to fill in the board.

## Example Output
```bash
Welcome to the Sudoku Solver
Boards before solving:
1)
0 1 0 | 8 0 0 | 0 0 2
0 5 0 | 0 0 3 | 9 0 0
4 0 8 | 5 0 0 | 0 0 0
- - - - - - - - - - - - 
...
Which board would you like to solve: 1
Solved board:
6 1 9 | 8 4 7 | 3 5 2
...
Thank you for using the Sudoku Solver! ```

## Future Improvements
- Allow users to input their own Sudoku board.
- Add a graphical user interface (GUI) for better user experience.
- Optimize the solving algorithm for better performance.

## Author
**Nicolas Buu**

---
This Sudoku solver is a simple yet powerful tool for solving puzzles using backtracking. Try it out and improve your Sudoku skills!
