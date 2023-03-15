class Dog(object):
    def nickname(self, name):
        self.name = name

dog1 = Dog()
bobik = dog1.nickname("Bobik")
print(dog1.name)
# Bobik
print(bobik)

