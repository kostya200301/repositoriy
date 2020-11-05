class Balance:
    def __init__(self):
        self.left = 0
        self.rigrh = 0
        if self.left == self.rigrh:
            self.result = "="
        elif self.left > self.rigrh:
            self.result = "L"
        else:
            self.result = "R"

    def add_left(self, value):
        self.left += value

    def add_right(self, value):
        self.rigrh += value
