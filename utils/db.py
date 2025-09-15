import sqlite3

def get_connection():
    return sqlite3.connect("data/escola.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Estudantes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
	    nota1 FLOAT,
            nota2 FLOAT
        )                   
    """)

    # Documentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data_upload TEXT
        )
    """)    
    conn.commit()
    conn.close()