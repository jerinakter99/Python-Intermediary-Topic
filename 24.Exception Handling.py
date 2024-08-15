# An exception is an error that happens during the execution of a program.
# manage errors gracefully without stopping the execution of your program.
# When an error occurs, Python raises an exception.
# You can handle these exceptions using try, except, else, and finally blocks

try:
    # Code that might raise an exception
    pass
except SomeException as e:
    # Code that runs if the exception occurs
    pass
else:
    # Code that runs if no exception occurs
    pass
finally:
    # Code that runs no matter what
    pass
