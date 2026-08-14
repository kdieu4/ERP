class Employee:
    def __init__(self, code: str, name: str, salary: float, days: int):
        self.code = code
        self.name = name
        self.salary = salary
        self.days = days
        
    def salary_value(self):
        return self.salary * self.days    