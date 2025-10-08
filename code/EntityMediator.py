from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:
# __ usa-se para métodos privados em que só funciona dentro de uma class especifica, no caso aqui da 'verify_collision'.
    @staticmethod
    def __verify_collision_window(ent: Entity): # verificando se o inimigo atingiu o limite da tela
        if isinstance(ent, Enemy): # verificação apenas para inimigos
            if ent.rect.right < 0: # se o enemy passar da tela
                ent.health = 0 # a vida dele eh reduzida a 0
                
        if isinstance(ent, PlayerShot): # verificação apenas para os tiros n passarem da tela
            if ent.rect.left >= WIN_WIDTH: # se o tiro passar da tela
                ent.health = 0
                
        if isinstance(ent, EnemyShot): # verificação apenas para inimigos
            if ent.rect.right <= 0: # se o enemy passar da tela
                ent.health = 0 # a vida dele eh reduzida a 0
        
        
    @staticmethod
    def __verify_collision_entity(ent1, ent2): # verificando as colisoes pra n ter fogo amigo, etc. Ent vai ser com o tiro da nave inimiga com a nave do player, e viceversa.
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        # tiro do inimigo no jogador:
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        # sendo elif pois n tem como mais de um cenário acontecer ao mesmo tempo. vai ser smp 1 desses quatro eventos acima.
        
        if valid_interaction: # if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                    ent1.health -= ent2.damage
                    ent2.health -= ent1.damage # vida da entidade 1 diminui de acordo com a vida da entidade 2
                    ent1.last_dmg = ent2.name # o ultimo dano causado na entidade 1 foi feito pela entidade 2, ent pontua no score
                    ent2.last_dmg = ent1.name
    
    
    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot': # se o last hit foi do player1:
            for ent in entity_list: # procura o player1 na lista de entidades
                if ent.name == 'Player1': # se encontra dá seu score:
                    ent.score += enemy.score
                    
        elif enemy.last_dmg == 'Player2Shot': # se o last hit foi do player2:
            for ent in entity_list: # procura o player2 na lista de entidades
                if ent.name == 'Player2': # se encontra dá seu score:
                    ent.score += enemy.score
                    
            
    @staticmethod
    def verify_collision(entity_list:list[Entity]): # lista das entidades: players, backgrounds, enemies etc
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1) # verificando se ta na borda da janela
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)
    
    @staticmethod
    def verify_health(entity_list:list[Entity]):
        for ent in entity_list: # para cada entidade
            if ent.health <= 0: # se a vida for reduzida a 0
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list) # qnd mata um inimigo, atualiza o score
                entity_list.remove(ent) # aquela entidade será removida
       