import sqlite3


class DBProxy:
    def __init__(self, db_name:str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS dados(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   date TEXT NOT NULL)
                                '''
                                )
        # ^ se a tabela n existir, cria chamada 'dados' e adiciona seus atributos.
        
    def save(self, score_dict: dict): # salvar no banco de dados
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict) # INSERIR dados
        self.connection.commit() # efetiva os dados salvos

    def retrieve_top10(self) -> list: # ter um score de top 10
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall() # SELECIONA *(tudo) em ORDEM limitado em 10

    def close(self): # fecha a conexao
        return self.connection.close()    
        