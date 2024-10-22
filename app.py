class Crossword:
    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.clues = []

    def add_word(self, start, direction, word, hint):
        x, y = start
        word_length = len(word)

        if direction == 'across':
            # Check if word fits and does not overlap incorrectly
            if y + word_length > self.size:
                print(f"Word '{word}' does not fit horizontally.")
                return False
            for i in range(word_length):
                if self.grid[x][y + i] not in ['.', word[i]]:
                    print(f"Cannot place '{word}' at {start} going {direction}. Conflict at {(x, y+i)}.")
                    return False
            for i in range(word_length):
                self.grid[x][y + i] = word[i]
            self.clues.append(f'({start[0]+1}, {start[1]+1} to {start[0]+1}, {start[1]+word_length}) - {hint}')
            return True

        elif direction == 'down':
            # Check if word fits and does not overlap incorrectly
            if x + word_length > self.size:
                print(f"Word '{word}' does not fit vertically.")
                return False
            for i in range(word_length):
                if self.grid[x + i][y] not in ['.', word[i]]:
                    print(f"Cannot place '{word}' at {start} going {direction}. Conflict at {(x+i, y)}.")
                    return False
            for i in range(word_length):
                self.grid[x + i][y] = word[i]
            self.clues.append(f'({start[0]+1}, {start[1]+1} to {start[0]+word_length}, {start[1]+1}) - {hint}')
            return True

        return False

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print("\nClues:")
        for clue in self.clues:
            print(clue)

# Initialize the crossword
crossword_size = 5  # You can set the desired size
crossword = Crossword(crossword_size)

# Add words with placements and hints
crossword.add_word((0, 0), 'across', 'MOON', 'celestial body which revolves around Earth')
crossword.add_word((0, 1), 'down', 'OAK', 'hardwood tree')
crossword.add_word((0, 3), 'down', 'NEST', 'place where birds sleep')

# Display the crossword
crossword.display()
