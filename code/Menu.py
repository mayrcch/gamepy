import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, C_WHITE, MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') #carrega a imagem
        self.rect = self.surf.get_rect(left=0, top=0) # vai começar o retangulo no canto superior esquerdo
        
    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3') # carrega o audio do menu
        pygame.mixer_music.play(-1) # musica toca, o -1 eh pra ela tocar infinitamente
        
        while True:
            self.window.blit(source=self.surf, dest=self.rect) # imagem aparece no retangulo
            self.menu_text(text_size=50, text='Mountain', text_color=C_ORANGE, text_center_pos=((WIN_WIDTH / 2), 70)) # eixo x e altura 70
            self.menu_text(text_size=50, text='Shooter', text_color=C_ORANGE, text_center_pos=((WIN_WIDTH / 2), 120)) # troca a altura so
            
            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=C_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
            
            
            pygame.display.flip() # atualiza a tela
        
        # checando tds os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechar a janela
                    quit()  # end pygame
                    
                    
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() # uma imagem feita
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        # fala a fonte utilizada e cria uma imagem para a font do texto
    
