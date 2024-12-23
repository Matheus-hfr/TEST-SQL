Características da biblioteca  SQLite3 

A biblioteca fornece uma API para: 

Criar e gerenciar conexões: Comunicação entre o programa Python e o banco de dados SQLite. 

Executar consultas SQL: Permite executar comandos SQL para criar tabelas, inserir, atualizar, consultar e excluir dados. 

Gerenciar transações: Permite garantir que as operações sejam realizadas com consistência, usando métodos como commit() e rollback(). 

Usar cursores: O cursor é um objeto intermediário que executa consultas SQL e manipula os resultados. 

 

 

 

Arquivo: db_connection.py 

Este arquivo contém funções que abstraem operações com um banco de dados SQLite. Ele permite criar a conexão, executar consultas e realizar operações como inserir, buscar, atualizar e deletar dados. 

Função create_connection 

Cria uma conexão com o banco de dados SQLite. 

Parâmetros: 

db_file: Caminho para o arquivo do banco de dados. Caso o arquivo não exista, ele será criado. 

Retorno: 

Um objeto de conexão SQLite ou None em caso de erro. 

 

Código: 

def create_connection(db_file): 
    try: 
        connection = sqlite3.connect(db_file) 
        print(f'Connection established to the database: {db_file}') 
    except Error as e: 
        print(f'Error connection to the database: {e}') 
        connection = None 
    return connection 
 

Exemplo de uso: 

connection = create_connection("educational_system.db") 

 

 

Função execute_query 

Executa uma consulta SQL simples, como criar uma tabela. 

Parâmetros: 

connection: Objeto de conexão SQLite. 

query: A consulta SQL a ser executada. 

 

 

Código: 

def execute_query(connection, query): 
    try: 
        cursor = connection.cursor() 
        cursor.execute(query) 
        connection.commit() 
        print('Query executed successfully') 
    except Error as e: 
        print(f'Error executing query: {e}') 

 

Exemplo de uso: 

query = """ 
CREATE TABLE IF NOT EXISTS students ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, 
    age INTEGER 
); 
""" 
execute_query(connection, query) 

 

Função insert_data 

Insere dados em uma tabela usando uma consulta SQL parametrizada. 

Parâmetros: 

connection: Objeto de conexão SQLite. 

query: Consulta SQL de inserção. 

data: Tupla com os valores a serem inseridos. 

Código: 

def insert_data(connection, query, data): 

 try: 

  cursor = connection.cursor() 

  cursor.execute(query, data)  

  connection.commit() 

 except Error as e: 

  print(f'Error inserting data: {e}') 

 

Exemplo de uso: 

insert_query = "INSERT INTO students (name, age) VALUES (?, ?);" 
data = ("John Doe", 20) 
insert_data(connection, insert_query, data) 

 

 

Função fetch_data 

Busca dados no banco de dados usando uma consulta SQL. 

Parâmetros: 

connection: Objeto de conexão SQLite. 

query: Consulta SQL para buscar dados. 

Retorno: 

Uma lista de tuplas contendo as linhas retornadas. 

Código: 

def fetch_data(connection, query): 

    try: 

        cursor = connection.cursor() 

        cursor.execute(query) 

        rows = cursor.fetchall() 

        print('Data retrieved successfully.') 

        return rows 

    except Error as e: 

        print(f'Error retrieving data: {e}') 

        return [] 

Exemplo de uso: 

fetch_query = "SELECT * FROM students;” 

students = fetch_data(connection, fetch_query) 

Função update_data 

Atualiza dados em uma tabela usando uma consulta SQL parametrizada. 

Parâmetros: 

connection: Objeto de conexão SQLite. 

query: Consulta SQL de atualização. 

data: Tupla com os novos valores. 

Código: 

def update_data(connection, query, data): 

    try: 

        cursor = connection.cursor() 

        cursor.execute(query, data) 

        connection.commit() 

        print("Data updated successfully") 

    except Error as e: 

        print(f"Error updating data: {e}") 

Exemplo de uso: 

update_query = "UPDATE students SET age = ? WHERE name = ?"  

data = (25, "John Doe") 

update_data(connection, update_query, data) 

Função delete_data 

Remove dados de uma tabela usando uma consulta SQL parametrizada. 

Parâmetros: 

connection: Objeto de conexão SQLite. 

query: Consulta SQL de exclusão. 

data: Tupla com os critérios de exclusão. 

Código: 

def delete_data(connection, query, data): 

    try: 

        cursor = connection.cursor() 

        cursor.execute(query, data) 

        connection.commit() 

        print("Data deleted successfully.") 

    except Error as e: 

        print(f"Error deleting data: {e}") 

Exemplo de uso: 

delete_query = "DELETE FROM students WHERE name = ?" 

data = ("John Doe",) 

delete_data(connection, delete_query, data) 

Arquivo: main.py 

O main.py integra as funções de db_connection.py para criar tabelas, inserir, buscar, atualizar e excluir dados no banco de dados. 

 

Fluxo Geral 

Criação da Conexão: 

Cria a conexão com o banco usando create_connection. 

Criação da Tabela: 

Cria a tabela Students se ela ainda não existir. 

Inserção de Dados: 

Insere múltiplos registros na tabela. 

Leitura e Exibição dos Dados: 

Busca e exibe todos os registros da tabela. 

Atualização de Dados: 

Atualiza a idade de um estudante específico. 

Exclusão de Dados: 

Remove um estudante com base no nome. 
