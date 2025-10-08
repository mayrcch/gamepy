from datetime import datetime
import sys
import pygame
from pygame import K_BACKSPACE, K_ESCAPE, K_RETURN, KEYDOWN, Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, C_YELLOW, MENU_OPTION, SCORE_POS
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha() #carrega a imagem
        self.rect = self.surf.get_rect(left=0, top=0) # começa o retangulo no canto superior esquerdo
    
    def save(self, game_mode:str, player_score:list[int]):
        pygame.mixer_music.load('./asset/Score.mp3') 
        pygame.mixer_music.play(-1) 
        # abre a conexão qnd ver o Score no Menu ou qnd vencer o jogo:
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'])
            text = 'Enter Player 1 Name (6 characters):'
            score = player_score[0]
            
            if game_mode == MENU_OPTION[0]: # new game - 1 player
                score = player_score[0]
                
            # cooperativo - 2 players
            if game_mode == MENU_OPTION[1]: 
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team Name (6 characters):'
                
            # competitivo - 2 players (quem pontua mais)
            if game_mode == MENU_OPTION[2]: 
                if player_score[0] >= player_score[1]: # se o score do player 1 for maior ou igual que do player 2
                    score = player_score[0]
                    text = 'Enter Player 1 Name (6 characters):'
                else: # viceversa
                    score = player_score[1]
                    text = 'Enter Player 2 Name (6 characters):'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])
            
            for event in pygame.event.get(): # evento de fechar a janela durante a fase
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 6: # 6 char
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    
                    elif event.key == K_BACKSPACE: # delete char
                        name = name[:-1] 
                    else: # se for menor q 6 char:
                        if len(name) < 6:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])        
            pygame.display.flip()
            pass
    
    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3') # carrega o audio do score
        pygame.mixer_music.play(-1) # musica toca, o -1 eh pra ela tocar infinitamente
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', C_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10() # busca os top10
        db_proxy.close()
        
        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05.1f}     {date}', C_YELLOW,
                            SCORE_POS[list_score.index(player_score)]) # index posicionado feito do Score em Const.py            
            # 05.1f
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()
            pass
    
    # texto do score  
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

# pega a data atual 
def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M") # hora e min q terminou o jogo
    current_date = current_datetime.strftime("%d/%m/%y") # data q temrinou o jogo
    return f"{current_time} - {current_date}"

