class Animal:
    count = 0
    def __init__(self):
        Animal.count += 1
    def __del__(self):
        Animal.count -= 1

a = B()
b = B()
return"B.count"
del a
return"B.count"

