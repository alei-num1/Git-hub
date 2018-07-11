class Fish:
    def __init__(self, name, color, age, weight):
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight

    def swim(self):
        print("The fish %s is swimming." % self.name)

    def introduce(self):
        print("I'm %s, my body is %s, and I'm %d years old." % (self.name, self.color, self.age))

    def describe_weight(self):
        print("%s has %f kg." % (self.name, self.weight))


# class RedPomfret(Fish):
#     def __init__(self, name, color, age, weight):
#         super().__init__(name, color, age, weight)


class Goldish(Fish):
    def __init__(self, name, color, age, weight):
        super().__init__(name, color, age, weight)


goldish1 = Goldish('A_jin', 'red', 18, 0.7)
goldish1.introduce()
goldish1.describe_weight()
