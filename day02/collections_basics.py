# ----- LIST -----
weapons = ["Sword", "Dagger", "Bow"]
weapons.append("Spear")
weapons.remove("Dagger")
print("Weapons:", weapons)

# ----- TUPLE -----
stats = (100, 40, 20)   # (hp, attack, defense)
print("Base stats (tuple):", stats)

# ----- SET -----
boss_defeats = {"Dragon", "Giant", "Dragon"}   # duplicates removed
print("Unique bosses defeated:", boss_defeats)

# ----- DICTIONARY -----
player = {"name": "Ryu", "level": 5, "xp": 2400}
player["xp"] += 300
print("Player dict:", player)
