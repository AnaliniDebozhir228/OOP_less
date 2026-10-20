from animals import animal


class cat(animal):
    def __init__(self,name, age):
        super().__init__(name,age)
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        print(sound)

cat1 = cat(name="Marusya", age=10)
cat2 = cat(name="Belash", age=11)
print(cat1.__str__(), cat2.__str__())
cat1.speak('Meow')
cat2.speak('MEOOOOW')
