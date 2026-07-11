# TechFlow Task Manager

## Descrição

O TechFlow Task Manager é um sistema de gerenciamento de tarefas desenvolvido em Python como parte da disciplina de Engenharia de Software.

O projeto simula o desenvolvimento de um software utilizando metodologias ágeis e boas práticas de Engenharia de Software, incluindo controle de versão com GitHub, gerenciamento de tarefas por Kanban, testes automatizados com Pytest e integração contínua utilizando GitHub Actions.

---

## Objetivo

Desenvolver um sistema simples para gerenciamento de tarefas que permita:

- Login de usuário;
- Cadastro de tarefas;
- Edição de tarefas;
- Exclusão de tarefas;
- Conclusão de tarefas;
- Pesquisa por título;
- Armazenamento em arquivo JSON.

---

## Tecnologias Utilizadas

- Python 3.13
- CustomTkinter
- JSON
- Pytest
- Git
- GitHub
- GitHub Actions

---

## Estrutura do Projeto

```
TechFlow-TaskManager
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── data/
│   ├── users.json
│   └── tasks.json
│
├── docs/
│
├── src/
│   ├── main.py
│   ├── login.py
│   ├── dashboard.py
│   ├── manager.py
│   └── task.py
│
├── tests/
│   └── test_manager.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Metodologia Ágil

O projeto foi desenvolvido utilizando a metodologia Kanban.

Durante o desenvolvimento foi utilizado um quadro no GitHub Projects contendo as colunas:

- A Fazer
- Em Progresso
- Concluído

Esse método permitiu organizar as atividades, acompanhar o progresso do projeto e controlar as mudanças solicitadas durante o desenvolvimento.

---

## Controle de Qualidade

O projeto utiliza testes automatizados com Pytest.

Também foi configurado um pipeline de Integração Contínua utilizando GitHub Actions, responsável por executar automaticamente os testes a cada Push ou Pull Request realizado no repositório.

---

## Mudança de Escopo

Durante o desenvolvimento, o cliente solicitou uma nova funcionalidade:

**Filtro de tarefas por prioridade.**

Essa alteração foi registrada no quadro Kanban, implementada no fluxo de desenvolvimento e documentada neste projeto, demonstrando a flexibilidade proporcionada pelas metodologias ágeis.

---

## Como Executar

### Clonar o repositório

```bash
git clone https://github.com/heisenberg-pinkman/TechFlow-TaskManager.git
```

### Entrar na pasta

```bash
cd TechFlow-TaskManager
```

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Windows

```bash
venv\Scripts\activate
```

Git Bash

```bash
source venv/Scripts/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar o sistema

```bash
python src/main.py
```

---

## Testes

Para executar os testes automatizados:

```bash
pytest
```

---

## Autor

Projeto desenvolvido por **Vitor Nogueira** para a disciplina de Engenharia de Software.