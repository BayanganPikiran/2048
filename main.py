import random
import tkinter as tk
from constants import *
import numpy as np



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

        self.score = 0

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

        self.root.bind('<Key>', self.link_keys)
        self.game_won = False
        self.game_lost = False

    # ----------------------------- Frames ------------------------------- #
    def create_game_frame(self):
        game_frame = tk.Frame(self.root, width=PLAY_WIDTH, height=PLAY_HEIGHT, bg=PLAYFIELD_GRAY)
        game_frame.pack(anchor=tk.CENTER, expand=True)
        return game_frame

    def create_footer_frame(self):
        footer = tk.Frame(self.root, width=FOOTER_WIDTH, height=FOOTER_HEIGHT, bg=FOOTER_GRAY)
        footer.pack(anchor=tk.CENTER, expand=True)
        return footer

    # ------------------------- Labels/Button/Toplevels -------------------------- #

    def create_score_label(self):
        score_label = tk.Label(self.footer_frame, text="Score: 2", width=32, height=1, font=LABEL_FONT)
        score_label.grid(row=0, column=0, sticky=tk.W, padx=4, ipady=6, pady=3)
        return score_label

    def create_hi_score_label(self):
        hi_score_label = tk.Label(self.footer_frame, text="High Score: 1", width=32, height=1, font=LABEL_FONT)
        hi_score_label.grid(row=1, column=0, sticky=tk.W, padx=4, ipady=6, pady=3)
        return hi_score_label

    def create_restart_btn(self):
        restart_btn = tk.Button(self.footer_frame, text="Restart", width=5, height=1, font=LABEL_FONT,
                                command=lambda: print("Big fat cock"))
        restart_btn.grid(row=0, column=1, rowspan=2, sticky=tk.E, padx=3, pady=2, ipadx=6, ipady=12)
        return restart_btn

    def create_gameover_toplevel(self):
        game_over = tk.Toplevel(self.root, width=200, height=200, padx=5, pady=5)
        game_over.title("Game Over")
        game_over.wm_transient()
        game_over_label = tk.Label(game_over, text="Your skills weren't up to snuff.  Try again.")
        game_over_label.pack(anchor=tk.CENTER, expand=True)

    def you_win_toplevel(self):
        you_win = tk.Toplevel(self.root, width=200, height=200, padx=5, pady=5)
        you_win.title("You Win")
        you_win.wm_transient()
        you_win_label = tk.Label(you_win, text="You're a bad motherfucker!  You win!")
        you_win_label.pack(anchor=tk.CENTER, expand=True)

    # ------------------------ Matrix Values & Cells ------------------------- #
    def create_board_matrix(self):
        matrix = [[0 for j in range(4)] for i in range(4)]
        return matrix

    def choose_random_index(self):
        index_list = [0, 1, 2, 3]
        random_index = random.sample(index_list, 2)
        return random_index

    def draw_to_board(self, row, col, value):
        self.board_squares[row][col].config(text=value)

    def color_squares(self, row, col, value):
        self.board_squares[row][col].config(bg=BACKGROUND_COLORS.get(str(value)), fg=FONT_COLORS.get(str(value)))

    def populate_vacant_square(self):
        rand_ind = self.choose_random_index()
        rand_val = random.choice([2, 4])
        if self.board_matrix[rand_ind[0]][rand_ind[1]] == 0:
            self.board_matrix[rand_ind[0]][rand_ind[1]] = rand_val
            self.draw_to_board(rand_ind[0], rand_ind[1], str(rand_val))
        else:
            self.populate_vacant_square()

    def start_with_two(self):
        for i in range(2):
            self.populate_vacant_square()
            self.update_board_squares()

    def update_board_squares(self):
        for i in range(4):
            for j in range(4):
                if self.board_matrix[i][j] == 0:
                    self.draw_to_board(i, j, ' ')
                    self.color_squares(i, j, 0)
                else:
                    self.draw_to_board(i, j, self.board_matrix[i][j])
                    self.color_squares(i, j, self.board_matrix[i][j])

    # ------------------------ Movement Configuration ------------------------- #

    def compress_matrix(self):
        temp_matrix = [[0] * 4 for x in range(4)]
        for i in range(4):
            temp_pos = 0
            for j in range(4):
                if self.board_matrix[i][j] != 0:
                    temp_matrix[i][temp_pos] = self.board_matrix[i][j]
                    temp_pos += 1
        self.board_matrix = temp_matrix

    def transpose_matrix(self):
        tp_matrix = np.transpose(self.board_matrix).tolist()
        self.board_matrix = np.transpose(self.board_matrix).tolist()

    def reverse_matrix(self):
        r_matrix = np.flip(self.board_matrix).tolist()
        self.board_matrix = np.flip(self.board_matrix).tolist()

    def merge_cells(self):
        for i in range(4):
            for j in range(3):
                if self.board_matrix[i][j] == self.board_matrix[i][j + 1]:
                    self.board_matrix[i][j] *= 2
                    self.board_matrix[i][j + 1] = 0
                    self.score += self.board_matrix[i][j]
        self.score_label.config(text=self.score)

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.board_matrix[i][j] == self.board_matrix[i][j + 1]:
                    return True
        for i in range(3):
            for j in range(4):
                if self.board_matrix[i][j] == self.board_matrix[i + 1][j]:
                    return True
        return False

    def link_keys(self, event):
        pressed_key = event.keysym
        if pressed_key == 'Up':
            # problem: doesn't go from bottom to top
            self.transpose_matrix()
            self.compress_matrix()
            self.merge_cells()
            self.transpose_matrix()
            self.populate_vacant_square()
            self.update_board_squares()
        if pressed_key == 'Down':
            self.transpose_matrix()
            self.reverse_matrix()
            self.compress_matrix()
            self.merge_cells()
            self.transpose_matrix()
            self.reverse_matrix()
            self.populate_vacant_square()
            self.update_board_squares()
        if pressed_key == 'Left':
            self.compress_matrix()
            self.merge_cells()
            self.populate_vacant_square()
            self.update_board_squares()
        if pressed_key == 'Right':
            # problem: doesn't go from far left to far right
            self.reverse_matrix()
            self.compress_matrix()
            self.merge_cells()
            self.reverse_matrix()
            self.populate_vacant_square()
            self.update_board_squares()

    def play_game(self):
        game_over = False
        self.choose_random_index()
        self.start_with_two()
        while not game_over:

            flag = 0
            for i in range(4):
                for j in range(4):
                    if self.board_matrix[i][j] == 2048:
                        flag = 1
                        break

            if flag == 1:
                self.game_won = True
                # make this a toplevel
                messagebox.showinfo('2048', 'You won!')
                game_over = True

            if not (flag or self.can_merge()):
                self.game_lost = True
                messagebox.showinfo('2048', 'You lost!')
                game_over = True

            self.root.mainloop()


# def restart(board):
#     board.root.destroy()
#     board.play_game()


if __name__ == '__main__':
    board = Board()
    board.play_game()
