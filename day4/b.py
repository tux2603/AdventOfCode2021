# class to keep track of a bingo baord
class Board:
    def __init__(self, lines):
        self.board = [[int(j) for j in i.split()] for i in lines]
        self.squares_played = [[False for i in range(5)] for j in range(5)]
        self.has_bingod = False

    def call_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.squares_played[i][j] = True

    def has_bingo(self):
        return any(all(self.squares_played[i]) for i in range(5)) or any(all(self.squares_played[j][i] for j in range(5)) for i in range(5))

    def get_unplayed_numbers(self):
        nums = []
        for i in range(5):
            for j in range(5):
                if not self.squares_played[i][j]:
                    nums.append(self.board[i][j])
        return nums

    def __str__(self):
        board_string = ''
        for i in range(5):
            for j in range(5):
                board_string += f'{self.board[i][j]:2} ' if not self.squares_played[i][j] else '** '
            board_string += '\n'

        return board_string

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

        numbers = [int(i) for i in lines[0].split(',')]

        # boards are one for every six lines, with the first line being blank and should be discarded
        boards = [Board(lines[i+1:i+6]) for i in range(1, len(lines), 6)]

    num_boards = len(boards)
    num_bingos = 0

    for i in numbers:
        # print(f'\n\nCalling {i}!')
        for j in boards:
            j.call_number(i)
            # print(j)
            # print('---')

            if j.has_bingo():
                if not j.has_bingod:
                    num_bingos += 1
                    j.has_bingod = True                

                if num_bingos == num_boards:
                    solution = sum(j.get_unplayed_numbers()) * i
                    print(solution)
                    exit()
