class Animal:
    def __init__(self,name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(f'Name: {self.name} \nHealth: {self.health}')
        return self

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.health = 150
    def pet(self):
        self.health +=5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
    def displayHealth(self):
        super().displayHealth()
        print('I am a Dragon')
        return self


animal1 = Animal('Ralph')
animal2 = Animal('Lenny')
dragon1 = Dragon('Carl')

# animal1.walk().walk().walk().run().run().displayHealth()
animal2.displayHealth()
dragon1.displayHealth()