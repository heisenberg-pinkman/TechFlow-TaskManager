"""
login.py

Tela de Login do sistema TechFlow Task Manager.
"""

import json
import os
import customtkinter as ctk
from tkinter import messagebox

from dashboard import Dashboard


class LoginWindow:

    def __init__(self):

        # Configura a aparência do sistema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Cria a janela principal
        self.janela = ctk.CTk()

        self.janela.title("TechFlow Task Manager")
        self.janela.geometry("500x420")
        self.janela.resizable(False, False)

        self.centralizar()
        self.criar_componentes()

        self.janela.mainloop()

    # ----------------------------------------------------

    def centralizar(self):
        """Centraliza a janela na tela."""

        largura = 500
        altura = 420

        largura_monitor = self.janela.winfo_screenwidth()
        altura_monitor = self.janela.winfo_screenheight()

        x = int((largura_monitor - largura) / 2)
        y = int((altura_monitor - altura) / 2)

        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")

    # ----------------------------------------------------

    def criar_componentes(self):
        """Cria todos os componentes da tela."""

        titulo = ctk.CTkLabel(
            self.janela,
            text="TechFlow Task Manager",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=35)

        subtitulo = ctk.CTkLabel(
            self.janela,
            text="Sistema de Gerenciamento de Tarefas"
        )
        subtitulo.pack(pady=5)

        self.usuario = ctk.CTkEntry(
            self.janela,
            placeholder_text="Usuário",
            width=300
        )
        self.usuario.pack(pady=20)

        self.senha = ctk.CTkEntry(
            self.janela,
            placeholder_text="Senha",
            show="*",
            width=300
        )
        self.senha.pack()

        botao = ctk.CTkButton(
            self.janela,
            text="Entrar",
            width=300,
            command=self.login
        )
        botao.pack(pady=30)

    # ----------------------------------------------------

    def login(self):
        """Valida o usuário e a senha."""

        usuario = self.usuario.get()
        senha = self.senha.get()

        caminho = os.path.join("data", "users.json")

        with open(caminho, "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)

        for user in usuarios:

            if (
                user["usuario"] == usuario
                and user["senha"] == senha
            ):

                messagebox.showinfo(
                    "Sucesso",
                    "Login realizado com sucesso!"
                )

                # Fecha a tela de login
                self.janela.destroy()

                # Abre o Dashboard
                Dashboard()

                return

        # Caso nenhum usuário seja encontrado
        messagebox.showerror(
            "Erro",
            "Usuário ou senha inválidos."
        )