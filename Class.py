class phone:
    def __init__(self, model, is_touch, size, price):
        self.model = model
        self.is_touch = is_touch
        self.size = size
        self.price = price

    def is_touchtable(self):
        if self.is_touch:
            return True
        else:
            return False

class Tablet(phone):
    def __init__(self, model, is_touch, size, price, color):
        self.model = model
        self.is_touch = is_touch
        self.size = size
        self.price = price
        self.color = color