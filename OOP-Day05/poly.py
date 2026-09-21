#1
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks       # Private variable

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        self.__marks = marks


student1 = Student("Virat", 90)

print("\nStudent Name:", student1.name)
print("Student Marks:", student1.get_marks())

student1.set_marks(95)

print("Updated Marks:", student1.get_marks())



# 2.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print("\nInitial Balance:", account.get_balance())

account.deposit(2000)
account.withdraw(1000)

print("Final Balance:", account.get_balance())

# 3.


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


employee1 = Employee("Rahul", 30000)

print("\nEmployee:", employee1.name)
print("Salary:", employee1.get_salary())

employee1.set_salary(40000)

print("Updated Salary:", employee1.get_salary())


# 4. 

class Person:

    def show_person(self):
        print("This is a Person")


class StudentInheritance(Person):

    def study(self):
        print("Student is studying")


student2 = StudentInheritance()

print("\nPerson -> Student")

student2.show_person()
student2.study()

# 5. 

class Vehicle:

    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


car = Car()

print("\nVehicle -> Car")

car.start()
car.drive()

# 6. 
class EmployeeParent:

    def work(self):
        print("Employee is working")


class Developer(EmployeeParent):

    def coding(self):
        print("Developer is coding")


developer = Developer()

print("\nEmployee -> Developer")

developer.work()
developer.coding()

# 7. 

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


class Puppy(Dog):

    def play(self):
        print("Puppy is playing")


puppy = Puppy()

print("\nAnimal -> Dog -> Puppy")

puppy.eat()
puppy.bark()
puppy.play()


7.
class Cricketer:

    def practice(self):
        print("Cricketer is practicing")


class Batsman(Cricketer):

    def batting(self):
        print("Batsman is batting")


class Opener(Batsman):

    def opening(self):
        print("Opener is opening the innings")


player = Opener()

print("\nCricket Multilevel Inheritance")

player.practice()
player.batting()
player.opening()


#8
class Father:

    def father_property(self):
        print("Father's property")


class Mother:

    def mother_property(self):
        print("Mother's property")


class Child(Father, Mother):

    def child_property(self):
        print("Child's property")


child = Child()

print("\nFather + Mother -> Child")

child.father_property()
child.mother_property()
child.child_property()



#9
class DogSound:

    def sound(self):
        print("Dog says Bow Bow")


class Cat:

    def sound(self):
        print("Cat says Meow")


class Cow:

    def sound(self):
        print("Cow says Moo")


print("\nDog, Cat and Cow")

dog = DogSound()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()


#10
class Shape:

    def area(self):
        print("Shape area")


class Circle(Shape):

    def area(self):
        radius = 5
        result = 3.14 * radius * radius
        print("Circle Area:", result)


class Rectangle(Shape):

    def area(self):
        length = 10
        width = 5
        result = length * width
        print("Rectangle Area:", result)


print("\nShape Polymorphism")

circle = Circle()
rectangle = Rectangle()

circle.area()
rectangle.area()


#11
class Payment:

    def pay(self):
        print("Payment method")


class UPI(Payment):

    def pay(self):
        print("Payment done using UPI")


class CardPayment(Payment):

    def pay(self):
        print("Payment done using Card")


print("\nPayment Polymorphism")

upi = UPI()
card = CardPayment()

upi.pay()
card.pay()

#12  

class EmployeeSalary:

    def calculate_salary(self):
        print("Employee salary")


class DeveloperSalary(EmployeeSalary):

    def calculate_salary(self):
        print("Developer Salary: 50000")


class ManagerSalary(EmployeeSalary):

    def calculate_salary(self):
        print("Manager Salary: 70000")


class TesterSalary(EmployeeSalary):

    def calculate_salary(self):
        print("Tester Salary: 40000")


print("\nEmployee Salary Polymorphism")

employees = [
    DeveloperSalary(),
    ManagerSalary(),
    TesterSalary()
]

for employee in employees:
    employee.calculate_salary()


#13

class AbstractVehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Bike(AbstractVehicle):

    def start(self):
        print("Bike starts with a button")


class Bus(AbstractVehicle):

    def start(self):
        print("Bus starts with a key")


print("\nAbstract Vehicle")

bike = Bike()
bus = Bus()

bike.start()
bus.start()


# ------------------------------------------------------------
# 14. Abstract Shape with area()
# ------------------------------------------------------------

class AbstractShape(ABC):

    @abstractmethod
    def area(self):
        pass


class AbstractCircle(AbstractShape):

    def area(self):
        radius = 5
        result = 3.14 * radius * radius
        print("Circle Area:", result)


class AbstractRectangle(AbstractShape):

    def area(self):
        length = 10
        width = 5
        result = length * width
        print("Rectangle Area:", result)


print("\nAbstract Shape")

circle2 = AbstractCircle()
rectangle2 = AbstractRectangle()

circle2.area()
rectangle2.area()


