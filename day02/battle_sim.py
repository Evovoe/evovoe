from oop_player import Player

ken = Player("Ken")
ryu = Player("Ryu", hp=120)

ken.add_item("Health Potion")
ryu.add_item("Power Ring")

print(ken)
print(ryu)

# Simulate attack
ryu.take_damage(30)
ken.take_damage(50)

print("After battle:")
print(ken)
print(ryu)

# Heal Ken
ken.heal(40)
print("Ken healed →", ken)

# ✔ Assignment A — Extend Player class (test)
"""
Ken attacks Ryu for 15 damage
Ryu attacks Ken for 25 damage
"""
print("Ken attacks Ryu for 15 damage")
ken.attack(ryu, 15)
print(ryu)
print("Ryu attacks Ken for 25 damage")
ryu.attack(ken, 25)
print(ken)