import sqlite3

conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    genero TEXT,
    duracao INTEGER,
    diretor TEXT,
    elenco TEXT
)
''')

conn.commit()