# ------------------------------------------------------------
# 15. Abstract Payment with pay()
# ------------------------------------------------------------

class AbstractPayment(ABC):

    @abstractmethod
    def pay(self):
        pass


class GooglePay(AbstractPayment):

    def pay(self):
        print("Payment using Google Pay")


class Card(AbstractPayment):

    def pay(self):
        print("Payment using Card")


print("\nAbstract Payment")

google_pay = GooglePay()
card_payment = Card()

google_pay.pay()
card_payment.pay()


# ------------------------------------------------------------
# 16. Abstract Employee with calculate_salary()
# ------------------------------------------------------------

class AbstractEmployee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(AbstractEmployee):

    def calculate_salary(self):
        print("Full Time Salary: 50000")


class PartTimeEmployee(AbstractEmployee):

    def calculate_salary(self):
        print("Part Time Salary: 25000")


print("\nAbstract Employee")

full_time = FullTimeEmployee()
part_time = PartTimeEmployee()

full_time.calculate_salary()
part_time.calculate_salary()


# ------------------------------------------------------------
# 17. Abstract BankAccount with withdraw()
# ------------------------------------------------------------

class AbstractBankAccount(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(AbstractBankAccount):

    def withdraw(self, amount):
        print("Withdraw", amount, "from Savings Account")


class CurrentAccount(AbstractBankAccount):

    def withdraw(self, amount):
        print("Withdraw", amount, "from Current Account")


print("\nAbstract Bank Account")

savings = SavingsAccount()
current = CurrentAccount()

savings.withdraw(2000)
current.withdraw(3000)


# ============================================================
# 5. COMBINED OOP
# ============================================================

print("\n========== COMBINED OOP ==========")


# ============================================================
# 18. STUDENT MANAGEMENT SYSTEM
# Uses:
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction
# ============================================================

print("\n----- STUDENT MANAGEMENT SYSTEM -----")


class StudentBase(ABC):

    @abstractmethod
    def display(self):
        pass


class StudentManagement(StudentBase):

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks       # Encapsulation

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print("Student:", self.name)
        print("Marks:", self.__marks)


class CricketStudent(StudentManagement):

    def display(self):
        print("Cricket Student:", self.name)
        print("Marks:", self.get_marks())
        print("Student also plays cricket")


student = CricketStudent("Virat", 90)

student.display()

student.set_marks(95)

print("Updated Marks:", student.get_marks())


# ============================================================
# 19. BANK MANAGEMENT SYSTEM
# ============================================================

print("\n----- BANK MANAGEMENT SYSTEM -----")


class BankUser(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsBank(BankUser):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


class SalaryAccount(SavingsBank):

    def account_type(self):
        print("This is a Salary Account")


bank_user = SalaryAccount("Rahul", 10000)

print("Account Holder:", bank_user.name)

bank_user.deposit(5000)
bank_user.withdraw(3000)

print("Balance:", bank_user.get_balance())

bank_user.account_type()


# ============================================================
# 20. EMPLOYEE MANAGEMENT SYSTEM
# ============================================================

print("\n----- EMPLOYEE MANAGEMENT SYSTEM -----")


class EmployeeManagement(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class DeveloperEmployee(EmployeeManagement):

    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary

    def calculate_salary(self):
        return self.__salary


class ManagerEmployee(EmployeeManagement):

    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary

    def calculate_salary(self):
        return self.__salary


developer = DeveloperEmployee("Amit", 50000)
manager = ManagerEmployee("Rohit", 70000)

print("Developer:", developer.name)
print("Salary:", developer.calculate_salary())

print("Manager:", manager.name)
print("Salary:", manager.calculate_salary())


# ============================================================
# 21. VEHICLE MANAGEMENT SYSTEM
# ============================================================

print("\n----- VEHICLE MANAGEMENT SYSTEM -----")


class VehicleManagement(ABC):

    @abstractmethod
    def start(self):
        pass


class CarManagement(VehicleManagement):

    def start(self):
        print("Car starts with a key")


class BikeManagement(VehicleManagement):

    def start(self):
        print("Bike starts with a button")


class BusManagement(VehicleManagement):

    def start(self):
        print("Bus starts with a key")


vehicles = [
    CarManagement(),
    BikeManagement(),
    BusManagement()
]

for vehicle in vehicles:
    vehicle.start()



# 22.


class LibraryItem(ABC):

    @abstractmethod
    def display(self):
        pass


class Book(LibraryItem):

    def __init__(self, title):
        self.__title = title

    def display(self):
        print("Book:", self.__title)

    def get_title(self):
        return self.__title


class Magazine(LibraryItem):

    def __init__(self, title):
        self.__title = title

    def display(self):
        print("Magazine:", self.__title)


book = Book("Python Programming")
magazine = Magazine("Sports Magazine")

book.display()
magazine.display()

print("Book Title:", book.get_title())


