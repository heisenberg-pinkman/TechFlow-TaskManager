"""
Arquivo: task.py

Responsável por representar uma tarefa do sistema.
Cada objeto criado será uma tarefa cadastrada pelo usuário.
"""

from datetime import datetime


class Task:
    """
    Classe que representa uma tarefa.

    Armazena todas as informações necessárias para o gerenciamento.
    """

    def __init__(self, titulo, descricao, prioridade):
        """
        Construtor da classe.

        Args:
            titulo (str): Nome da tarefa.
            descricao (str): Descrição da tarefa.
            prioridade (str): Alta, Média ou Baixa.
        """

        # Título da tarefa
        self.titulo = titulo

        # Descrição da tarefa
        self.descricao = descricao

        # Prioridade da tarefa
        self.prioridade = prioridade

        # Toda tarefa começa como pendente
        self.status = "Pendente"

        # Guarda a data e hora da criação
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")

    def to_dict(self):
        """
        Converte o objeto Task em um dicionário.

        Isso permite salvar os dados facilmente em JSON.
        """

        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status,
            "data_criacao": self.data_criacao
        }

    @classmethod
    def from_dict(cls, dados):
        """
        Cria uma Task a partir de um dicionário.

        Utilizado quando carregamos informações do arquivo JSON.
        """

        tarefa = cls(
            dados["titulo"],
            dados["descricao"],
            dados["prioridade"]
        )

        tarefa.status = dados["status"]
        tarefa.data_criacao = dados["data_criacao"]

        return tarefa

    def __str__(self):
        """
        Define como a tarefa será exibida ao imprimir o objeto.
        """

        return (
            f"Título: {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Prioridade: {self.prioridade}\n"
            f"Status: {self.status}\n"
            f"Criada em: {self.data_criacao}"
        )