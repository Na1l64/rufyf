class Animal:
    count = 0
    def __init__(self):
        Animal.count += 1
    def __del__(self):
        Animal.count -= 1

