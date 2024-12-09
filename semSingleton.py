class DatabaseConnection:
    def __init__(self):
        print("Nova conexão com o banco de dados criada")
 
    def query(self, sql):
        print(f"Executando consulta: {sql}")
 
 
# Criando múltiplas conexões
db1 = DatabaseConnection()
db2 = DatabaseConnection()
 
db1.query("SELECT * FROM users")
db2.query("SELECT * FROM orders")