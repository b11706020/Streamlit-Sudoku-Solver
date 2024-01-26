import streamlit as st

# Sudoku Solver Logic
def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def board_to_string(board):
    return '\n'.join([' '.join([str(cell) for cell in row]) for row in board])

# Streamlit UI
st.title('Sudoku Solver')

board_input = st.text_area("Enter your Sudoku puzzle here, row by row, with spaces and zeros for empty cells:")

if st.button('Solve Sudoku'):
    try:
        board = [[int(num) for num in row.split()] for row in board_input.split('\n')]
        if len(board) != 9 or any(len(row) != 9 for row in board):
            st.error("Invalid Sudoku puzzle. Ensure it's a 9x9 grid.")
        elif solve_sudoku(board):
            st.success("Sudoku solved!")
            st.text(board_to_string(board))
        else:
            st.error("Sudoku puzzle is unsolvable.")
    except ValueError:
        st.error("Invalid input. Please enter only numbers.")
