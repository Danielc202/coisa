class SingletonMeta(type):
    """Metaclasse para implementar o Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        print("Conexão com o banco de dados criada")

    def query(self, sql):
        print(f"Executando consulta: {sql}")


if __name__ == "__main__":
    # Criando conexões usando o Singleton
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    db1.query("SELECT * FROM users")
    db2.query("SELECT * FROM orders")

    # Verificando que ambas as conexões são a mesma instância
    print(db1 is db2)  # True