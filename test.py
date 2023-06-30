"""
syntax to define and instantiate class
"""
import math


class NewClass:
    static_attribute = "shared"  # called a class object attribute

    # constructor
    def __init__(self, f_name="joseph", l_name="cortez"):
        self.f_name = f_name
        self.l_name = l_name

    def setName(self, new_name):
        self.name = new_name

    def getFullName(self):
        return f"My name is {self.f_name} {self.l_name}"


new_class_instance = NewClass("Dominick")
new_class_instance.static_attribute == NewClass.static_attribute
print(new_class_instance.getFullName())
