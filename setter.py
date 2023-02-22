

class Employee():
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname

    def print_details(self):
        return f"The name of the employee is {self.fname} {self.lname}."
    
    @property
    def email(self):
        return f"Email of the employee is {self.fname}.{self.lname}@gmail.com" 
    
    @email.setter
    def email(self, new_email):
        fullName = new_email.split("@")[0]
        self.fname = fullName.split(".")[0]
        self.lname = fullName.split(".")[1]
        
        # return f"Now new details are ---->The name of employee is {self.fname} {self.lname}"

jay = Employee("Jay", "Barmeda")
# jay.fname = "Shivam"
print(jay.email) 

jay.email = "Something.new@gmail.com"
print(jay.email) 
