"""
MODULES
"""
# modules in python are a python file with a .py extension
""" to import a module """
import math


"""
PACKAGES
"""
# are name-spaces which contain multiple packages and modules themselves. They are simply directories, but MUST contain a special file called _init_.py

# init.py: This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported
""" to import a module inside package """
import packageName.moduleName
from packageName import moduleName
