class OddEvenSeparator:
    def __init__(self):
        self.even = []
        self.odd = []

    def add_number(self, value):
        if value % 2 == 0:
            self.even.append(value)
        else:
            self.odd.append(value)
