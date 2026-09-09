# ============================================================
# INSTANCE VARIABLES
# ============================================================

# 1. Student
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


s1 = Student("Dhiraj", 21, 85)
s1.display()


# 2. Employee
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


e1 = Employee("Rahul", 30000, "IT")
e1.display()


# 3. Car - Two objects
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


car1 = Car("Toyota", "Fortuner", 4000000)
car2 = Car("BMW", "X5", 8000000)

car1.display()
car2.display()


# 4. Book
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book = Book("Python Programming", "John", 500)
book.display()


# 5. Mobile
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


mobile = Mobile("Apple", "iPhone 13", 50000)
mobile.display()


# 6. Product
class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


product = Product("Laptop", 60000, 2)
product.display()


# 7. Person - Three objects
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)


person1 = Person("Dhiraj", 21, "Pune")
person2 = Person("Rahul", 22, "Mumbai")
person3 = Person("Amit", 23, "Nashik")

person1.display()
person2.display()
person3.display()


# 8. Laptop
class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)


laptop = Laptop("Dell", "16GB", "512GB", 60000)
laptop.display()


# 9. Movie
class Movie:
    def __init__(self, name, actor, actress, rating):
        self.name = name
        self.actor = actor
        self.actress = actress
        self.rating = rating

    def display(self):
        print("Movie:", self.name)
        print("Actor:", self.actor)
        print("Actress:", self.actress)
        print("Rating:", self.rating)


movie = Movie("3 Idiots", "Aamir Khan", "Kareena Kapoor", 9)
movie.display()


# 10. BankAccount
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


account = BankAccount("Dhiraj", 12345, 25000)
account.display()


# 11. Teacher - Two objects
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Salary:", self.salary)


teacher1 = Teacher("Amit", "Python", 40000)
teacher2 = Teacher("Priya", "Java", 45000)

teacher1.display()
teacher2.display()


# 12. CollegeStudent
class CollegeStudent:
    def __init__(self, name, roll_no, course, year):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.year = year

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Year:", self.year)


student = CollegeStudent("Dhiraj", 101, "BBA CA", 3)
student.display()


# 13. HospitalPatient
class HospitalPatient:
    def __init__(self, name, age, disease, room_no):
        self.name = name
        self.age = age
        self.disease = disease
        self.room_no = room_no

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Room No:", self.room_no)


patient = HospitalPatient("Rahul", 30, "Fever", 205)
patient.display()


# 14. Five Laptop objects
class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print(self.brand, self.ram, self.storage, self.price)


laptop1 = Laptop("Dell", "8GB", "512GB", 50000)
laptop2 = Laptop("HP", "16GB", "512GB", 60000)
laptop3 = Laptop("Lenovo", "8GB", "256GB", 45000)
laptop4 = Laptop("Asus", "16GB", "1TB", 70000)
laptop5 = Laptop("Acer", "8GB", "512GB", 48000)

laptop1.display()
laptop2.display()
laptop3.display()
laptop4.display()
laptop5.display()


# 15. Bike
class Bike:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Price:", self.price)


bike = Bike("Honda", "Shine", "Black", 90000)
bike.display()


# 16. Company
class Company:
    def __init__(self, company_name, location, employees):
        self.company_name = company_name
        self.location = location
        self.employees = employees

    def display(self):
        print("Company:", self.company_name)
        print("Location:", self.location)
        print("Employees:", self.employees)


company = Company("TCS", "Pune", 5000)
company.display()


