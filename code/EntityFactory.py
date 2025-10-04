from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name:str, position=(0,0)): # os background smp vao ser instanciados em esq0, top0
        match entity_name:
            case 'Level1Bg':
                list_bg = [] # tds os backgrounds dentro dessa lista
                for i in range(7): # p/ cada arq de background da fase1 passando
                    list_bg.append(Background(f'Level1Bg{i}', position=(0,0))) # começa no inicio da tela e vai diminuindo
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0))) # vao entrando p tela, redesenhando o background = efeito parallax

                return list_bg
                