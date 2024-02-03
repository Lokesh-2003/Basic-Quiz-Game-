import random
import tkinter as tk
import matplotlib
matplotlib.use("Agg")  

class Game2048:
    def __init__(self):
        self.board_size = 4
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.score = 0
        self.high_score = 0
        self.game_over = False

    def start_game(self):
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.score = 0
        self.game_over = False
        self.spawn_random_tile()
        self.spawn_random_tile()

    def spawn_random_tile(self):
        empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = random.choice([2, 4])

    def move(self, direction):
        rotated_board = self.rotate_board(direction)
        for i in range(self.board_size):
            rotated_board[i] = self.compress_tiles(rotated_board[i])
            rotated_board[i] = self.merge_tiles(rotated_board[i])
            rotated_board[i] = self.compress_tiles(rotated_board[i])
        self.board = self.rotate_board(direction, rotated_board)
        self.spawn_random_tile()
        self.update_board()

    def merge_tiles(self, row):
        for i in range(self.board_size - 1, 0, -1):
            if row[i] == row[i - 1] and row[i] != 0:
                row[i] *= 2
                self.score += row[i]
                row[i - 1] = 0
        return row

    def compress_tiles(self, row):
        compressed_row = [val for val in row if val != 0] + [0] * row.count(0)
        return compressed_row

    def rotate_board(self, direction, board=None):
        if board is None:
            board = self.board.copy()
        if direction == 'right':
            return [list(reversed(col)) for col in zip(*board)]
        elif direction == 'left':
            return [list(col) for col in zip(*reversed(board))]
        elif direction == 'down':
            return list(reversed(board))
        elif direction == 'up':
            return board

    def is_game_over(self):
        pass

    def update_score(self, merged_values):
        pass


class Game2048GUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.title("2048 Game")
        self.geometry("400x400")
        self.bind("<Key>", self.handle_key_press)
        self.create_widgets()

    def create_widgets(self):
        self.score_label = tk.Label(self, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack(pady=10)

        self.board_frame = tk.Frame(self)
        self.board_frame.pack()

        self.board_labels = [[tk.Label(self.board_frame, text="", width=5, height=2, font=("Helvetica", 16), borderwidth=2, relief="solid") for _ in range(self.game.board_size)] for _ in range(self.game.board_size)]

        for i in range(self.game.board_size):
            for j in range(self.game.board_size):
                self.board_labels[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.update_board()

    def update_board(self):
        for i in range(self.game.board_size):
            for j in range(self.game.board_size):
                value = self.game.board[i][j]
                text = str(value) if value != 0 else ""
                self.board_labels[i][j].configure(text=text, bg=self.get_tile_color(value))

        self.score_label.configure(text=f"Score: {self.game.score}")

    def handle_key_press(self, event):
        key_mapping = {'Left': 'left', 'Right': 'right', 'Up': 'up', 'Down': 'down'}
        direction = key_mapping.get(event.keysym)
        if direction:
            self.game.move(direction)
            self.update_board()

    def get_tile_color(self, value):
        colors = {0: "lightgray", 2: "lightblue", 4: "lightgreen", 8: "lightyellow", 16: "lightorange", 32: "lightred",
                  64: "lightpink", 128: "lightcyan", 256: "lightmagenta", 512: "lightbrown", 1024: "lightpurple", 2048: "lightgold"}
        return colors.get(value, "white")


if __name__ == "__main__":
    game = Game2048()
    gui = Game2048GUI(game)
    gui.mainloop()
