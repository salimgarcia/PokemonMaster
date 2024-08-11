
'Functions for Pokemon'
class Pokemon:

    'Pokemon Stats'
    def __init__(self, name, level, health, max_health, type, is_knocked_out = False):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        self.is_knocked_out = is_knocked_out

    'Lose Health'
    def lose_health(self, lost_health):
        self.health = self.health - lost_health
        if self.health > 0:
            print(self.name + " now has " + str(self.health) + " health.")
            return
        'Pokemon will be knocked out if health reaches 0'
        if self.health <= 0:
            self.knock_out()
            return
    
    'Gain health'
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

'Functions for trainer'
class Trainer:

    'Trainer stats'
    def __init__(self, pokemons, potions, current_pokemon, name):
        self.pokemons = pokemons
        self.potions = potions
        self.current_pokemon = current_pokemon
        self.name = name

    'Use a Potion'
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

    'Attack another trainer'
    def attack_other_trainer(self, other_trainer):
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        if self.pokemons[self.current_pokemon].is_knocked_out:
            print("This Pokemon is knocked out and cannot attack")
            return
        print("{0} attacked {1}".format(self.name, other_trainer.name))
        self.pokemons[self.current_pokemon].attack(their_pokemon)
        return

    'Switch to another Pokemon'
    def switch_pokemon(self, new_current_pokemon):
        if len(self.pokemons) - 1 >= new_current_pokemon >= 0 and self.pokemons[new_current_pokemon].is_knocked_out == False:
            self.current_pokemon = new_current_pokemon
            print("{0} switched to {1}".format(self.name, self.pokemons[self.current_pokemon].name))
            return
        else:
            print("Invalid input")
            return

'--------------Pokemon--------------'
charmander = Pokemon('Charmander', 10, 100, 100, 'Fire')

squirtle = Pokemon('Squirtle', 8, 100, 100, 'Water')

pikachu = Pokemon('Pikachu', 12, 100, 100, 'Grass')

'--------------Trainers--------------'
red = Trainer([charmander, squirtle], 2, 0, 'Red')

ethan = Trainer([squirtle], 4, 0, 'Ethan')

ash = Trainer([pikachu], 4, 0, 'Ash')


trainers = [red, ethan, ash]

'Select a trainer to play as'
def trainer_choice():
    while True:
        selection = input("Choose your Trainer!\n1.Red\n2.Ethan\n")
        if selection in ('1', '2'):
            break
        print("Please make a valid selection...")
    if selection == '1':
        print("You Chose Red!")
        return(trainers[0])
    elif selection ==  '2':
        print("You Chose Ethan!")
        return(trainers[1])

'Select a trainer to battle'
def op_choice():
    while True:
        selection = input("Choose your Opponent!\n1.Red\n2.Ethan\n")
        if selection in ('1', '2'):
            break
        print("Please make a valid selection...")
    if selection == '1':
        print("Your opponent is Red!")
        return(trainers[0])
    elif selection ==  '2':
        print("Your opponenet is Ethan!")
        return(trainers[1])

'Menu for player options during battle'    
def battle_menu():
    while True:
        selection = input("What do you want to do?\n1.Attack\n2.Use Potion\n")
        if selection in ('1', '2'):
            break
        print("Please make a valid selection...")
    if selection == '1':
        player_trainer.attack_other_trainer(opponent_trainer)
    if selection == '2':
        player_trainer.use_potion()

def battle():
    x = 0
    while True:
        if x == 0:
            battle_menu()
            'If Opponents Pokemon gets knocked out, player wins'
            if opponent_pokemon.is_knocked_out == True:
                print("You Win!")
                break
            x += 1
        if  x == 1:
            if opponent_pokemon.health <= opponent_pokemon.max_health / 2:
                opponent_trainer.use_potion()
                x -= 1
            else:
                opponent_trainer.attack_other_trainer(player_trainer)
                'If Players pokemon gets knocked out, opponent wins'
                if player_pokemon.is_knocked_out == True:
                    print("You Lose")
                    break
                x -= 1


player_trainer = trainer_choice()
opponent_trainer = op_choice()
player_pokemon = player_trainer.pokemons[player_trainer.current_pokemon]
opponent_pokemon = opponent_trainer.pokemons[opponent_trainer.current_pokemon]

battle()


'Promp player to quit or play again'