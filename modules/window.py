from time import sleep

class Window:
    def __init__(self, x, y):
        self.timeout = 1
        self.x = x - 2
        self.y = y
        self.lines = []
        self.void = " "
        self.buf_column = []
        for column in range(self.y):
            self.buf_column.append(self.void)
        for line in range(self.x):
            self.lines.append(list(self.buf_column))

    def clear(self):
        print("\033[2J\033[1;1H", end="")

    def set(self, x, y, char):
        self.lines[x][y] = char

    def display(self):
        output = ''
        for line in self.lines:
            for char in line:
                output += char
            output += '\n'
        print(output)
        sleep(self.timeout)

    def flush(self):
        for line in range(self.x):
            self.lines[line] = list(self.buf_column)
