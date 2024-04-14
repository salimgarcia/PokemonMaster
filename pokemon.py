class Pokemon:
    def __init__(self, name, level, health, max_health, type, is_knocked_out = False):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        self.is_knocked_out = is_knocked_out

    def lose_health(self, lost_health):
        self.health = self.health - lost_health
        if self.health > 0:
            print(self.name + " now has " + str(self.health) + " health.")
            return
        if self.health <= 0:
            self.knock_out()
            return

    def gain_health(self, gained_health):
        if self.health + gained_health > self.max_health:
            self.health = self.max_health
        if self.health + gained_health <= self.max_health:
            self.health = self.health + gained_health
        print(self.name + " now has " + str(self.health) + " health")
        return 0

    def knock_out(self):
        if self.health <= 0:
            self.is_knocked_out = True
            print(self.name + " is knocked out!")
        return 0

    def revive(self):
        if self.is_knocked_out:
            self.is_knocked_out = False
            print(self.name + " has been revived!")
        return 0

    def attack(self, opponent):
        damage = 0
        if self.type == 'Fire' and opponent.type == 'Grass' or self.type == 'Water' and opponent.type == 'Fire' or self.type == 'Grass' and opponent.type == 'Water':
            damage = self.level * 2
        elif self.type == 'Grass' and opponent.type == 'Fire' or self.type == 'Fire' and opponent.type == 'Water' or self.type == 'Water' and opponent.type == 'Grass':
            damage = self.level / 2
        elif self.type == opponent.type:
            damage = self.level
        print("{0} did {1} damage to {2}".format(self.name, str(damage), opponent.name))
        opponent.lose_health(damage)
        return 0

class Trainer:
    def __init__(self, pokemons, potions, current_pokemon, name):
        self.pokemons = pokemons
        self.potions = potions
        self.current_pokemon = current_pokemon
        self.name = name

    def use_potion(self):
        if self.pokemons[self.current_pokemon].health == self.pokemons[self.current_pokemon].max_health:
            print("{0} already has full health".format(self.pokemons[self.current_pokemon].name))
            return
        if self.potions > 0:
            print("{0} used a potion on {1}".format(self.name, self.pokemons[self.current_pokemon].name))
            if self.pokemons[self.current_pokemon].is_knocked_out:
                self.pokemons[self.current_pokemon].revive()
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("{0} has no more potions.".format(self.name))
        return

    def attack_other_trainer(self, other_trainer):
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        if self.pokemons[self.current_pokemon].is_knocked_out:
            print("This Pokemon is knocked out and cannot attack")
            return
        print("{0} attacked {1}".format(self.name, other_trainer.name))
        self.pokemons[self.current_pokemon].attack(their_pokemon)
        return

    def switch_pokemon(self, new_current_pokemon):
        if len(self.pokemons) - 1 >= new_current_pokemon >= 0 and self.pokemons[new_current_pokemon].is_knocked_out == False:
            self.current_pokemon = new_current_pokemon
            print("{0} switched to {1}".format(self.name, self.pokemons[self.current_pokemon].name))
            return
        else:
            print("Invalid input")
            return


charmander = Pokemon('Charmander', 200, 100, 100, 'Fire')

squirtle = Pokemon('Squirtle', 8, 100, 100, 'Water')

red = Trainer([charmander, squirtle], 2, 0, 'Red')

ethan = Trainer([squirtle], 4, 0, 'Ethan')

red.attack_other_trainer(ethan)
ethan.attack_other_trainer(red)
ethan.use_potion()
red.use_potion()

