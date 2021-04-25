#!/usr/bin/env python3

# Standard Imports
import random

# Third Party Imports

# Custom Imports

def build_board(rows, columns, mines):
    # Create empty board
    board=[]
    for c in range(0,columns):
        board.append([])

        for r in range(0,rows):
            board[c].append(" ")

    board = generate_mines(board, mines)
    board = generate_clues(board)
    return board

def generate_mines(board, mines):
    c = len(board)
    r = len(board[0])

    mineXY = []
    for mine in range(0, mines):
        x = (random.randint(0, r-1))
        y = (random.randint(0, c-1))
        xy = (x, y)

        while xy in mineXY:
            x = (random.randint(0, r-1))
            y = (random.randint(0, c-1))
            xy = (x, y)

        mineXY.append(xy)

    for xy in mineXY:
        x = xy[0]
        y = xy[1]

        board[y][x] = "X"

    return board

def generate_clues(board):
    c = len(board)
    r = len(board[0])

    for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] != "X":
                    neighbours = 0

                    # Row Above
                    if y != 0:
                        if x != 0:
                            if board[y-1][x-1] == "X": neighbours = neighbours + 1
                        if board[y-1][x] == "X": neighbours = neighbours + 1
                        if x != len(board[y])-1:
                            if board[y-1][x+1] == "X": neighbours = neighbours + 1

                    # Current Row
                    if x != 0:
                        if board[y][x-1] == "X": neighbours = neighbours + 1
                    if x != len(board[y])-1:
                        if board[y][x+1] == "X": neighbours = neighbours + 1

                    # Row Below
                    if y != len(board)-1:
                        if x != 0:
                            if board[y+1][x-1] == "X": neighbours = neighbours + 1
                        if board[y+1][x] == "X": neighbours = neighbours + 1
                        if x != len(board[y])-1:
                            if board[y+1][x+1] == "X": neighbours = neighbours + 1

                    if neighbours != 0:
                        board[y][x] = str(neighbours)

    return board
