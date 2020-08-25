class Pokemon:
  def __init__(self, name, types, level):
    self.name = name
    self.level = level
    self.health = level * 5
    self.max_health = level * 5
    self.types = types
    self.is_knocked_out = False
  
  def __repr__(self):
    return f"Pokemon info: {self.name}, Type: {self.types}, Current Health: {self.health}, Max Health: {self.max_health}"
    
  def revive(self):
    self.is_knocked_out = False
    if self.health == 0:
      self.health = 1
    print(f"{self.name} was revived!")

  def knock_out(self):
    self.is_knocked_out = True
    if self.health != 0:
      self.health = 0
    print(f"{self.name} has been knocked out")

  def lose_health(self, life):
    self.health -= life
    if self.health <= 0:
       self.health = 0
       self.knock_out()
    else:
      print(f"{self.name} now has {self.health} health.")

  def gain_health(self, heal):
    if self.health == 0:
        self.revive()
        self.health +=heal
    print(f"{self.name} now has {self.health} health")

  def attack (self, other_pokemon):
      if self.is_knocked_out == True:
        print(f"You can't attack. {self.name} has been knocked out.")
      return
      if (self.types == "Grass" and other_pokemon.types == "Fire") or (self.types == "Fire" and other_pokemon.types == "Water") or (self.types == "Water" and other_pokemon.types == "Grass"):
        damage = self.level * 0.5
        print("It's not an effective attack!")
        other_pokemon.loose_health(round(damage))
      if (self.types == other_pokemon.types):
        print("Both used same power")
        other_pokemon.loose_health(self.level)
      if (self.types == "Fire" and other_pokemon.types == "Grass") or (self.types == "Grass" and other_pokemon.types == "Water") or (self.types == "Water" and other_pokemon.types == "Fire"):
        damage = self.level * 2
        print("It's an effective attack!")
        other_pokemon.loose_health((damage))

class Charmander(Pokemon):
  def __init__(self, level = 5):
    super().__init__("Charmander", "Fire", level)

class Pikachu(Pokemon):
  def __init__(self, level = 5):
    super().__init__("Pikachu", "Water", level)

class Eevee(Pokemon):
  def __init__(self, level = 5):
    super().__init__("Eevee", "Grass", level)

class Trainer:
  def __init__(self, pokemon_list, num_potions, name):
    self.pokemons = pokemon_list
    self.potions = num_potions
    self.c_pokemon = 0
    self.name = name
    
  def __repr__(self):
    print(f"The trainer {self.name} has the following pokemon")
    for pokemon in self.pokemons:
      print(pokemon)
    return f"The current active pokemon is {self.pokemons[self.c_pokemon].name}"

        

  def switch_active_pokemon(self, new_pokemon):
    if new_pokemon < len(self.pokemons) and new_pokemon >= 0:
      if self.pokemons[new_pokemon].is_knocked_out:
        print(f"{self.pokemons[new_pokemon].name} is knocked out.")
      elif new_pokemon == self.c_pokemon:
        print(f"{self.pokemons[new_pokemon].name} is your active pokemon")
      else:
        self.c_pokemon = new_pokemon
        print(f"Now {self.pokemons[self.c_pokemon].name} pokemon turn!")


  def use_potion(self):
    if self.potions > 0:
      print(f"{self.pokemons[self.c_pokemon].name} has used a potions ")
      self.pokemons[self.c_pokemon].gain_health(20)
      self.potions -= 1
    else:
      print("No Potions Left!")

  def attack_other_trainer(self, other_trainer):
    my_pokemon = self.pokemons[self.c_pokemon]
    # print(dir(my_pokemon))
    their_pokemon = other_trainer.pokemons[other_trainer.c_pokemon]
    my_pokemon.attack(their_pokemon)

a = Charmander(7)
b = Pikachu()
c = Pikachu(1)
d = Eevee(10)
e = Charmander(8)
f = Eevee()

trainer_one = Trainer([a,b,c], 3, "Alex")
trainer_two = Trainer([d,e,f], 5, "Billa")
print(trainer_one)
print(trainer_two)

trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(2)