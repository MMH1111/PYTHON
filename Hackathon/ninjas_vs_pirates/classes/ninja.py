import random

class Ninja:

    def __init__(self , name , sp_attack, speed = (random.randrange(1,20)) , strength =(random.randrange(1,10))):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = 100
        self.attack = 10
        self.sp_attack = sp_attack
    
    def show_stats(self, pirate):
        print(f"Name: {self.name} \nHealth: {self.health}\n")
        if self.health <= 0:
            print(f"{self.name} is dead! \n{pirate.name} is the victor!")
        return self

    def do_attack(self, pirate):
        sp_attack = self.sp_attack
        print(f"{self.name} {sp_attack} {pirate.name}")
        # pirate.health -= self.attack
        pirate.show_stats(self)
        return self

    def dodge (self, pirate):
        if self.speed > pirate.speed:
            print(f"{self.name} dodged {pirate.name}'s attack!")
        else:
            print(f"{self.name} couldn't dodge {pirate.name}'s attack!")
            self.health -= pirate.attack
            self.show_stats(pirate)
        return self

    def parry (self, pirate):
        if self.strength > pirate.strength:
            pirate.health -= self.attack
            print(f"{self.name} parried {pirate.name} and attacked and spit {pirate.name}")
            pirate.show_stats(self)
        else:
            self.health -= pirate.attack
            print(f"{self.name} failed to parry {pirate.name}'s attack!")
            self.show_stats(pirate)
        return self
        

