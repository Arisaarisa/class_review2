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

    def entry_free(self):
        if self.age < 20:
            return print(1000)

        if self.age >= 20 and self.age < 65:
            return print(1500)

        if self.age >= 65:
            return print(1200)

        print(self.entry_free())

    def info_csv(self):
        print(f"{self.full_name()}{self.age}{self.entry_free()}")


if __name__ == "__main__":
    ken = Customer("Ken ", "Takahashi", 15)
    # ken.full_name()
    # ken.age
    # ken.entry_free()
    ken.info_csv()

    tom = Customer("Tom ", "Ford", 57)
    # tom.full_name()
    # tom.age
    # tom.entry_free()
    tom.info_csv()

    ieyasu = Customer("Ieyasu ", "Tokugawa", 73)
    # ieyasu.full_name()
    # ieyasu.age
    # ieyasu.entry_free()
    ieyasu.info_csv()
