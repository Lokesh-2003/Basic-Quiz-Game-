import random

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

    def update_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))
        print(f"Score: {self.score}")

if __name__ == "__main__":
    game = Game2048()
    game.start_game()

    while not game.game_over:
        direction = input("Enter move direction (up, down, left, right): ").lower()
        if direction in ['up', 'down', 'left', 'right']:
            game.move(direction)
        else:
            print("Invalid direction. Please enter up, down, left, or right.")

    
