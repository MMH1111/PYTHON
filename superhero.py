class Superhero:
    def __init__(self, name, alias, ability, species, weakness, origin, health= 100):
        self.name = name
        self.alias = alias
        self.ability = ability
        self.species = species
        self.weakness = weakness
        # weakness should be 2 times normal damage; if resistance .5  
        self.origin = origin
        self.health = health
#METHODS
    def power(self):
        print(f"{self.name} AKA {self.alias}  uses {self.ability}")
    
    def attacked(self, target):
        if self.health > 0:
            target.health -= 100
        print(target.display_user_balance())
        if target.health <= 0:
            print(f"{self.name} has won!")
                
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.health}")
        return self

    

#instance
superhero1 = Superhero("ethan","ETREE", "super omega farm", "flora", "fire", " the redwoods")
superhero2 = Superhero("chad", "Whey-Boy", "superego", "a bro", "Intelligence", "the g
