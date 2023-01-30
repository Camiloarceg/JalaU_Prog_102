#!/usr/bin/env python3

class Singleton:
    #class variable to keep track of the only object.
    __instance = None

    # method to create instances if does not exist else returns existing instance
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

obj1 = Singleton()
print(obj1)
obj2 = Singleton()
print(obj2)
obj1.x = 5
print(obj2.x)
if id(obj1) == id(obj2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")
