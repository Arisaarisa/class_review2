class Customer:  #B1
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def name(self):
        return self.first_name + self.family_name

    def full_name(self):
        print(self.name())


if __name__ == "__main__":
    ken = Customer("Ken ", "Takahashi")
    ken.full_name()

    tom = Customer("Tom ", "Ford")
    tom.full_name()
