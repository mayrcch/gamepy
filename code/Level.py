from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) # pegando a lista de background em EntityFactory.py
        
    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) # pegando cada imagem e fazendo um blit nela ( desenhando ela )
                ent.move() # fazendo o background se mover e ela ficar redesenhando infinito = efeito paralax
            pygame.display.flip()
        pass
