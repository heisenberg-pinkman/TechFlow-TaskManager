"""
manager.py

Responsável pelo gerenciamento das tarefas.
"""

import json
import os

from task import Task


class TaskManager:

    def __init__(self):

        self.arquivo = os.path.join("data", "tasks.json")

        self.tarefas = []

        self.carregar()

    # --------------------------------------------

    def carregar(self):
        """Carrega as tarefas do JSON."""

        if not os.path.exists(self.arquivo):
            self.tarefas = []
            return

        try:

            with open(self.arquivo, "r", encoding="utf-8") as arquivo:

                dados = json.load(arquivo)

                self.tarefas = [
                    Task.from_dict(item)
                    for item in dados
                ]

        except Exception:

            self.tarefas = []

    # --------------------------------------------

    def salvar(self):
        """Salva as tarefas."""

        with open(self.arquivo, "w", encoding="utf-8") as arquivo:

            json.dump(

                [tarefa.to_dict() for tarefa in self.tarefas],

                arquivo,

                indent=4,

                ensure_ascii=False

            )

    # --------------------------------------------

    def adicionar(self, tarefa):
        """Adiciona uma nova tarefa."""

        self.tarefas.append(tarefa)

        self.salvar()

    # --------------------------------------------

    def listar(self):
        """Retorna todas as tarefas."""

        return self.tarefas

    # --------------------------------------------

    def editar(self, indice, nova_tarefa):
        """
        Atualiza uma tarefa.
        """

        if 0 <= indice < len(self.tarefas):

            self.tarefas[indice] = nova_tarefa

            self.salvar()

            return True

        return False

    # --------------------------------------------

    def excluir(self, indice):
        """
        Remove uma tarefa.
        """

        if 0 <= indice < len(self.tarefas):

            del self.tarefas[indice]

            self.salvar()

            return True

        return False

    # --------------------------------------------

    def concluir(self, indice):
        """
        Marca uma tarefa como concluída.
        """

        if 0 <= indice < len(self.tarefas):

            self.tarefas[indice].status = "Concluída"

            self.salvar()

            return True

        return False

    # --------------------------------------------

    def pesquisar(self, texto):
        """
        Pesquisa tarefas pelo título.
        """

        texto = texto.lower()

        return [

            tarefa

            for tarefa in self.tarefas

            if texto in tarefa.titulo.lower()

        ]