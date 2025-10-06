import pygame.key
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)
        pass
    
    # def update(self, ):
    #     pass
    
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: # se UP for clicado E chegar ate o final do topo ( pra n sumir )
            self.rect.centery -= ENTITY_SPEED[self.name] # cada vez q verificar o pressionado, vai subir na velocidade salva em Const.py
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: # se UP for clicado E chegear ate o final abaixo ( pra n sumir )
            self.rect.centery += ENTITY_SPEED[self.name] # cada vez q verificar o pressionado, vai descer na velocidade salva em Const.py    
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0: 
            self.rect.centerx -= ENTITY_SPEED[self.name] # diminuindo o valor de Y ate bater na borda esquerda   
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name] # aumentando o valor de X ate bater na borda direita
        
        
        # tem que ser 'if', pois se for 'elif' não conseguiria apertar vários botões de uma vez só na movimentação.
        pass