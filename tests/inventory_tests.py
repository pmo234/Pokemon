import unittest

from src.character import Character
from src.moves import Moves
from src.items import Items
from src.inventory import Inventory

class TestInventory(unittest.TestCase):

    def setUp(self):
        
        self.tackle = Moves("Tackle", 1.1, "Normal", 40)
        self.vine_whip = Moves("Vine Whip", 1.2, "Grass", 20)
        self.ember = Moves("Ember",1.2,"Fire",20)
        self.water_gun = Moves("Water Gun",1.2,"Water",20)
        self.thundershock = Moves("Thundershock",1.2,"Electric",20)
        
        self.bulbasaur = Character("Bulbasaur", "Grass",[self.tackle,self.vine_whip],["Ivysaur",'Venusaur'], 10, 38, 98, 15, False)
        self.charmander = Character("Charmander", "Fire",[self.tackle,self.ember],["Charmeleon","Charizard"], 15, 70, 20, 16, False)
        self.squirtle = Character("Squirtle", "Water", [self.tackle,self.water_gun],["Wartortle", "Blastoise"], 24, 45, 105, 15, False)
        self.pikachu = Character("Pikachu", "Electric", [self.tackle,self.thundershock],["Raichu"], 25, 29, 90, 15, False)

        self.potion = Items("Potion", 1)
        self.rare_candy = Items("Rare Candy",1)
        self.pokeball = Items("Pokeball",10)

        self.inventory = Inventory([self.potion,self.rare_candy,self.pokeball],[self.bulbasaur,self.pikachu,self.squirtle])

    @unittest.skip
    def test_rare_candy(self):
        self.assertEqual("Bulbasaur's level has increased to 16",self.inventory.use_rare_candy(self.bulbasaur))

    @unittest.skip
    def test_potion(self):
        self.assertEqual("Bulbasaur's health has increased to 57",self.inventory.use_potion(self.bulbasaur))

    @unittest.skip
    def test_use_pokeball(self):
        self.inventory.use_pokeball(self.charmander)
        self.assertEqual(3,len(self.inventory.pokemon))

    @unittest.skip
    def test_use_rare_candy_through_menu(self):
        self.assertEqual("Ivysaur's level has increased to 16",self.inventory.menu_use_an_item(self.charmander))

    @unittest.skip
    def test_use_potion_through_menu(self):
        self.assertEqual("Bulbasaur's health has increased to 57",self.inventory.menu_use_an_item(self.charmander))
    
    @unittest.skip
    def test_use_pokeball_through_menu(self):
        self.inventory.menu_use_an_item(self.charmander)
        self.assertEqual(4,len(self.inventory.pokemon))

    @unittest.skip
    def test_use_move_through_menu(self):
        self.assertEqual(12,self.inventory.menu_use_a_move(self.charmander))

    @unittest.skip
    def test_run_from_battle(self):
        self.assertEqual("You failed to run away!",self.inventory.run_from_battle(self.charmander))

    @unittest.skip
    def test_change_active_pokemon(self):
        self.assertEqual("Go Pikachu!",self.inventory.change_active_pokemon(self.pikachu))

    @unittest.skip
    def test_menu_change_active_pokemon(self):
        self.assertEqual("Go Pikachu!",self.inventory.menu_change_pokemon(self.pikachu))

    @unittest.skip
    def test_use_pokeball_through_battle_menu(self):
        self.inventory.battle_menu(self.charmander)
        self.assertEqual(4,len(self.inventory.pokemon))

    @unittest.skip
    def test_battle_menu_change_active_pokemon(self):
        self.assertEqual("Go Pikachu!",self.inventory.battle_menu(self.charmander))

    @unittest.skip
    def test_use_move_through_battle_menu(self):
        self.assertEqual(12,self.inventory.battle_menu(self.charmander))
    
    
    def test_start_battle(self):
        self.inventory.start_battle(self.charmander)
        self.assertEqual(4,len(self.inventory.pokemon))