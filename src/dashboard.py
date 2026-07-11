"""
dashboard.py

Tela principal do sistema TechFlow Task Manager.
"""

import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk

from manager import TaskManager
from task import Task


class Dashboard:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.manager = TaskManager()

        # Guarda o índice real da tarefa
        self.indices = []

        # Índice da tarefa em edição
        self.editando = None

        self.janela = ctk.CTk()
        self.janela.title("TechFlow Task Manager")
        self.janela.geometry("900x650")
        self.janela.resizable(False, False)

        self.criar_interface()

        self.atualizar_lista()

        self.janela.mainloop()

    # ===================================================

    def criar_interface(self):

        titulo = ctk.CTkLabel(
            self.janela,
            text="TechFlow Task Manager",
            font=("Arial", 28, "bold")
        )

        titulo.pack(pady=15)

        # ---------------- FORMULÁRIO ----------------

        frame = ctk.CTkFrame(self.janela)

        frame.pack(fill="x", padx=20)

        ctk.CTkLabel(frame, text="Título").grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.entry_titulo = ctk.CTkEntry(
            frame,
            width=300
        )

        self.entry_titulo.grid(row=0, column=1)

        ctk.CTkLabel(
            frame,
            text="Descrição"
        ).grid(row=1, column=0)

        self.entry_descricao = ctk.CTkEntry(
            frame,
            width=300
        )

        self.entry_descricao.grid(row=1, column=1)

        ctk.CTkLabel(
            frame,
            text="Prioridade"
        ).grid(
            row=2,
            column=0,
            pady=10
        )

        self.combo = ctk.CTkComboBox(
            frame,
            values=[
                "Alta",
                "Média",
                "Baixa"
            ],
            width=170
        )

        self.combo.set("Média")

        self.combo.grid(row=2, column=1)

        self.bt_salvar = ctk.CTkButton(
            frame,
            text="Adicionar Tarefa",
            command=self.adicionar_tarefa
        )

        self.bt_salvar.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=15
        )

        # ---------------- PESQUISA ----------------

        self.entry_pesquisa = ctk.CTkEntry(
            self.janela,
            placeholder_text="Pesquisar..."
        )

        self.entry_pesquisa.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.entry_pesquisa.bind(
            "<KeyRelease>",
            self.pesquisar
        )

        # ---------------- LISTA ----------------

        self.lista = tk.Listbox(
            self.janela,
            height=15,
            font=("Arial", 11)
        )

        self.lista.pack(
            fill="both",
            expand=True,
            padx=20
        )

        # ---------------- BOTÕES ----------------

        botoes = ctk.CTkFrame(self.janela)

        botoes.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            botoes,
            text="Editar",
            command=self.editar_tarefa
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            botoes,
            text="Excluir",
            command=self.excluir_tarefa
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            botoes,
            text="Concluir",
            command=self.concluir_tarefa
        ).pack(
            side="left",
            padx=10
        )

        # ---------------- STATUS ----------------

        self.lbl_status = ctk.CTkLabel(
            self.janela,
            text=""
        )

        self.lbl_status.pack(pady=10)

    # ===================================================

    def atualizar_lista(self, tarefas=None):

        self.lista.delete(0, tk.END)

        self.indices.clear()

        if tarefas is None:

            tarefas = list(
                enumerate(
                    self.manager.listar()
                )
            )

        pendentes = 0
        concluidas = 0

        for indice, tarefa in tarefas:

            self.indices.append(indice)

            self.lista.insert(

                tk.END,

                f"{tarefa.titulo} | {tarefa.prioridade} | {tarefa.status}"

            )

            if tarefa.status == "Pendente":
                pendentes += 1
            else:
                concluidas += 1

        self.lbl_status.configure(

            text=f"Total: {len(tarefas)} | Pendentes: {pendentes} | Concluídas: {concluidas}"

        )

    # ===================================================

    def limpar_campos(self):
        """Limpa o formulário."""

        self.entry_titulo.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.combo.set("Média")

        self.editando = None

        self.bt_salvar.configure(
            text="Adicionar Tarefa"
        )

    # ===================================================

    def adicionar_tarefa(self):
        """Adiciona uma nova tarefa ou salva uma edição."""

        titulo = self.entry_titulo.get().strip()
        descricao = self.entry_descricao.get().strip()
        prioridade = self.combo.get()

        if not titulo:

            messagebox.showwarning(
                "Aviso",
                "Informe um título."
            )

            return

        nova = Task(
            titulo,
            descricao,
            prioridade
        )

        # EDITAR

        if self.editando is not None:

            antiga = self.manager.listar()[self.editando]

            nova.status = antiga.status
            nova.data_criacao = antiga.data_criacao

            self.manager.editar(
                self.editando,
                nova
            )

            messagebox.showinfo(
                "Sucesso",
                "Tarefa atualizada!"
            )

        # ADICIONAR

        else:

            self.manager.adicionar(nova)

            messagebox.showinfo(
                "Sucesso",
                "Tarefa adicionada!"
            )

        self.limpar_campos()

        self.atualizar_lista()

    # ===================================================

    def editar_tarefa(self):
        """Carrega uma tarefa para edição."""

        selecionado = self.lista.curselection()

        if not selecionado:

            messagebox.showwarning(
                "Aviso",
                "Selecione uma tarefa."
            )

            return

        indice = self.indices[
            selecionado[0]
        ]

        tarefa = self.manager.listar()[indice]

        self.entry_titulo.delete(0, tk.END)
        self.entry_titulo.insert(
            0,
            tarefa.titulo
        )

        self.entry_descricao.delete(0, tk.END)
        self.entry_descricao.insert(
            0,
            tarefa.descricao
        )

        self.combo.set(
            tarefa.prioridade
        )

        self.editando = indice

        self.bt_salvar.configure(
            text="Salvar Alterações"
        )

    # ===================================================

    def excluir_tarefa(self):
        """Exclui uma tarefa."""

        selecionado = self.lista.curselection()

        if not selecionado:

            messagebox.showwarning(
                "Aviso",
                "Selecione uma tarefa."
            )

            return

        indice = self.indices[
            selecionado[0]
        ]

        confirmar = messagebox.askyesno(

            "Excluir",

            "Deseja realmente excluir esta tarefa?"

        )

        if confirmar:

            self.manager.excluir(indice)

            self.atualizar_lista()

    # ===================================================

    def concluir_tarefa(self):
        """Conclui uma tarefa."""

        selecionado = self.lista.curselection()

        if not selecionado:

            messagebox.showwarning(
                "Aviso",
                "Selecione uma tarefa."
            )

            return

        indice = self.indices[
            selecionado[0]
        ]

        self.manager.concluir(indice)

        self.atualizar_lista()

        messagebox.showinfo(

            "Sucesso",

            "Tarefa concluída."

        )

    # ===================================================

    def pesquisar(self, event=None):
        """Pesquisa pelo título."""

        texto = self.entry_pesquisa.get().lower().strip()

        if not texto:

            self.atualizar_lista()

            return

        resultado = []

        for indice, tarefa in enumerate(

            self.manager.listar()

        ):

            if texto in tarefa.titulo.lower():

                resultado.append(

                    (indice, tarefa)

                )

        self.atualizar_lista(resultado)