from model.filme import Filme
from service.filme_service import FilmeService

class FilmeController:

    def __init__(self):
        self.service = FilmeService()

    def cadastrar_filme(self):

        titulo = input('Título: ')
        genero = input('Gênero: ')
        duracao = int(input('Duração em minutos: '))
        diretor = input('Diretor: ')
        elenco = input('Elenco: ')

        filme = Filme(titulo, genero, duracao, diretor, elenco)

        self.service.cadastrar_filme(filme)