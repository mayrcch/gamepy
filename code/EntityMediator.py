from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:
# __ usa-se para métodos privados em que só funciona dentro de uma class especifica, no caso aqui da 'verify_collision'.
    @staticmethod
    def __verify_collision_window(ent: Entity): # verificando se o inimigo atingiu o limite da tela
        if isinstance(ent, Enemy): # verificação apenas para inimigos
            if ent.rect.right < 0: # se o enemy passar da tela
                ent.health = 0 # a vida dele eh reduzida a 0
        pass
        
        
    @staticmethod
    def verify_collision(entity_list:list[Entity]): # lista das entidades: players, backgrounds, enemies etc
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)
            
    
    @staticmethod
    def verify_health(entity_list:list[Entity]):
        for ent in entity_list: # para cada entidade
            if ent.health <= 0: # se a vida for reduzida a 0
                entity_list.remove(ent) # aquela entidade será removida
       