import sqlite3

class FilmeRepository:

    def salvar(self, filme):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO filmes (titulo, genero, duracao, diretor, elenco)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            filme.titulo,
            filme.genero,
            filme.duracao,
            filme.diretor,
            filme.elenco
        ))

        conn.commit()
        conn.close()