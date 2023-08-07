import random
import tkinter as tk
from constants import *
import numpy as np

sample_matrix = [[0, 0, 2, 0], [1, 2, 0, 4], [0, 0, 0, 5], [0, 3, 0, 8]]

sample_matrix_2 = [[0, 3, 1, 0], [1, 0, 0, 8], [0, 0, 9, 0], [0, 0, 2, 4]]

sample_matrix_3 = [[0, 0, 0, 1], [0, 0, 0, 4], [0, 0, 0, 3], [0, 0, 0, 4]]

sample_matrix_4 = [[0, 0, 0, 5], [0, 3, 0, 8], [0, 0, 2, 0], [1, 2, 0, 4]]


class Board:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(("{}x{}".format(ROOT_WIDTH, ROOT_HEIGHT)))
        self.root.resizable(None, None)
        self.root.configure(background=PLAYFIELD_GRAY)
        self.root.title("2048")

        self.game_frame = self.create_game_frame()
        self.footer_frame = self.create_footer_frame()

        self.score_label = self.create_score_label()
        self.hi_score_label = self.create_hi_score_label()
        self.restart_btn = self.create_restart_btn()

        self.board_matrix = self.create_board_matrix()
        self.board_squares = []
        for i in range(4):
            rows = []
            for j in range(4):
                tile = tk.Label(self.game_frame, text=" ", font=LABEL_FONT, bg=CELL_LT_BLUE,
                                width=10, height=5, relief=tk.SOLID, borderwidth=2)
                tile.grid(row=i, column=j, padx=2, pady=1)
                rows.append(tile)
            self.board_squares.append(rows)

    # ----------------------------- Frames ------------------------------- #
    def create_game_frame(self):
        game_frame = tk.Frame(self.root, width=PLAY_WIDTH, height=PLAY_HEIGHT, bg=PLAYFIELD_GRAY)
        game_frame.pack(anchor=tk.CENTER, expand=True)
        return game_frame

    def create_footer_frame(self):
        footer = tk.Frame(self.root, width=FOOTER_WIDTH, height=FOOTER_HEIGHT, bg=FOOTER_GRAY)
        footer.pack(anchor=tk.CENTER, expand=True)
        return footer

    # ------------------------- Labels & Buttons -------------------------- #

    def create_score_label(self):
        score_label = tk.Label(self.footer_frame, text="Score: 2", width=32, height=1, font=LABEL_FONT)
        score_label.grid(row=0, column=0, sticky=tk.W, padx=4, ipady=6, pady=3)
        return score_label

    def create_hi_score_label(self):
        hi_score_label = tk.Label(self.footer_frame, text="High Score: 1", width=32, height=1, font=LABEL_FONT)
        hi_score_label.grid(row=1, column=0, sticky=tk.W, padx=4, ipady=6, pady=3)
        return hi_score_label

    def create_restart_btn(self):
        restart_btn = tk.Button(self.footer_frame, text="Restart", width=5, height=1, font=LABEL_FONT)
        restart_btn.grid(row=0, column=1, rowspan=2, sticky=tk.E, padx=3, pady=2, ipadx=6, ipady=12)
        return restart_btn

    # ------------------------ Matrix Values & Cells ------------------------- #
    def create_board_matrix(self):
        matrix = [[0 for j in range(4)] for i in range(4)]
        print(f"The starting matrix is: {matrix}")
        return matrix

    def choose_random_index(self):
        index_list = [0, 1, 2, 3]
        random_index = random.sample(index_list, 2)
        print(f"choose_rand_index result: {random_index}")
        return random_index

    def draw_to_board(self, row, col, value):
        self.board_squares[row][col].config(text=value)

    def populate_vacant_square(self):
        # replaces matrix 0 with 2 or 4 and draws value to corresponding board location
        rand_ind = self.choose_random_index()
        rand_val = random.choice([2, 4])
        if self.board_matrix[rand_ind[0]][rand_ind[1]] == 0:
            self.board_matrix[rand_ind[0]][rand_ind[1]] = rand_val
            self.draw_to_board(rand_ind[0], rand_ind[1], str(rand_val))
        else:
            self.populate_vacant_square()
        print(f"The new matrix values are {self.board_matrix}")

    def start_with_two(self):
        for i in range(2):
            self.populate_vacant_square()

    # ------------------------ Movement Configuration ------------------------- #

    def squeeze_matrix(self, matrix):
        mx = matrix
        for i in range(4):
            for j in range(3):
                while mx[i][j] == 0 and mx[i][j + 1] != 0:
                    for row in range(4):
                        for col in range(3):
                            if mx[row][col] == 0:
                                mx[row][col] = mx[row][col + 1]
                                mx[row][col + 1] = 0
        # print(f"This is our new matrix: {mx}")

    def compress(self, matrix):
        self.squeeze_matrix(matrix)
        mx = matrix
        for i in range(4):
            for j in range(3):
                while mx[i][j] == 0 and mx[i][j + 1] != 0:
                    if mx[i][j] == 0:
                        mx[i][j] = mx[i][j + 1]
                        mx[i][j + 1] = 0
        print(f"The compressed matrix is: {mx}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    board.choose_random_index()
    board.start_with_two()
    # board.squeeze_matrix(sample_matrix_4)
    board.compress(sample_matrix)
    board.root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
