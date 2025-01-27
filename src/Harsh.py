class Harsh:
    __id = 168
    def __init__(self, role: str, salary:int):
        self.role = role
        self.salary = salary

    def printDetails(self)->None:
        print("Harsh id: " + Harsh.__id)
        print("Harsh role: " + self.role)
        print("Harsh Salary is: " + self.salary)