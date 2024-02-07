from weapon import fists



class Character:
    def __init__(self, name:str , health:int, damage:int):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to "
              f"{target.name} with {self.weapon.name}") 

class Hero(Character):
    def __int__(self, name:str, health:str ) ->None:
        super().__init__(name=name, health=health)
    