# fazer pull do projeto: do github para a maquina
import pygame
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT)) # importando os valores de tamanho da tela do arquivo Const.py
        
    def run(self):
        # para a janela se manter aberta
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            
            
    