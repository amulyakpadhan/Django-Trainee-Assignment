class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

if __name__=='__main__':
    rect = Rectangle(20, 10)

    for i in rect:
        print(i)