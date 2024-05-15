# NÃO ESQUEÇA DE DAR UM PIP INSTALL CUSTOMTKINTER ANTES DE APRESENTAR!

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

#Pré lista - Dicionário que armazena os produtos no estoque
estoque = {
    "Arroz": {"Quantidade": 50, "Preço": 10.99, "Categoria": "Grãos"},
    "Feijão": {"Quantidade": 40, "Preço": 8.50, "Categoria": "Grãos"},
    "Macarrão": {"Quantidade": 30, "Preço": 5.75, "Categoria": "Massas"},
    "Café": {"Quantidade": 20, "Preço": 15.25, "Categoria": "Bebidas"},
    "Leite": {"Quantidade": 25, "Preço": 3.99, "Categoria": "Laticínios"},
    "Óleo de Soja": {"Quantidade": 15, "Preço": 6.99, "Categoria": "Óleos"},
}

# Função de adicionar produto ao estoque
def adicionar_produto():
    nome = nome_entry.get()
    quantidade = int(quantidade_entry.get())
    preco = float(preco_entry.get())
    categoria = categoria_entry.get()

    # Formata o nome e a categoria para iniciar com letra maiúscula
    for i in estoque:
        nome = nome.capitalize()
        categoria = categoria.capitalize()
    
    # Verifica se o produto já existe no estoque
    if nome not in estoque:
        estoque[nome] = {"Quantidade": quantidade, "Preço": preco, "Categoria": categoria}
        messagebox.showinfo("Sucesso", f"Produto {nome} adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", f"O produto {nome} já existe no estoque!")

# Função de atualizar a quantidade de um produto no estoque
def atualizar_estoque():
    nome = nome_entry.get()
    quantidade = int(quantidade_entry.get())
    
    # Formata o nome para iniciar com letra maiúscula
    for i in estoque:
        nome = nome.capitalize()
    
    # Verifica se o produto está no estoque e atualiza a quantidade
    if nome in estoque:
        estoque[nome]["Quantidade"] += quantidade
        messagebox.showinfo("Sucesso", f"Estoque de {nome} atualizado para {estoque[nome]['Quantidade']} unidades.")
    else:
        messagebox.showerror("Erro", f"Produto {nome} não encontrado no estoque.")

# Função de listar todos os produtos no estoque
def listar_produtos():
    if estoque:
        produtos = "\n".join([f"{produto}: {info['Quantidade']} unidades, R$ {info['Preço']}, {info['Categoria']}" for produto, info in estoque.items()])
        messagebox.showinfo("Lista de Produtos", produtos)
    else:
        messagebox.showinfo("Estoque Vazio", "O estoque está vazio.")

# Função de buscar um produto específico no estoque
def buscar_produto():
    nome = nome_entry.get()
    
    # Formata o nome para iniciar com letra maiúscula
    for i in estoque:
        nome = nome.capitalize()
    
    # Verifica se o produto está no estoque e exibe suas informações
    if nome in estoque:
        info = estoque[nome]
        messagebox.showinfo("Informações do Produto", f"Informações sobre o produto {nome}:\nQuantidade: {info['Quantidade']} unidades\nPreço: R$ {info['Preço']}\nCategoria: {info['Categoria']}")
    else:
        messagebox.showerror("Produto Não Encontrado", f"Produto {nome} não encontrado no estoque.")

# Função de remover um produto do estoque
def remover_produto():
    nome = nome_entry.get()
    
    # Formata o nome para iniciar com letra maiúscula
    for i in estoque:
        nome = nome.capitalize()
    
    # Verifica se o produto está no estoque e o remove
    if nome in estoque:
        del estoque[nome]
        messagebox.showinfo("Produto Removido", f"Produto {nome} removido do estoque.")
    else:
        messagebox.showerror("Produto Não Encontrado", f"Produto {nome} não encontrado no estoque.")

# Função de deletar todo o estoque
def deletar_todo_estoque():
    global estoque
    estoque.clear()
    messagebox.showinfo("Estoque Apagado", "O estoque foi apagado.")

# Função de listar produtos com quantidade baixa (<= 10 unidades)
def produtos_em_baixa_quantidade():
    baixos = [produto for produto, info in estoque.items() if info['Quantidade'] <= 10]
    if baixos:
        messagebox.showinfo("Produtos em Baixa Quantidade", f"Produtos com quantidade baixa:\n{', '.join(baixos)}")
    else:
        messagebox.showinfo("Produtos em Baixa Quantidade", "Todos os produtos estão em quantidade satisfatória.")

# Função principal para criar a janela e os widgets
def main():
    global nome_entry, quantidade_entry, preco_entry, categoria_entry
    root = ctk.CTk()
    root.title("Gestor de Estoque")

    # Criação dos widgets (rótulos, entradas de texto e botões)
    nome_label = ctk.CTkLabel(root, text="Nome:")
    nome_entry = ctk.CTkEntry(root)

    quantidade_label = ctk.CTkLabel(root, text="Quantidade:")
    quantidade_entry = ctk.CTkEntry(root)

    preco_label = ctk.CTkLabel(root, text="Preço:")
    preco_entry = ctk.CTkEntry(root)

    categoria_label = ctk.CTkLabel(root, text="Categoria:")
    categoria_entry = ctk.CTkEntry(root)

    adicionar_button = ctk.CTkButton(root, text="Adicionar", command=adicionar_produto)
    atualizar_button = ctk.CTkButton(root, text="Atualizar Estoque", command=atualizar_estoque)
    listar_button = ctk.CTkButton(root, text="Listar Produtos", command=listar_produtos)
    buscar_button = ctk.CTkButton(root, text="Buscar Produto", command=buscar_produto)
    remover_button = ctk.CTkButton(root, text="Remover Produto", command=remover_produto)
    baixa_quantidade_button = ctk.CTkButton(root, text="Produtos em Baixa Quantidade", command=produtos_em_baixa_quantidade)
    deletar_button = ctk.CTkButton(root, text="Deletar Estoque", command=deletar_todo_estoque)

    # Empacotamento (adicionar à janela) dos widgets
    nome_label.pack()
    nome_entry.pack()

    quantidade_label.pack()
    quantidade_entry.pack()

    preco_label.pack()
    preco_entry.pack()

    categoria_label.pack()
    categoria_entry.pack()

    adicionar_button.pack(fill="x", pady=5)
    atualizar_button.pack(fill="x", pady=5)
    listar_button.pack(fill="x", pady=5)
    buscar_button.pack(fill="x", pady=5)
    remover_button.pack(fill="x", pady=5)
    baixa_quantidade_button.pack(fill="x", pady=5)
    deletar_button.pack(fill="x", pady=5)

    root.mainloop()

# Executa a função principal se este script for executado diretamente
if __name__ == "__main__":
    main()
