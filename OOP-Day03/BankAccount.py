# 1

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

    def display_balance(self):
        print("Current balance:", self.__balance)


account = BankAccount(20000)
account.deposit(5000)
account.withdraw(2000)
account.display_balance()


# 2
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student = Student("Dhiraj", 95)

print("\nStudent Name:", student.get_name())
print("Student Marks:", student.get_marks())

student.set_name("Rohit")
student.set_marks(92)

print("Updated Name:", student.get_name())
print("Updated Marks:", student.get_marks())


# 3=

class EmployeeSalary:
    def __init__(self, salary):
        self.__salary = salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
            print("Salary updated")
        else:
            print("Salary cannot be negative")

    def get_salary(self):
        return self.__salary


emp = EmployeeSalary(30000)

print("\nSalary:", emp.get_salary())

emp.set_salary(40000)
print("New Salary:", emp.get_salary())

emp.set_salary(-5000)


# 4

class Person:
    def __init__(self, age):
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def check_voting(self):
        if self.__age >= 18:
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")


person = Person(20)

print()
person.check_voting()

person.set_age(21)
person.check_voting()


#5
class Product:
    def __init__(self, price):
        self.__price = 0
        self.set_price(price)

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be greater than zero")

    def get_price(self):
        return self.__price


product = Product(500)

print("\nProduct Price:", product.get_price())

product.set_price(-100)
print("Product Price:", product.get_price())


#6

