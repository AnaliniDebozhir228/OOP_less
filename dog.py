from animals import animal


class Dog(animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age, breed)


dog = Dog(name='Myxtar', age='9', breed='Dvornyaga')

print(dog.__str__())

