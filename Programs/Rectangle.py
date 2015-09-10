from Shape import Shape

class Rectangle(Shape):

    sides = 4
    
    def __init__(self, length, width):
        super().__init__('Rectangle')
        self.length = length
        self.width = width

    #The getters
    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    #The setters
    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError('Error: Length must be positive.')
        self._length = value

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Error: Width must be positive.')
        self._width = value


    
    def getArea(self):
        return self.length * self.width
