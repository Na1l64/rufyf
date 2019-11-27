class Animal:
    __count = 0
    def __init__(self):
        Animal.__count += 1
    def __del__(self):
        Animal.__count -= 1
    def seqrurity(self):
        return Animal.__count

a = Animal()
b = Animal()
print (Animal.seqrurity())
