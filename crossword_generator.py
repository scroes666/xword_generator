import numpy as np
from x_word_cells import *
# import tkinter as tk
import csv

n = 15
global_grid_version = 1


def assign_grid_values(size: int):
    assigned_grid = np.zeros((size, size)).tolist()
    i = 1
    for row in assigned_grid:
        j = 1
        for _ in row:
            assigned_grid[i - 1][j - 1] = Cell(i, j)
            j += 1
        i += 1
    return assigned_grid


x_word = assign_grid_values(n)


def change_cell(grid: list, row: int, column: int, new_value: str):
    new_cell = Cell(row, column)
    if new_value == "#":
        new_cell.set_black()
        opposite_cell = grid[len(grid) - row][len(grid) - column]
        opposite_cell.set_black()
    elif new_value == "?":
        new_cell.se()
        opposite_cell = grid[len(grid) - row][len(grid) - column]
        opposite_cell.set_black()
    if new_value.isalpha():
        new_cell.set_letter(new_value)
    grid[row - 1][column - 1] = new_cell
    return grid


def save_grid(grid: list):
    f = "sample_grid.v" + str(global_grid_version) + ".csv"
    with open(f, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in grid:
            writer.writerow(row)


def valid_word(grid: list, direction: str, start_row: int, start_col: int, word: str):
    length = len(word)
    size = len(grid)
    zero_indexed_row = start_row - 1
    zero_indexed_col = start_col - 1
    if direction.lower() not in ['across', 'down']:
        raise ValueError("Invalid direction. Please use 'across' or 'down'.")
    if length > size or (
            direction == "across" and length + zero_indexed_col > size) or (
            direction == "down" and length + zero_indexed_row - 1 > size):
        raise OutOfBoundsError
    else:
        return True


def add_word(grid: list, direction: str, start_row: int, start_col: int, word: str):
    i = 0
    try:
        if not valid_word(grid,direction,start_row,start_col,word):
            return
        for _ in word:
            if direction == "across":
                change_cell(grid, start_row, start_col + i, word[i])
                i += 1
            elif direction == "down":
                change_cell(grid, start_row + i, start_col, word[i])
                i += 1
        return grid
    except OutOfBoundsError as e:
        print("An Error Occurred: ", e.message)


def reset_grid(grid):
    i = 1
    for row in grid:
        j = 1
        for _ in row:
            grid[i - 1][j - 1] = Cell(i, j)
            j += 1
        i += 1
    return grid
