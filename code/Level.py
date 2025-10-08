import random
import sys
from code.Const import C_CYAN, C_GREEN, C_WHITE, EVENT_ENEMY, EVENT_TIMEOUT, MENU_OPTION, SPAWN_TIME, TIMEOUT_LEVEL, TIMEOUT_STEP, WIN_HEIGHT
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font
import pygame

from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name:str, game_mode:str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL # 20 sec
        self.window = window
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg')) # pegando a lista de background em EntityFactory.py
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0] # score do player1
        self.entity_list.append(player)
        
        # qnd for selecionado o modo cooperativo em 2:
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1] # score do player2
            self.entity_list.append(player) # nave do player 2 aparece
        # cada X tempo vem um inimigo
        
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) 
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # a cada 100 milissegundos checa a condiçao de vitoria
        
        
        
    def run(self, player_score: list[int]): # para atualizar o score qnd atualizar o lvl
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1) # carrega a musica
        clock = pygame.time.Clock() # fixa fps
        while True:
            clock.tick(60) # padrao 60 fps independente da maquina
            
            # para fechar a janela durante a fase
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) # pegando cada imagem e fazendo um blit nela ( desenhando ela )
                ent.move() # fazendo o background se mover e ela ficar redesenhando infinito = efeito paralax
                
                if isinstance(ent, (Player, Enemy)): # para apenas as entidades Player e Enemy que VAO atirar:
                    shoot = ent.shoot()
                    if shoot is not None: 
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(text_size=14, text=f'Player1 - Health: {ent.health} | Score: {ent.score}', text_color=C_GREEN, text_pos=(10, 25))
                if ent.name == 'Player2':
                    self.level_text(text_size=14, text=f'Player2 - Health: {ent.health} | Score: {ent.score}', text_color=C_CYAN, text_pos=(10, 45))
                    
                        
                        
            for event in pygame.event.get(): # evento de fechar a janela durante a fase
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice)) # spawna inimigos 1 ou 2 aleatoriamente
                
                if event.type == EVENT_TIMEOUT: # a cada 100 milissegundos
                    self.timeout -= TIMEOUT_STEP # diminui os 20sec da fase
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score 
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score  
                                 
                        return True # chegar em 0, encerra a fase e começa o lvl 2
                
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                        
                if not found_player: # if found_player == False
                    return False # se o jogador morrer, retorna false
                
            
            # mostra o texto
            # tempo de duracao da fase
            self.level_text(text_size=14, text=f'{self.name} - Tempo de Fase: {self.timeout / 1000:.0f}s', text_color=C_WHITE, text_pos=(10,5))
            # mostra o fps do game em tempo real
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            # mostra quantas entidades tem na tela
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 20))
            pygame.display.flip()
            
            EntityMediator.verify_collision(entity_list=self.entity_list) # verificando colisoes
            EntityMediator.verify_health(entity_list=self.entity_list) # verificando a vida   
    
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() # uma imagem feita
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
