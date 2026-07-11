"""
Testes automatizados do TaskManager.
"""

import os
import sys

# Permite importar arquivos da pasta src
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from manager import TaskManager
from task import Task


def limpar_dados(manager):
    """Limpa todas as tarefas antes dos testes."""

    manager.tarefas = []
    manager.salvar()


def test_adicionar_tarefa():

    manager = TaskManager()

    limpar_dados(manager)

    tarefa = Task(
        "Teste",
        "Descrição",
        "Alta"
    )

    manager.adicionar(tarefa)

    assert len(manager.listar()) == 1


def test_editar_tarefa():

    manager = TaskManager()

    limpar_dados(manager)

    manager.adicionar(
        Task(
            "Antiga",
            "Teste",
            "Alta"
        )
    )

    nova = Task(
        "Nova",
        "Atualizada",
        "Baixa"
    )

    manager.editar(0, nova)

    assert manager.listar()[0].titulo == "Nova"


def test_excluir_tarefa():

    manager = TaskManager()

    limpar_dados(manager)

    manager.adicionar(
        Task(
            "Excluir",
            "Teste",
            "Alta"
        )
    )

    manager.excluir(0)

    assert len(manager.listar()) == 0


def test_concluir_tarefa():

    manager = TaskManager()

    limpar_dados(manager)

    manager.adicionar(
        Task(
            "Concluir",
            "Teste",
            "Alta"
        )
    )

    manager.concluir(0)

    assert manager.listar()[0].status == "Concluída"


def test_pesquisar():

    manager = TaskManager()

    limpar_dados(manager)

    manager.adicionar(
        Task(
            "README",
            "Teste",
            "Alta"
        )
    )

    resultado = manager.pesquisar("read")

    assert len(resultado) == 1