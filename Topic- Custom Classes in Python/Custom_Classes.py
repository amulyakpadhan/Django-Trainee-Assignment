class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length} # Yield length in the required format
        yield {'width': self.width}  # Yield width in the required format

# Driver Code
if __name__=='__main__':
    # Create a Rectangle instance
    rect = Rectangle(20, 10)

    # Iterate over the Rectangle instance
    for i in rect:
        print(i)
