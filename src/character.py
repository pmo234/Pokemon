from src import inventory


class Character:


    def __init__(self,name,type,moves,evolutions,strength,health,exp,level,fainted):
        self.name = name
        self.type = type
        self.moves = moves
        self.evolutions = evolutions
        self.strength = strength
        self.health = health
        self.exp = exp
        self.level = level
        self.fainted = fainted
    


    def evolve(self):
        
        if len(self.evolutions)> 0:
            if self.name == self.evolutions[0]:
               return
            if self.level > 15:
                self.strength *= 1.5
                self.health *= 1.5
                round(self.strength)
                round(self.health)
                print(self.name + " has evolved into " + self.evolutions[0] + "!")
                self.name = self.evolutions[0]

        if len(self.evolutions)> 1:
            if self.name == self.evolutions[1]:
                return   
            if self.level > 31:
               self.strength *= 1.5
               self.health *= 1.5
               print(self.name + " has evolved into " + self.evolutions[1] + "!")
               self.name = self.evolutions[1]
            
        
        return self
            
    def level_up(self):
        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            self.evolve()
        return
    
    