class Mobile:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def set_details(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def display_details(self):
        print("\nMobile Details")
        print("Brand:", self.__brand)
        print("Model:", self.__model)
        print("Price:", self.__price)


mobile = Mobile("Samsung", "S24", 70000)
mobile.display_details()

mobile.set_details("Apple", "iPhone 13", 40000)
mobile.display_details()


#7
class Car:
    def __init__(self, speed):
        self.__speed = speed

    def accelerate(self, value):
        self.__speed += value
        print("Speed after acceleration:", self.__speed)

    def brake(self, value):
        self.__speed -= value

        if self.__speed < 0:
            self.__speed = 0

        print("Speed after braking:", self.__speed)


car = Car(50)

print()
car.accelerate(30)
car.brake(20)
car.brake(100)


# 8
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


rectangle = Rectangle(10, 5)

print("\nRectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())


# 9
class Circle:
    def __init__(self, radius):
        self.__radius = 0
        self.set_radius(radius)

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be greater than zero")

    def area(self):
        return 3.14 * self.__radius * self.__radius


circle = Circle(5)

print("\nCircle Area:", circle.area())

circle.set_radius(-2)


#10

class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def display_account(self):
        print("\nAccount Information")
        print("Account Number:", self.__account_number)
        print("Balance:", self.__balance)


account1 = Account("123456789", 50000)
account1.display_account()


#11

class LibraryBook:
    def __init__(self, title):
        self.__title = title
        self.__issued = False

    def issue_book(self):
        if self.__issued == False:
            self.__issued = True
            print("Book issued")
        else:
            print("Book is already issued")

    def return_book(self):
        if self.__issued == True:
            self.__issued = False
            print("Book returned")
        else:
            print("Book was not issued")

    def display_status(self):
        print("Book:", self.__title)

        if self.__issued == True:
            print("Status: Issued")
        else:
            print("Status: Available")


book = LibraryBook("Python Programming")

book.display_status()
book.issue_book()
book.display_status()
book.return_book()
book.display_status()


#12

class StudentResult:
    def __init__(self, mark1, mark2, mark3):
        self.__mark1 = mark1
        self.__mark2 = mark2
        self.__mark3 = mark3

    def total(self):
        return self.__mark1 + self.__mark2 + self.__mark3

    def percentage(self):
        return self.total() / 3

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"


result = StudentResult(80, 75, 90)

print("\nTotal:", result.total())
print("Percentage:", result.percentage())
print("Grade:", result.grade())


#13

class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def validate_login(self, username, password):
        if username == self.__username and password == self.__password:
            print("Login successful")
        else:
            print("Invalid username or password")


login = Login("admin", "1234")

print()
login.validate_login("admin", "1234")
login.validate_login("admin", "1111")


#14

class User:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Old password is incorrect")


user = User("abc@gmail.com", "12345")

print()
user.change_password("12345", "67890")
user.change_password("11111", "99999")


#15

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def to_fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    def to_kelvin(self):
        return self.__celsius + 273.15


temperature = Temperature(25)

print("\nFahrenheit:", temperature.to_fahrenheit())
print("Kelvin:", temperature.to_kelvin())


# 16

class BankCustomer:
    def __init__(self, name, pin):
        self.__name = name
        self.__pin = pin

    def verify_pin(self, pin):
        if pin == self.__pin:
            print("PIN is correct")
        else:
            print("Wrong PIN")


customer = BankCustomer("Rahul", 1234)

print()
customer.verify_pin(1234)
customer.verify_pin(1111)


#17

class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited")
        else:
            print("Invalid amount")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Wrong PIN")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Amount withdrawn")

    def balance_inquiry(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Wrong PIN")


atm = ATM(10000, 1234)

print()
atm.balance_inquiry(1234)
atm.deposit(5000)
atm.withdraw(2000, 1234)
atm.balance_inquiry(1234)


#18

class EmployeeDetails:
    def __init__(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary

    def annual_salary(self):
        return self.__salary * 12

    def display(self):
        print("\nEmployee Name:", self.__name)
        print("Department:", self.__department)
        print("Monthly Salary:", self.__salary)
        print("Annual Salary:", self.annual_salary())


employee2 = EmployeeDetails("Amit", "IT", 40000)
employee2.display()


#19

class HospitalPatient:
    def __init__(self, name, age, bill):
        self.__name = name
        self.__age = age
        self.__bill = bill

    def add_charges(self, amount):
        self.__bill += amount

    def display_bill(self):
        print("\nPatient Name:", self.__name)
        print("Age:", self.__age)
        print("Total Bill:", self.__bill)


patient = HospitalPatient("Ravi", 35, 5000)

patient.add_charges(2000)
patient.add_charges(1000)

patient.display_bill()



# 20. ShoppingCart


class ShoppingCart:
    def __init__(self):
        self.__items = []
        self.__total = 0

    def add_product(self, name, price):
        self.__items.append(name)
        self.__total += price
        print(name, "added")

    def remove_product(self, name, price):
        if name in self.__items:
            self.__items.remove(name)
            self.__total -= price
            print(name, "removed")
        else:
            print("Product not found")

    def calculate_total(self):
        return self.__total

    def display_cart(self):
        print("\nItems:", self.__items)
        print("Total:", self.__total)


cart = ShoppingCart()

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

cart.display_cart()

cart.remove_product("Mouse", 1000)

cart.display_cart()



# 21. Course

class Course:
    def __init__(self, course_name, fees):
        self.__course_name = course_name
        self.__fees = 0
        self.set_fees(fees)

    def set_fees(self, fees):
        if fees >= 0:
            self.__fees = fees
        else:
            print("Fees cannot be negative")

    def display_course(self):
        print("\nCourse Name:", self.__course_name)
        print("Course Fees:", self.__fees)


course = Course("Python", 10000)
course.display_course()

course.set_fees(-500)


# 22. Vehicle

class Vehicle:
    def __init__(self, fuel):
        self.__fuel = fuel

    def refuel(self, amount):
        if amount > 0:
            self.__fuel += amount
            print("Fuel added")
        else:
            print("Invalid fuel amount")

    def drive(self, fuel_needed):
        if fuel_needed <= self.__fuel:
            self.__fuel -= fuel_needed
            print("Vehicle is driving")
        else:
            print("Not enough fuel")

    def show_fuel(self):
        print("Available fuel:", self.__fuel)


vehicle = Vehicle(50)

print()
vehicle.show_fuel()

vehicle.drive(20)
vehicle.show_fuel()

vehicle.refuel(30)
vehicle.show_fuel()

vehicle.drive(100)


#23

class Wallet:
    def __init__(self, money):
        self.__money = money

    def add_money(self, amount):
        if amount > 0:
            self.__money += amount
            print("Money added")
        else:
            print("Amount must be positive")

    def spend_money(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        elif amount <= self.__money:
            self.__money -= amount
            print("Money spent")
        else:
            print("Not enough money")

    def display_money(self):
        print("Money in wallet:", self.__money)


wallet = Wallet(1000)

print()
wallet.display_money()

wallet.add_money(500)
wallet.spend_money(300)

wallet.display_money()


#24

class Salary:
    def __init__(self, basic_salary):
        self.__basic_salary = basic_salary

    def calculate_hra(self):
        # HRA = 20% of basic salary
        return self.__basic_salary * 20 / 100

    def calculate_da(self):
        # DA = 10% of basic salary
        return self.__basic_salary * 10 / 100

    def calculate_gross(self):
        hra = self.calculate_hra()
        da = self.calculate_da()

        return self.__basic_salary + hra + da

    def display_salary(self):
        print("\nBasic Salary:", self.__basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.calculate_gross())


salary = Salary(30000)
salary.display_salary()


#25

class Result:
    def __init__(self, marks):
        self.__marks = 0
        self.update_marks(marks)

    def update_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            print("Marks updated")
        else:
            print("Marks must be between 0 and 100")

    def display_marks(self):
        print("Marks:", self.__marks)


result = Result(75)

result.display_marks()

result.update_marks(90)
result.display_marks()

result.update_marks(120)


#26

class DoorLock:
    def __init__(self, password):
        self.__password = password
        self.__locked = True

    def lock(self):
        self.__locked = True
        print("Door is locked")

    def unlock(self, password):
        if password == self.__password:
            self.__locked = False
            print("Door is unlocked")
        else:
            print("Wrong password")

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Old password is incorrect")


door = DoorLock("1234")

door.unlock("1234")
door.lock()

door.unlock("1111")

door.change_password("1234", "5678")
door.unlock("5678")



# 27. Contact

class Contact:
    def __init__(self, phone_number):
        self.__phone_number = ""

        if len(phone_number) == 10 and phone_number.isdigit():
            self.__phone_number = phone_number
            print("Phone number stored")
        else:
            print("Phone number must contain exactly 10 digits")

    def display_phone(self):
        if self.__phone_number != "":
            print("Phone Number:", self.__phone_number)


contact = Contact("9876543210")
contact.display_phone()

contact2 = Contact("12345")
contact2.display_phone()


#28

class Movie:
    def __init__(self, rating):
        self.__rating = 0
        self.set_rating(rating)

    def set_rating(self, rating):
        if rating >= 1 and rating <= 5:
            self.__rating = rating
            print("Rating updated")
        else:
            print("Rating must be between 1 and 5")

    def display_rating(self):
        print("Movie Rating:", self.__rating)


movie = Movie(4)

movie.display_rating()

movie.set_rating(5)
movie.display_rating()

movie.set_rating(7)


#29

class Bank:
    def __init__(self, interest_rate):
        self.__interest_rate = interest_rate

    def calculate_simple_interest(self, principal, time):
        simple_interest = (principal * self.__interest_rate * time) / 100
        return simple_interest


bank = Bank(5)

principal = 10000
time = 2

interest = bank.calculate_simple_interest(principal, time)

print("\nPrincipal:", principal)
print("Interest Rate:", 5, "%")
print("Time:", time, "years")
print("Simple Interest:", interest)


# 30

class Inventory:
    def __init__(self, quantity):
        self.__quantity = quantity

    def add_stock(self, quantity):
        if quantity > 0:
            self.__quantity += quantity
            print("Stock added")
        else:
            print("Quantity must be positive")

    def sell(self, quantity):
        if quantity <= 0:
            print("Quantity must be positive")
        elif quantity <= self.__quantity:
            self.__quantity -= quantity
            print("Product sold")
        else:
            print("Not enough stock")

    def display_quantity(self):
        print("Available Quantity:", self.__quantity)


inventory = Inventory(50)

inventory.display_quantity()

inventory.add_stock(20)
inventory.display_quantity()

inventory.sell(30)
inventory.display_quantity()

inventory.sell(100)
