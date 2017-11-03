import Rectangle

class surface:
    def__init__(self,"image.png",x,y,width,height):
        self.rect = Rectangle.rectangle(x,y,height,width)
        self.image = "image.png"
        
def getRect(self):
    return self.rect

class rectangle:
    def__init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    def__str__(self):
        return "x:",self.x, "y:", self.y, "height:", self.height, "width:", self.width
