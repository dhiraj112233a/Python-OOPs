# A. __init__() - Constructor

# 1. Student class
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Rahul", 20, "BBA CA")
student1.display()


# 2. Employee class
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


employee1 = Employee("Amit", 35000, "IT")
employee1.display()


# 3. Book class - Create 3 objects
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book1 = Book("Python Basics", "John", 500)
book2 = Book("Java Programming", "James", 600)
book3 = Book("Web Development", "David", 700)

book1.display()
book2.display()
book3.display()


# 4. BankAccount class
class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def display(self):
        print("Account No:", self.account_no)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)


account1 = BankAccount(101, "Rahul", 50000)
account1.display()


#  __str__() - Readable Object Representation


# 1. Student using __str__()
class StudentStr:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}"


student2 = StudentStr("Amit", 21, "BCA")
print(student2)


# 2. Employee using __str__()
class EmployeeStr:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return (
            f"Employee ID: {self.employee_id}\n"
            f"Name: {self.name}\n"
            f"Salary: {self.salary}"
        )


employee2 = EmployeeStr(101, "Rahul", 35000)
print(employee2)


# 3. Hospital using __str__()
class Hospital:
    def __init__(self, patient_id, patient_name, disease):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.disease = disease

    def __str__(self):
        return (
            f"Patient ID: {self.patient_id}\n"
            f"Patient Name: {self.patient_name}\n"
            f"Disease: {self.disease}"
        )


patient1 = Hospital(501, "Amit", "Fever")
print(patient1)


#  @classmethod

# 1. Student - change school name
class StudentSchool:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


print(StudentSchool.school_name)

StudentSchool.change_school_name("XYZ School")

print(StudentSchool.school_name)


# 2. Employee - change company name
class EmployeeCompany:
    company_name = "ABC Company"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


print(EmployeeCompany.company_name)

EmployeeCompany.change_company_name("Google")

print(EmployeeCompany.company_name)


# 3. Bank - change bank name
class Bank:
    bank_name = "SBI"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


print(Bank.bank_name)

Bank.change_bank_name("HDFC Bank")

print(Bank.bank_name)


# 4. Company - update location
class Company:
    company_name = "TCS"
    location = "Pune"

    @classmethod
    def change_location(cls, new_location):
        cls.location = new_location


print(Company.company_name)
print(Company.location)

Company.change_location("Mumbai")

print(Company.location)


# @staticmethod

# 1. Calculator - addition, subtraction, multiplication, division
class Calculator:

    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b


print("Addition:", Calculator.addition(10, 5))
print("Subtraction:", Calculator.subtraction(10, 5))
print("Multiplication:", Calculator.multiplication(10, 5))
print("Division:", Calculator.division(10, 5))


# 2. MathUtility - even or odd
class MathUtility:

    @staticmethod
    def even_odd(number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"


print(MathUtility.even_odd(10))
print(MathUtility.even_odd(7))


# 3. Validator - email contains @
class Validator:

    @staticmethod
    def validate_email(email):
        if "@" in email:
            return "Valid Email"
        else:
            return "Invalid Email"


print(Validator.validate_email("abc@gmail.com"))
print(Validator.validate_email("abcgmail.com"))


# 4. PasswordValidator
class PasswordValidator:

    @staticmethod
    def validate_password(password):
        if len(password) >= 8:
            return "Valid Password"
        else:
            return "Password must have at least 8 characters"


print(PasswordValidator.validate_password("password123"))
print(PasswordValidator.validate_password("abc"))


# 5. Calculator - square and cube
class Calculator2:

    @staticmethod
    def square(number):
        return number * number

    @staticmethod
    def cube(number):
        return number * number * number


print("Square:", Calculator2.square(5))
print("Cube:", Calculator2.cube(5))


# 6. AgeValidator
class AgeValidator:

    @staticmethod
    def check_vote(age):
        if age >= 18:
            return "Eligible to vote"
        else:
            return "Not eligible to vote"


print(AgeValidator.check_vote(20))
print(AgeValidator.check_vote(15))


# 7. NumberUtility - factorial and sum of digits
class NumberUtility:

    @staticmethod
    def factorial(number):
        result = 1

        for i in range(1, number + 1):
            result = result * i

        return result

    @staticmethod
    def sum_digits(number):
        total = 0

        while number > 0:
            digit = number % 10
            total = total + digit
            number = number // 10

        return total


print("Factorial:", NumberUtility.factorial(5))
print("Sum of digits:", NumberUtility.sum_digits(1234))


# 8. StringUtility
class StringUtility:

    @staticmethod
    def reverse_string(text):
        return text[::-1]

    @staticmethod
    def palindrome(text):
        if text == text[::-1]:
            return "Palindrome"
        else:
            return "Not Palindrome"


print("Reverse:", StringUtility.reverse_string("Python"))
print(StringUtility.palindrome("madam"))
print(StringUtility.palindrome("hello"))


#@property

# 1. Student - private _name
class StudentName:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


student3 = StudentName("Rahul")
print("Student Name:", student3.name)


# 2. Person - private _age
class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age


person1 = Person(25)
print("Age:", person1.age)


# 3. Employee - private _salary
class EmployeeSalary:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary


employee3 = EmployeeSalary(40000)
print("Salary:", employee3.salary)


# 4. Mobile - private _brand
class Mobile:

    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):
        return self._brand


