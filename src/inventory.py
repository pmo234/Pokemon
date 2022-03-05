
from random import *
from src.character import Character
import sys


class Inventory:
    def __init__(self,items,pokemon):
        self.items = items
        self.pokemon = pokemon

    def start_battle(self,wild_pokemon):
       
        print("A wild " + wild_pokemon.name + " has appeared! " + wild_pokemon.name + " has " + str(wild_pokemon.health) + " health.")
        print("You sent out " + self.pokemon[0].name + ". " + self.pokemon[0].name + " has " + str(self.pokemon[0].health) + " health.")

        self.battle_menu(wild_pokemon)
        

    def battle_menu(self,wild_pkm):
        
        menu_choice = input("Type what you would like to do?  Use Move  Use Item  Change Pokemon  Run ")
        if menu_choice.lower() == "use move":
             self.menu_use_a_move(wild_pkm)
        if menu_choice.lower() == "use item":
             self.menu_use_an_item(wild_pkm)
        if menu_choice.lower() == "change pokemon":
             self.menu_change_pokemon(wild_pkm)
        if menu_choice.lower() == "run":
             self.run_from_battle(wild_pkm)
        self.battle_menu(wild_pkm)

    def menu_use_an_item(self,wild_pokemon):
        
        if len(self.items) == 3:
            item_choice = input("Which item would you like to use? " + self.items[0].name + "(" + str(self.items[0].amount) + ") " + self.items[1].name + "(" + str(self.items[1].amount) + ") " 
            + self.items[2].name + "(" + str(self.items[2].amount) + ") (Type 'back' to go back.) ")
            
        if len(self.items) == 2:
            item_choice = input("Which item would you like to use? " + self.items[0].name + "(" + str(self.items[0].amount) + ") "
             + self.items[1].name + "(" + str(self.items[1].amount) + ") (Type 'back' to go back.) "  )
            
        if len(self.items) == 1:
            item_choice = input("Which item would you like to use? " + self.items[0].name + "(" + str(self.items[0].amount) + ") (Type 'back' to go back.) "  )
            
        if len(self.items) ==0:
            return print ("You have no more items!")
        for available_items in self.items:
            if item_choice.lower() == "rare candy":
                self.use_rare_candy(self.pokemon[0])
                self.wild_pokemon_attack(wild_pokemon)
            if item_choice.lower() == "potion":
                self.use_potion(self.pokemon[0])
                self.wild_pokemon_attack(wild_pokemon)
            if item_choice.lower() == "pokeball":
                self.use_pokeball(wild_pokemon)
                self.wild_pokemon_attack(wild_pokemon)
            if item_choice.lower() == "back":
                return
        self.menu_use_an_item(wild_pokemon)

    def menu_change_pokemon(self,wild_pokemon):
        if len(self.pokemon)==3:
            pokemon_choice = input("Which Pokemon would you like to switch to? " + self.pokemon[1].name + " " + self.pokemon[2].name + " (Type 'back' to go back.) "  )
        if len(self.pokemon)==2:
            pokemon_choice = input("Which Pokemon would you like to switch to? " + self.pokemon[1].name + " (Type 'back' to go back.) "  )
        if len(self.pokemon)==1:
            print("You have no more pokemon to switch to!")
            self.battle_menu(wild_pokemon)
        for available_pokemon in self.pokemon:
            if pokemon_choice.capitalize() == available_pokemon.name and pokemon_choice.capitalize() != self.pokemon[0].name:
                self.change_active_pokemon(available_pokemon)
                self.wild_pokemon_attack(wild_pokemon)
            if pokemon_choice.lower() == "back":
                return
        self.menu_change_pokemon(wild_pokemon)

    def menu_use_a_move(self,wild_pokemon):
        move_choice = input("Which move would you like to use? " + self.pokemon[0].moves[0].name + " " + self.pokemon[0].moves[1].name + " (Type 'back' to go back.) "  )
        
        for available_moves in self.pokemon[0].moves:
            if move_choice.lower() == available_moves.name.lower():
                self.use_move(move_choice,wild_pokemon)
                return self.pokemon[0].strength
            if move_choice.lower() == "back":
                return
        self.menu_use_a_move(wild_pokemon)
        
    def use_move(self,move_choice,wild_pokemon):
        for available_move in self.pokemon[0].moves:
            if move_choice.lower() == available_move.name.lower() and available_move.pp !=0:
                print( self.pokemon[0].name + " used " + move_choice)
                self.pokemon[0].strength *= available_move.power
                self.attack_pokemon(wild_pokemon)
        self.use_move(move_choice,wild_pokemon)


    def attack_pokemon(self,wild_pkm):
        wild_pkm.health -= round(self.pokemon[0].strength)
        if wild_pkm.health <= 0:
            wild_pkm.fainted = True
            print(wild_pkm.name + " has fainted!")
            self.pokemon[0].exp += 25
            print(self.pokemon[0].name + " gained 25 exp!")
            self.pokemon[0].level_up()
            sys.exit()
        print(wild_pkm.name + " has " + str(wild_pkm.health) + " health left!" )
        self.wild_pokemon_attack(wild_pkm)    
        
        
    def wild_pokemon_attack(self,wild_pkm):
        move_choice = choice(wild_pkm.moves)
        print(wild_pkm.name + " used " + move_choice.name)
        new_attack_strength = move_choice.power*wild_pkm.strength
        self.pokemon[0].health -= round(new_attack_strength)
        if self.pokemon[0].health <= 0:
            self.pokemon[0].fainted = True
            print(self.pokemon[0].name + " has fainted!")
            self.choose_new_pokemon_after_fainting(wild_pkm)
            
        print(self.pokemon[0].name + " has " + str(self.pokemon[0].health) + " health left!" )
            
        self.battle_menu(wild_pkm)



    def use_rare_candy(self,pokemon_name):
        for pokemon in self.pokemon:
            if pokemon == pokemon_name:
                for item in self.items:
                    if item.amount != 0 and item.name == "Rare Candy":
                        item.amount -= 1
                        if item.amount == 0:
                            self.items.remove(item)
                        pokemon.level +=1
                        print(pokemon.name + "'s level has increased to " + str(pokemon.level))
                        pokemon.evolve()
                        return pokemon.name + "'s level has increased to " + str(pokemon.level)
                       

    def use_potion(self,pokemon_name):
        for pokemon in self.pokemon:
            if pokemon == pokemon_name:
                for item in self.items:
                    if item.name == "Potion" and item.amount != 0:
                        item.amount -= 1
                        if item.amount == 0:
                            self.items.remove(item)
                        pokemon.health +=20
                        print(pokemon.name + "'s health has increased to " + str(pokemon.health))
                        return pokemon.name + "'s health has increased to " + str(pokemon.health)

    def use_pokeball(self,pokemon_to_catch):
        chance_to_catch = random()*100
        print(chance_to_catch)
        for item in self.items:
            if item.name == "Pokeball" and item.amount !=0:
                item.amount -= 1
                if item.amount == 0:
                    self.items.remove(item)
                if pokemon_to_catch.health < chance_to_catch:
                    self.pokemon.append(pokemon_to_catch)
                    print("Congratulations you caught " + pokemon_to_catch.name + "!")
                    sys.exit()
                else: print("Oh no! " + pokemon_to_catch.name + " broke free!")
                self.wild_pokemon_attack(pokemon_to_catch)

    def run_from_battle(self,wild_pokemon):
        chance_to_run = random()*100
        if wild_pokemon.health < chance_to_run:
            sys.exit("You ran away!")
        else: print("You failed to run away!")
        self.wild_pokemon_attack(wild_pokemon)

    def change_active_pokemon(self,pkm_to_become_active_pkm):
        current_active_pkm = self.pokemon[0].name
        new_order = [pkm_to_become_active_pkm]
        for available_pkm in self.pokemon:
            if pkm_to_become_active_pkm.name != available_pkm.name and available_pkm.fainted == False:
               new_order.append(available_pkm)
        self.pokemon =new_order
        print("Come back " + current_active_pkm + "!")
        print("Go " + self.pokemon[0].name + "!")
        return("Go " + self.pokemon[0].name + "!")

    def choose_new_pokemon_after_fainting(self,wild_pokemon):
        non_fainted_pokemon = []
        for available_pokemon in self.pokemon:
            if available_pokemon.fainted == False:
                non_fainted_pokemon.append(available_pokemon)
        if len(non_fainted_pokemon) == 0:
            print ("You are out of available Pokemon. You Lose.")
            sys.exit()
        if len(non_fainted_pokemon) == 1:
            self.pokemon[0] = non_fainted_pokemon[0]
            self.pokemon = non_fainted_pokemon
            print("Go " + self.pokemon[0].name)
            self.battle_menu(wild_pokemon)
        if len(non_fainted_pokemon) == 2:
            new_active_pokemon = input("Which Pokemon do you want to send out next? " + non_fainted_pokemon[0].name + " " + non_fainted_pokemon[1].name + " ")
            for pokemon_left in non_fainted_pokemon:
                if new_active_pokemon.lower() == pokemon_left.name.lower():
                    non_fainted_pokemon.remove(pokemon_left)
                    non_fainted_pokemon.insert(0,pokemon_left)
                    self.pokemon = non_fainted_pokemon
                    print("Go " + self.pokemon[0].name)
                    self.battle_menu(wild_pokemon)
            else:self.choose_new_pokemon_after_fainting(wild_pokemon)
            



        
                
