from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo" , "throws pizza stars")
leonardo = Ninja("Leonardo", "spins with swords")
donatello = Ninja("Donatello", "rebel sad boy tears")
raphael = Ninja("Raphael", "round house kick")
splinter = Ninja("Splinter", "gives Yoda advice")


jack_sparrow = Pirate("Captain Jack Sparrow" , "throws a jar of dirt")
shredder = Pirate("Shredder", "plows through walls")
captain_morgan = Pirate("Captain Morgan", "throws bottle of rum")
will = Pirate("Will Turner Jr.", "throws loving glances at Elizabeth Swann")
barbosa = Pirate("Captain Barbossa", "spits sea water and barnacles")

michelangelo.do_attack(jack_sparrow)
jack_sparrow.lunge(michelangelo)
michelangelo.parry(jack_sparrow)
captain_morgan.yell()
captain_morgan.lunge(splinter)
splinter.parry(captain_morgan)
shredder.do_attack(captain_morgan)
barbosa.yell()
donatello.do_attack(barbosa)
barbosa.block(donatello)
raphael.do_attack(barbosa)
barbosa.block(raphael)
barbosa.yell()
will.lunge(leonardo)
leonardo.parry(will)
