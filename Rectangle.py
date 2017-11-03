class Rectangle:
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " height: " + str(self.height) + " width: " + str(self.width)

