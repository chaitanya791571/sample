class Employee:
    def __init__(self, salary, increment):
        self._salary = salary
        self._increment = increment

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary cannot be negative.")

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        if value > 0:
            self._increment = value
        else:
            raise ValueError("Increment must be positive.")

    def apply_increment(self):
        self._salary += self._salary * (self._increment / 100)


emp = Employee(50000, 10)
print(f"Initial Salary: {emp.salary}")  

emp.apply_increment()
print(f"Salary after increment: {emp.salary}") 