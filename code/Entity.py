from abc import ABC, abstractmethod
import pygame.image

from code.Const import ENTITY_HEALTH


class Entity(ABC): # classe abstrata q terá implementacoes nas suas 'classes filhas'
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() # trata a imagem png
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # posicao dos inimigos e onde a nave vai(?)
        self.speed = 0 # velocidade
        self.health = ENTITY_HEALTH[self.name]
        
    @abstractmethod   # decorator 
    def move(self, ):
        pass