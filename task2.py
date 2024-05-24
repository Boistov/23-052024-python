class Employee:
    def __init__(self, name, department, salary, years_of_experience):
        self.name = name
        self.department = department
        self.salary = salary
        self.years_of_experience = years_of_experience
    def calculate_bonus(self):
        if self.years_of_experience >= 5:
            return 0.1 * self.salary
        else:
            return 0
    def print_employee_info(self):
        print(f"name: {self.name}")
        print(f"department: {self.department}")
        print(f"salary: ${self.salary}")
        print(f"years of experience: {self.years_of_experience} years")

emp = Employee("John Doe", "IT", 60000, 7)
bonus = emp.calculate_bonus()
emp.print_employee_info()
print(f"Bonus: ${bonus}")
