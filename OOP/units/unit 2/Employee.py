class Employee:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email
        self.remaining_leave_days = 5  # set default remaining leave days to 5

    def book_leave_day(self):
        if self.remaining_leave_days > 0:
            self.remaining_leave_days -= 1
            print(f"{self.name} has successfully booked a day of annual leave.")
        else:
            print(f"{self.name} has no remaining leave days.")


class ProtectedEmployee(Employee):
    def __init__(self, name, id, email):
        super().__init__(name, id, email)
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


class UnprotectedEmployee(Employee):
    def __init__(self, name, id, email):
        super().__init__(name, id, email)
        self.salary = 0

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


# create an instance of Employee
employee1 = Employee("John Smith", 1234, "john.smith@email.com")
print(employee1.name)  # output: John Smith
# output: John Smith has successfully booked a day of annual leave.
employee1.book_leave_day()
# output: John Smith has successfully booked a day of annual leave.
employee1.book_leave_day()
# output: John Smith has successfully booked a day of annual leave.
employee1.book_leave_day()
# output: John Smith has successfully booked a day of annual leave.
employee1.book_leave_day()
# output: John Smith has successfully booked a day of annual leave.
employee1.book_leave_day()
employee1.book_leave_day()  # output: John Smith has no remaining leave days.

# create an instance of ProtectedEmployee
employee2 = ProtectedEmployee("Jane Doe", 5678, "jane.doe@email.com")
employee2.set_salary(50000)
print(employee2.get_salary())  # output: 50000
employee2._ProtectedEmployee__salary = 60000  # change salary using name mangling
print(employee2.get_salary())  # output: 60000

# create an instance of UnprotectedEmployee
employee3 = UnprotectedEmployee("Jack Johnson", 9012, "jack.johnson@email.com")
employee3.set_salary(40000)
print(employee3.salary)  # output: 40000
employee3.salary = 45000  # change salary directly
print(employee3.salary)  # output: 45000