mobile1 = Mobile("Samsung")
print("Brand:", mobile1.brand)


# 5. Laptop - private _ram
class Laptop:

    def __init__(self, ram):
        self._ram = ram

    @property
    def ram(self):
        return self._ram


laptop1 = Laptop("16 GB")
print("RAM:", laptop1.ram)


# 6. Rectangle - length and width properties
class Rectangle:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width


rectangle1 = Rectangle(10, 5)

print("Length:", rectangle1.length)
print("Width:", rectangle1.width)


# 7. Student - marks getter and setter
class StudentMarks:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks):
        self._marks = new_marks


student4 = StudentMarks(80)

print("Old Marks:", student4.marks)

student4.marks = 90

print("New Marks:", student4.marks)


# 8. Student - percentage between 0 and 100
class StudentPercentage:

    def __init__(self, percentage):
        self._percentage = percentage

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        if 0 <= value <= 100:
            self._percentage = value
        else:
            print("Percentage must be between 0 and 100")


student5 = StudentPercentage(80)

print("Percentage:", student5.percentage)

student5.percentage = 95

print("New Percentage:", student5.percentage)

student5.percentage = 150


# 9. Book - pages greater than 0
class BookPages:

    def __init__(self, pages):
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value > 0:
            self._pages = value
        else:
            print("Pages must be greater than 0")


book4 = BookPages(200)

print("Pages:", book4.pages)

book4.pages = 300

print("New Pages:", book4.pages)


# 10. Employee - prevent negative experience
class EmployeeExperience:

    def __init__(self, experience):
        self._experience = experience

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value >= 0:
            self._experience = value
        else:
            print("Experience cannot be negative")


employee4 = EmployeeExperience(2)

print("Experience:", employee4.experience)

employee4.experience = 5

print("New Experience:", employee4.experience)

employee4.experience = -2


# 11. Rectangle - area property
class RectangleArea:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


rectangle2 = RectangleArea(10, 5)

print("Area:", rectangle2.area)


# 12. Employee - annual salary property
class EmployeeAnnualSalary:

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    @property
    def annual_salary(self):
        return self.monthly_salary * 12


employee5 = EmployeeAnnualSalary(30000)

print("Monthly Salary:", employee5.monthly_salary)
print("Annual Salary:", employee5.annual_salary)


# 13. Student - total of 5 subjects
class StudentTotal:

    def __init__(self, m1, m2, m3, m4, m5):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    @property
    def total(self):
        return self.m1 + self.m2 + self.m3 + self.m4 + self.m5


student6 = StudentTotal(80, 75, 90, 85, 70)

print("Total Marks:", student6.total)


# 14. Student - percentage property
class StudentPercentage2:

    def __init__(self, total_marks):
        self.total_marks = total_marks

    @property
    def percentage(self):
        return self.total_marks / 500 * 100


student7 = StudentPercentage2(400)

print("Percentage:", student7.percentage)


# 15. Product - total price
class Product:

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    @property
    def total_price(self):
        return self.price * self.quantity


product1 = Product(100, 5)

print("Total Price:", product1.total_price)


# 16. BankAccount - balance after fixed interest
class BankAccountInterest:

    def __init__(self, balance):
        self.balance = balance

    @property
    def balance_with_interest(self):
        interest_rate = 5

        interest = self.balance * interest_rate / 100

        return self.balance + interest


account2 = BankAccountInterest(10000)

print("Original Balance:", account2.balance)
print("Balance after Interest:", account2.balance_with_interest)


# 17. Car - mileage property
class Car:

    def __init__(self, distance, fuel_used):
        self.distance = distance
        self.fuel_used = fuel_used

    @property
    def mileage(self):
        return self.distance / self.fuel_used


car1 = Car(500, 25)

print("Mileage:", car1.mileage, "km/l")