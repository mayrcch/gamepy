import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size = (600, 480))
print('Setup End')

print('Loop Start')
# para a janela se manter aberta
while True:
    # checando tds os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fechar a janela
            quit()  # end pygame