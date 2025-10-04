from abc import ABC, abstractmethod
import pygame.image


class Entity(ABC): # classe abstrata q terá implementacoes nas suas 'classes filhas'
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # posicao dos inimigos e onde a nave vai(?)
        self.speed = 0 # velocidade
        
    @abstractmethod   # decorator 
    def move(self, ):
        pass