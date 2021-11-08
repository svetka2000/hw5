import abc
from  abc import ABC
from random import choice

class AnimeMon(ABC):
    @abc.abstractmethod
    def inc_exp(self, value: int):
        self.experience += value
    @property
    @abc.abstractmethod
    def exp(self):
        return self.experience

class Digimon(AnimeMon):
    def __init__(self, name: str):
        self.name = name
        self.experience = 0
    def inc_exp(self, value: int):
        self.experience += value * 8
    @property
    def exp(self):
        return super().exp


class BasePokemon:
    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    emodji = {'grass': '🌿', 
           'fire': '🔥', 
           'water':'🌊', 
           'electric': '⚡'}
    def __str__(self):
        text_poketype = super().__str__()
        return text_poketype.replace(self.poketype, self.emodji[self.poketype])


class Pokemon(AnimeMon, EmojiMixin, BasePokemon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self.experience = 0
    def inc_exp(self, value: int):
        super().inc_exp(value)
    @property
    def exp(self):
        return super().exp


def train(animemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = choice([True, False])
        if win:
            animemon.inc_exp(step_size) 
            

if __name__ == '__main__':
    agumon = Digimon(name='Agumon')
    print(agumon.exp)
    train(agumon)
    print(agumon.exp)

    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
    pikachu = Pokemon(name='Pikachu', poketype='electric')
    print(pikachu)
    print(pikachu.exp)
    
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur.exp)
    train(bulbasaur)
    print(bulbasaur.exp)