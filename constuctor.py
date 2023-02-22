from os import stat


class Employee:
    leave = 8
    def __init__(self,aname,asalary,ades):
        self.name = aname
        self.salary = asalary
        self.des = ades

    def printDetails(self):
        return f"The Name is {self.name}.\n The salary is {self.salary}.\n And his designation is {self.des}."
    
    @classmethod
    def change_leave(cls,new_leaves):
        cls.leave = new_leaves

    @classmethod
    def get_string(cls,strings):
        return cls(*strings.split("-"))
    
    @staticmethod
    def print_string(string):
        print("This is good " + string)
         
class player:
    games = 4
    def __init__(self,name,game):
        self.playerName = name
        self.playerGame = game

    def print_player(self):
        return f"The Player Name is {self.playerName} and the game of that player is {self.playerGame}."

class Details(Employee, player):
    country = "India"

    def print_country(self):
        print(self.country)
    
jay = Details("jay",75000,"prog"    )

print(jay.printDetails())


        