class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.inventory = []

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def heal(self, amount):
        self.hp = min(100, self.hp + amount)

    def add_item(self, item):
        self.inventory.append(item)

    # ✔ Assignment A — Extend Player class
    def attack(self, target, dmg):
        target.take_damage(dmg)
    # end
    
    def __repr__(self):
        return f"<Player {self.name} | HP={self.hp} | Items={self.inventory}>"

class Team:
    def _init_(self):
        self.__playerslist = []

    def add_player(self, player):
        self.__playerslist.append(player)

    def team_hp(self):
        return sum(player.hp for player in self.__playerslist)

    def alive_players(self):
        return[player for player in self.__playerslist if player.hp > 0]