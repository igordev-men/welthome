import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect("enderecos.db")
cursor = conn.cursor()

# Criar a tabela de endereços
cursor.execute("""
CREATE TABLE IF NOT EXISTS enderecos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    endereco TEXT NOT NULL
)
""")

# Inserir alguns endereços de exemplo
enderecos_exemplo = ["Endereço 1", "Endereço 2", "Endereço 3", "Endereço 4"]

for endereco in enderecos_exemplo:
    cursor.execute("INSERT INTO enderecos (endereco) VALUES (?)", (endereco,))

# Salvar e fechar
conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
