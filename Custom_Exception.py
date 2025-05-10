class Custom_Exception(Exception):
    pass

try:
    raise Custom_Exception("you are basd boy")
except Custom_Exception:
    print("My custom exception is raised")