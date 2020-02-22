class MyException(Exception):
    pass

try:
    raise MyException("My hovercraft is full of animals", 404)
except MyException as e:
    print(e.args[0],e.args[1])
