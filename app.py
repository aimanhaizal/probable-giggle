class Crossword:
    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.clues = []

    def add_word(self, start, direction, word, hint):
        x, y = start
        word_length = len(word)

        if direction == 'across':
            if y + word_length > self.size:
                print(f"Word '{word}' does not fit horizontally.")
                return False
            for i in range(word_length):
                if self.grid[x][y + i] not in ['.', word[i]]:
                    print(f"Cannot place '{word}' at {start} going {direction}. Conflict at {(x, y+i)}.")
                    return False
            for i in range(word_length):
                self.grid[x][y + i] = word[i]
            # Change clue format to (A1 to A4)
            self.clues.append(f'({chr(x + 65)}{y + 1} to {chr(x + 65)}{y + word_length}) - {hint}')
            return True

        elif direction == 'down':
            if x + word_length > self.size:
                print(f"Word '{word}' does not fit vertically.")
                return False
            for i in range(word_length):
                if self.grid[x + i][y] not in ['.', word[i]]:
                    print(f"Cannot place '{word}' at {start} going {direction}. Conflict at {(x+i, y)}.")
                    return False
            for i in range(word_length):
                self.grid[x + i][y] = word[i]
            # Change clue format to (A2 to C2)
            self.clues.append(f'({chr(x + 65)}{y + 1} to {chr(x + word_length + 65 - 1)}{y + 1}) - {hint}')
            return True

        return False

    def display(self):
        # Display column numbers with extra spaces for alignment
        print('    ' + ' '.join(str(i + 1) for i in range(self.size)))  # Adjusted spaces here
        
        for idx, row in enumerate(self.grid):
            # Display row letter (A, B, C...)
            print(chr(idx + 65) + ' | ' + ' '.join(row))
        
        print("\nClues:")
        for clue in self.clues:
            print(clue)

# Initialize the crossword
crossword_size = 5  # You can set the desired size
crossword = Crossword(crossword_size)

# Add words with placements and hints
crossword.add_word((0, 0), 'across', 'MOON', 'celestial body which revolves around Earth')
crossword.add_word((0, 1), 'down', 'OAK', 'hardwood tree')

# Display the crossword
crossword.display()
