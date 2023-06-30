"""
exception handling
"""

""" syntax """
try:
    pass
except ExceptionName:
    pass
except:
    pass
else:
    pass  # always executes after successful try block
finally:
    print("always executes, even if there is an exception")
