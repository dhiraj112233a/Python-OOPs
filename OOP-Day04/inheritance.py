#1.Hierarchical Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

ani= Animal()
dog = Dog()
cat = Cat()

dog.eat()  
dog.bark()  
cat.eat()


#2.Single Inheritance
class Parent:
    def greet(self):
        print("Hello I am Parent")

class Child(Parent):
    def greet(self):
        print("Hello I am Child")

parent = Parent()
child = Child()

parent.greet()
child.greet()

#3.Multiple Inheritance
class Captain:
    def skills(self):
        print("I am a Captain (Rohit Sharma)")

class ViceCaptain:
    def skills(self):
        print("I am a ViceCaptain (Virat Kohli)")

class Player(Captain, ViceCaptain):
    def skills(self):
        Captain.skills(self)
        ViceCaptain.skills(self)
        print("I am a Player")

player = Player()
player.skills()


#4. Multilevel Inheritance
class Car:
    def start(self):
        print("Car is starting")

class SportsCar(Car):
    def accelerate(self):
        print("SportsCar is accelerating")

class BMW(SportsCar):
    def turbo(self):
        print("BMW is using turbo")

bmw = BMW()
bmw.start()
bmw.accelerate()
bmw.turbo()


#5. Hybrid Inheritance
class Player:

    def play(self):
        print("Player is playing cricket")


class Batsman(Player):

    def batting(self):
        print("Batsman is batting")


class Bowler(Player):

    def bowling(self):
        print("Bowler is bowling")


class AllRounder(Batsman, Bowler):

    def fielding(self):
        print("All-rounder is fielding")


player = AllRounder()

player.play()
player.batting()
player.bowling()
player.fielding()