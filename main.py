import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

estoque = {
    "arroz": {"Quantidade": 50, "Preço": 10.99, "Categoria": "Grãos"},
    "Feijão": {"Quantidade": 40, "Preço": 8.50, "Categoria": "Grãos"},
    "Macarrão": {"Quantidade": 30, "Preço": 5.75, "Categoria": "Massas"},
    "Café": {"Quantidade": 20, "Preço": 15.25, "Categoria": "Bebidas"},
    "Leite": {"Quantidade": 25, "Preço": 3.99, "Categoria": "Laticínios"},
    "Óleo de Soja": {"Quantidade": 15, "Preço": 6.99, "Categoria": "Óleos"},

}


def adicionar_produto():
    nome = nome_entry.get()
    quantidade = int(quantidade_entry.get())
    preco = float(preco_entry.get())
    categoria = categoria_entry.get()

    for i in estoque:
        nome = nome.capitalize()
    
    if nome not in estoque:
        estoque[nome] = {"Quantidade": quantidade, "Preço": preco, "Categoria": categoria}
        messagebox.showinfo("Sucesso", f"Produto {nome} adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", f"O produto {nome} já existe no estoque!")

def atualizar_estoque():
    nome = nome_entry.get()
    quantidade = int(quantidade_entry.get())
    
    if nome in estoque:
        estoque[nome]["Quantidade"] += quantidade
        messagebox.showinfo("Sucesso", f"Estoque de {nome} atualizado para {estoque[nome]['Quantidade']} unidades.")
    else:
        messagebox.showerror("Erro", f"Produto {nome} não encontrado no estoque.")

def listar_produtos():
    if estoque:
        produtos = "\n".join([f"{produto}: {info['Quantidade']} unidades, R$ {info['Preço']}, {info['Categoria']}" for produto, info in estoque.items()])
        messagebox.showinfo("Lista de Produtos", produtos)
    else:
        messagebox.showinfo("Estoque Vazio", "O estoque está vazio.")

def buscar_produto():
    nome = nome_entry.get()
    if nome in estoque:
        info = estoque[nome]
        messagebox.showinfo("Informações do Produto", f"Informações sobre o produto {nome}:\nQuantidade: {info['Quantidade']} unidades\nPreço: R$ {info['Preço']}\nCategoria: {info['Categoria']}")
    else:
        messagebox.showerror("Produto Não Encontrado", f"Produto {nome} não encontrado no estoque.")

def remover_produto():
    nome = nome_entry.get()
    if nome in estoque:
        del estoque[nome]
        messagebox.showinfo("Produto Removido", f"Produto {nome} removido do estoque.")
    else:
        messagebox.showerror("Produto Não Encontrado", f"Produto {nome} não encontrado no estoque.")

def produtos_em_baixa_quantidade():
    baixos = [produto for produto, info in estoque.items() if info['Quantidade'] <= 5]
    if baixos:
        messagebox.showinfo("Produtos em Baixa Quantidade", f"Produtos com quantidade baixa:\n{', '.join(baixos)}")
    else:
        messagebox.showinfo("Produtos em Baixa Quantidade", "Todos os produtos estão em quantidade satisfatória.")

def main():
    global nome_entry, quantidade_entry, preco_entry, categoria_entry
    root = ctk.CTk()
    root.title("Gestor de Estoque")

    # Definição dos Widgets
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

    # Empacotamento dos Widgets
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

    root.mainloop()

if __name__ == "__main__":
    main()
