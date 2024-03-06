class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = "?"

        self.is_unknown = True
        self.is_black = False
        self.is_letter = False

    def set_black(self):
        self.is_black = True
        self.is_unknown = False
        self.is_letter = False
        self.value = "#"

    def set_letter(self, letter):
        self.is_letter = True
        self.is_black = False
        self.is_unknown = False
        self.value = letter

    def set_unknown(self):
        self.is_unknown = True
        self.is_black = False
        self.is_letter = False
        self.value = "?"



    def add_word(self, grid, direction: str, word: str, location):
        pass

    def __repr__(self):
        if self.is_black:
            return "#"
        elif self.is_letter:
            return str(self.value)
        else:
            return "?"


class OutOfBoundsError(Exception):
    def __init__(self, message="Word Doesn't Fit"):
        self.message = message

