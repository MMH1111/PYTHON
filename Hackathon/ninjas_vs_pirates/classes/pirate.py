import random
class Pirate:

    def __init__(self , name, sp_attack, speed = (random.randrange(1,10)), strength =(random.randrange(1,20))):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.attack = 20
        self.health = 100
        self.sp_attack = sp_attack

    def show_stats(self, ninja):
        print(f"Name: {self.name} Health: {self.health}\n")
        if self.health <= 0:
            print(f"{self.name} is dead! \n{ninja.name} is the victor!")
        return self

    def do_attack (self, ninja):
        ninja.health -= self.attack
        sp_attack = self.sp_attack
        print(f"{self.name} {sp_attack} {ninja.name}'s face!")
        ninja.show_stats(self)
        return self

    def block (self, ninja):
        if self.strength > ninja.strength:
            print(f"{self.name} blocked {ninja.name}'s attack!")
        else: 
            print(f"{self.name} couldn't dodge {ninja.name}'s attack!")
            self.health -= ninja.attack
            self.show_stats(ninja)
        return self
        
    def yell (self):
        print("{self.name} says 'ARRRGGGHHHHH!!!'")
        return self

    def lunge (self, ninja):
        if self.strength > ninja.strength:
            ninja.health -= self.attack
            print(f"{self.name} lunged at {ninja.name} and made contact!")
            ninja.show_stats(self)
        else:
            self.health -= ninja.attack
            print(f"{self.name} tried to lunge at {ninja.name} but instead fell and hurt themselves...")
            self.show_stats(ninja)
        return self

