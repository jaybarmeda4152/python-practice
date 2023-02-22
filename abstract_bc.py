from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        return 0

class rectangle():
    type = "Rectangle"
    side = 4
    def __init__(self):
        self.length = 6
        self.width = 6
        
    def area(self):
        return f"The area of {self.type} is {self.length * self.width} and it have {self.side} sides."

rect = rectangle()
print(rect.area())