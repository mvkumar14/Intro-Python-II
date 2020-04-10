class Item():
    def __init__(self,name,description):
        self.name = name.lower()
        self.description = description
    def on_take(self):
        print(f"You picked up a {self.name}!")
    def on_drop(self):
        print(f"You dropped a {self.name}!")


class Weapon(Item):
    def __init__(self,name,description, damage, weight):
        super().__init__(self,name,description)
        self.damage = 10
        self.weight = weight
