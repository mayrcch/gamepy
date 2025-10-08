# fazer pull do projeto: do github para a maquina
import sys
import pygame
from code.Level import Level
from code.Menu import Menu
from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT)) # importando os valores de tamanho da tela do arquivo Const.py
        
    def run(self):
        # para a janela se manter aberta
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: # inicio de fase do menu = new game, coop1, coop2
                # score
                player_score = [0, 0] #[player1, player2]
                
                
                level = Level(self.window, 'Level1', menu_return, player_score) # inicia a class Level do arq Level
                level_return = level.run(player_score) # run do Level() 1
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score) # inicia a class Level do arq Level
                    level_return = level.run(player_score) # run do Level() 2
                    if level_return:
                        score.save(menu_return, player_score)
                    
             
            elif menu_return == MENU_OPTION[3]:
                score.show() # menu do score
                
            elif menu_return == MENU_OPTION[4]: # saída
                pygame.quit()
                quit() 
            else:
                pygame.quit() 
                sys.quit()
                
                
            
            
    