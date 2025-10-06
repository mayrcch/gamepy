import sys
from code.Const import C_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font
import pygame


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000 # 20 sec
        self.window = window
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) # pegando a lista de background em EntityFactory.py
        
    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1) # carrega a musica
        clock = pygame.time.Clock() # fixa fps
        while True:
            clock.tick(60) # padrao 60 fps independente da maquina
            
            # para fechar a janela durante a fase
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) # pegando cada imagem e fazendo um blit nela ( desenhando ela )
                ent.move() # fazendo o background se mover e ela ficar redesenhando infinito = efeito paralax
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # mostra o texto
            # tempo de duracao da fase
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', text_color=C_WHITE, text_pos=(10,5))
            # mostra o fps do game em tempo real
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            # mostra quantas entidades tem na tela
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() # uma imagem feita
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
