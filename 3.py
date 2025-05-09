class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value


class Student(Person):
    def __init__(self, name, address, roll):
        super().__init__(name, address)
        self._roll = roll

    @property
    def roll(self):
        return self._roll

    @roll.setter
    def roll(self, value):
        self._roll = value


class Cname(Student):
    def __init__(self, name, address, roll, cname):
        super().__init__(name, address, roll)
        self._cname = cname

    @property
    def cname(self):
        return self._cname

    @cname.setter
    def cname(self, value):
        self._cname = value


class Employee(Person):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value


# Create object of Person
p1 = Person("Gehendra", "Dang")
print(f"The name is {p1.name} and address is {p1.address}")

# Create object of Student
s1 = Student("Gehendra", "Lamahi", "20")
print(f"The name is {s1.name}, address is {s1.address}, and roll is {s1.roll}")

# Create object of Cname
c1 = Cname("Gehendra", "Ghorahi", "25", "BCA")
print(f"The name is {c1.name}, address is {c1.address}, roll is {c1.roll}, and class name is {c1.cname}")

# Create object of Employee
e1 = Employee("Ram", "Kathmandu", 45000)
print(f"The name is {e1.name}, address is {e1.address}, and salary is {e1.salary}")
