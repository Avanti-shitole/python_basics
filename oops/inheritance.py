class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.sleep()
dog1.bark()