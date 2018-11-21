class Customer:  # B1 #A2
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def name(self):
        return self.first_name + self.family_name

    def full_name(self):
        print(self.name())

        print(self.age)


if __name__ == "__main__":
    ken = Customer("Ken ", "Takahashi", 15)
    ken.full_name()
    ken.age

    tom = Customer("Tom ", "Ford", 57)
    tom.full_name()
    tom.age

    ieyasu = Customer("Ieyasu ", "Tokugawa", 73)
    ieyasu.full_name()
    ieyasu.age
