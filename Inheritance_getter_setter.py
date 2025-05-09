class Person:
    def set_name(self, value):
        self._name = value

    def get_name(self):
        return self._name

    def set_address(self, value):
        self._address = value

    def get_address(self):
        return self._address


class Student(Person):
    def set_roll(self, value):
        self._roll = value

    def get_roll(self):
        return self._roll


class Cname(Student):
    def set_cname(self, value):
        self._cname = value

    def get_cname(self):
        return self._cname


class Employee(Person):
    def set_salary(self, value):
        self._salary = value

    def get_salary(self):
        return self._salary
# Person
p1 = Person()
p1.set_name("Gehendra")
p1.set_address("Dang")
print(f"The name is {p1.get_name()} and address is {p1.get_address()}")

# Student
s1 = Student()
s1.set_name("Gehendra")
s1.set_address("Lamahi")
s1.set_roll("20")
print(f"The name is {s1.get_name()}, address is {s1.get_address()}, and roll is {s1.get_roll()}")

# Cname
c1 = Cname()
c1.set_name("Gehendra")
c1.set_address("Ghorahi")
c1.set_roll("25")
c1.set_cname("BCA")
print(f"The name is {c1.get_name()}, address is {c1.get_address()}, roll is {c1.get_roll()}, and class name is {c1.get_cname()}")

# Employee
e1 = Employee()
e1.set_name("Ram")
e1.set_address("Kathmandu")
e1.set_salary(45000)
print(f"The name is {e1.get_name()}, address is {e1.get_address()}, and salary is {e1.get_salary()}")
