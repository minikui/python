#coding: UTF-8

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, number):
        self.number = number

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is-a Person has-a name hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    def __init__(self, location, number):
        self.Location = location
        self.number = number

## Salmon is-a Fish
class Salmon(Fish):
    def __init__(self, color, number):
        self.color = color
        self.number = number

## Halibut is-a Fish
class Halibut(Fish):
    def __init__(self, color, number):
        self.color = color
        self.number = number


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet dog
mary.pet = satan

## frank is-a Employee has-a salary
frank = Employee("Frank", 120000)

## frank has-a pet dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
