class Button:
    def __init__(self):
        self.click_count = 0

    def click(self):
        self.click_count += 1

    def reset(self):
        self.click_count = 0
