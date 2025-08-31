class dog():
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

obj=dog("Bulldog", "Brown")
print(obj.breed)
print(obj.color)
obj2=dog("Pug", "Black")
print(obj2.breed)
print(obj2.color)