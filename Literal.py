
class Literal:
    def __init__(self,name):
        self.name = name

    def copy(self):
        copy = Literal(self.name)
        return copy