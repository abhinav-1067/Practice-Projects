class Character:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
    def attack_enemy(self,enemy):
        enemy.health = enemy.health - self.health
        print(f"{self.name} attack {enemy.name}")
        print(f"{enemy.name} Health is now {enemy.health}")
        
# defining character
hero = Character("Hero",85,20)
goblin = Character("Goblin",80,15)

# printing values
print(hero.name,hero.health,hero.attack,)
print(goblin.name,goblin.health,goblin.attack)