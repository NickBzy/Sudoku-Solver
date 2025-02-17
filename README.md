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
