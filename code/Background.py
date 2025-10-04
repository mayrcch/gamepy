from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name, position) # super classe
        
        
    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # cada imagem vai se mover com sua respectiva velocidade de acordo com oq foi definido em Const.py
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        # td vez que o canto direito da imagem passar pela tela toda "completando a imagem", ela reseta, fazendo um efeito de background infinito da mountain
        