# 17. Course
class Course:
    def __init__(self, course_name, duration, fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

    def display(self):
        print("Course:", self.course_name)
        print("Duration:", self.duration)
        print("Fees:", self.fees)


course = Course("Python", "6 Months", 20000)
course.display()


# 18. Restaurant
class Restaurant:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating

    def display(self):
        print("Name:", self.name)
        print("Location:", self.location)
        print("Rating:", self.rating)


restaurant = Restaurant("Food Palace", "Pune", 4.5)
restaurant.display()


# 19. Flight
class Flight:
    def __init__(self, flight_no, source, destination, price):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.price = price

    def display(self):
        print("Flight No:", self.flight_no)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Price:", self.price)


flight = Flight("AI101", "Pune", "Delhi", 5000)
flight.display()


# 20. Hotel
class Hotel:
    def __init__(self, name, location, room_type, price):
        self.name = name
        self.location = location
        self.room_type = room_type
        self.price = price

    def display(self):
        print("Hotel:", self.name)
        print("Location:", self.location)
        print("Room Type:", self.room_type)
        print("Price:", self.price)


hotel = Hotel("Taj Hotel", "Mumbai", "Deluxe", 8000)
hotel.display()


# ============================================================
# INSTANCE METHODS
# ============================================================

# 21. Student display() method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s = Student("Dhiraj", 21)
s.display()


# 22. Employee display_salary()
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def display_salary(self):
        print("Salary:", self.salary)


e = Employee(30000)
e.display_salary()


# 23. Car start()
class Car:
    def start(self):
        print("Car Started")


car = Car()
car.start()


# 24. Mobile call()
class Mobile:
    def call(self):
        print("Calling someone...")


mobile = Mobile()
mobile.call()


# 25. Person greet()
class Person:
    def greet(self):
        print("Hello, Welcome!")


person = Person()
person.greet()


# 26. BankAccount display_balance()
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print("Balance:", self.balance)


account = BankAccount(20000)
account.display_balance()


# 27. Book display_book()
class Book:
    def __init__(self, title):
        self.title = title

    def display_book(self):
        print("Book:", self.title)


book = Book("Python Programming")
book.display_book()


# 28. Product display_product()
class Product:
    def __init__(self, product_name):
        self.product_name = product_name

    def display_product(self):
        print("Product:", self.product_name)


product = Product("Laptop")
product.display_product()


# ============================================================
# SELF KEYWORD PRACTICE
# ============================================================

# 29. Student - self.name and self.marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student = Student("Dhiraj", 90)
student.display()


# 30. Employee - self.salary
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def display(self):
        print("Employee Salary:", self.salary)


employee = Employee(35000)
employee.display()


# 31. Car - self.brand and self.model
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car = Car("BMW", "X5")
car.display()


# 32. Product - self.price
class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_price(self):
        print("Total Price:", self.price * self.quantity)


product = Product(100, 5)
product.total_price()


# 33. Student - Hello + name
class Student:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello", self.name)


student = Student("Dhiraj")
student.hello()


# 34. BankAccount - self.balance
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print("Current Balance:", self.balance)


account = BankAccount(15000)
account.display()


# 35. Book - self.title and self.author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)


book = Book("Python", "John")
book.display()


# 36. Mobile - self.price
class Mobile:
    def __init__(self, price):
        self.price = price

    def display(self):
        print("Mobile Price:", self.price)


mobile = Mobile(50000)
mobile.display()


# ============================================================
# MULTIPLE METHODS IN ONE CLASS
# ============================================================

# 37. Calculator
class Calculator:

    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

    def divide(self, a, b):
        print("Division:", a / b)


calculator = Calculator()

calculator.add(10, 5)
calculator.subtract(10, 5)
calculator.multiply(10, 5)
calculator.divide(10, 5)


# 38. Student - display, total, percentage
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        print("Name:", self.name)

    def calculate_total(self):
        return self.m1 + self.m2 + self.m3

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / 3


student = Student("Dhiraj", 80, 85, 90)

student.display()
print("Total:", student.calculate_total())
print("Percentage:", student.calculate_percentage())


# 39. Employee - display, annual salary, bonus
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def display(self):
        print("Name:", self.name)
        print("Monthly Salary:", self.monthly_salary)

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def calculate_bonus(self):
        return self.monthly_salary * 0.10


employee = Employee("Rahul", 30000)

employee.display()
print("Annual Salary:", employee.calculate_annual_salary())
print("Bonus:", employee.calculate_bonus())


# 40. BankAccount - deposit, withdraw, balance
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)

    def display_balance(self):
        print("Balance:", self.balance)


account = BankAccount(10000)

account.deposit(5000)
account.withdraw(2000)
account.display_balance()


# 41. Rectangle - area, perimeter, display
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


rectangle = Rectangle(10, 5)
rectangle.display()


# 42. Circle - area, circumference, display
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Circumference:", self.circumference())


circle = Circle(7)
circle.display()


# 43. Product - display, total, discount
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self, discount):
        total = self.calculate_total()
        discount_amount = total * discount / 100
        return total - discount_amount


product = Product("Laptop", 50000, 2)

product.display()
print("Total:", product.calculate_total())
print("Final Price:", product.apply_discount(10))