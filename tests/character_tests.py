import unittest
from src import inventory

from src.character import Character
from src.moves import Moves
from src.items import Items
from src.inventory import Inventory

class TestCharacter(unittest.TestCase):

    def setUp(self):
        
        self.tackle = Moves("Tackle", 1.1, "Normal", 40)
        self.vine_whip = Moves("Vine Whip", 1.2, "Grass", 20)
        self.ember = Moves("Ember",1.2,"Fire",20)
        self.water_gun = Moves("Water Gun",1.2,"Water",20)
        self.thundershock = Moves("Thundershock",1.2,"Electric",20)
        
        self.bulbasaur = Character("Bulbasaur", "Grass",[self.tackle,self.vine_whip],["Ivysaur",'Venusaur'], 10, 100, 10, 15, False)
        self.charmander = Character("Charmander", "Fire",[self.tackle,self.ember],["Charmeleon","Charizard"], 15, 70, 20, 16, False)
        self.squirtle = Character("Squirtle", "Water", [self.tackle,self.water_gun],["Wartortle", "Blastoise"], 24, 45, 105, 15, False)
        self.pikachu = Character("Pikachu", "Electric", [self.tackle,self.thundershock],["Raichu"], 25, 29, 42, 15, False)

        self.potion = Items("Potion", 1)
        self.rare_candy = Items("Rare Candy",1)
        self.pokeball = Items("Pokeball",6)

        self.inventory = Inventory([self.potion,self.rare_candy,self.pokeball],[self.bulbasaur,self.pikachu])
    
    @unittest.skip
    def test_battle_wild(self):
        self.inventory.attack_pokemon(self.squirtle)
        self.assertTrue(self.squirtle.fainted)

    @unittest.skip
    def test_evolve(self):
        self.charmander.evolve()
        self.assertEqual("Charmeleon",self.charmander.name)

    @unittest.skip
    def test_wild_battle_with_evolved_pokemon(self):
        self.inventory.attack_pokemon(self.squirtle.evolve())
        self.assertFalse(self.squirtle.fainted)
    
    @unittest.skip
    def test_level_up(self):    
        self.assertEqual(16,self.squirtle.level_up())
    
    @unittest.skip
    def evolve_after_level_up(self):
        self.squirtle.level_up
        self.assertEqual("Wartortle",self.squirtle.name)

    @unittest.skip
    def test_use_move(self):
        self.assertEqual(12,self.bulbasaur.use_move(self.vine_whip.name))