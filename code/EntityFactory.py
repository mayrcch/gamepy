import random
from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name:str): # os background smp vao ser instanciados em esq0, top0
        match entity_name:
            case 'Level1Bg': # lvl 1
                list_bg = [] # tds os backgrounds dentro dessa lista
                for i in range(7): # p/ cada arq de background da fase1 passando
                    list_bg.append(Background(f'Level1Bg{i}', position=(0,0))) # começa no inicio da tela e vai diminuindo
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0))) # vao entrando p tela, redesenhando o background = efeito parallax
                return list_bg
            
            case 'Level2Bg': # lvl 2
                list_bg = [] # tds os backgrounds dentro dessa lista
                for i in range(5): # p/ cada arq de background da fase2 passando
                    list_bg.append(Background(f'Level2Bg{i}', position=(0,0))) # começa no inicio da tela e vai diminuindo
                    list_bg.append(Background(f'Level2Bg{i}', position=(WIN_WIDTH, 0))) # vao entrando p tela, redesenhando o background = efeito parallax
                return list_bg
            
            # players
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30)) # nave se inicia full esquerda quase encostando no final da tela
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30)) # nave se inicia full esquerda quase encostando no final da tela
            
            # enemies
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40))) # as naves inimigas vem de forma aleatoria de fora da tela
            
   

