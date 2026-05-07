# Rede de Cinemas

Projeto desenvolvido para a disciplina de Engenharia de Software com foco na aplicação de UML, arquitetura em camadas e persistência de dados utilizando SQLite.

---

# Informações da Atividade

**Atividade realizada em sala**  
**Aluno:** Mateus Graçadio Coelho  
**RA:** 25000217

---

# Objetivo

O sistema tem como objetivo auxiliar no gerenciamento de uma rede de cinemas, permitindo o controle de filmes, sessões e público.

---

# Caso de Uso Implementado

## Cadastro de Filmes

A implementação realizada permite:

- Cadastrar filmes
- Informar título, gênero, duração, diretor e elenco
- Validar duração do filme
- Persistir os dados em banco SQLite

---

# Arquitetura Utilizada

O projeto foi desenvolvido utilizando:

- MVC (Model, View e Controller)
- Service Layer
- Repository Pattern
- SQLite

---

# 📂 Estrutura do Projeto

```text
src/
├── controller/
├── service/
├── repository/
├── model/
├── database/
└── main.py
```

---

# 🗄️ Banco de Dados

O sistema utiliza SQLite para persistência dos dados.

Tabela implementada:

- filmes

---

# ▶️ Execução do Projeto

Execute o arquivo principal:

```bash
python main.py
```

---

# 🧩 Diagramas UML

O projeto contém:

- Diagrama de Casos de Uso
- Diagrama de Classes
- Diagramas de Atividade
- Diagramas de Sequência

---

# 👨‍💻 Tecnologias Utilizadas

- Python
- SQLite
- PlantUML
- GitHub
