import tkinter as tk
from tkinter import messagebox

estoque = {}

def adicionar_produto():
    global nome_entry, quantidade_entry, preco_entry, categoria_entry
    nome = nome_entry.get()
    quantidade = int(quantidade_entry.get())
    preco = float(preco_entry.get())
    categoria = categoria_entry.get()
    
    if nome not in estoque:
        estoque[nome] = {"Quantidade": quantidade, "Preço": preco, "Categoria": categoria}
        messagebox.showinfo("Sucesso", f"Produto {nome} adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", f"O produto {nome} já existe no estoque!")

def atualizar_estoque():
    global nome_entry, quantidade_entry
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
    global nome_entry
    nome = nome_entry.get()
    if nome in estoque:
        info = estoque[nome]
        messagebox.showinfo("Informações do Produto", f"Informações sobre o produto {nome}:\nQuantidade: {info['Quantidade']} unidades\nPreço: R$ {info['Preço']}\nCategoria: {info['Categoria']}")
    else:
        messagebox.showerror("Produto Não Encontrado", f"Produto {nome} não encontrado no estoque.")

def remover_produto():
    global nome_entry
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
    root = tk.Tk()
    root.title("Gestor de Estoque")

    # Definição dos Widgets
    nome_label = tk.Label(root, text="Nome:")
    nome_entry = tk.Entry(root)

    quantidade_label = tk.Label(root, text="Quantidade:")
    quantidade_entry = tk.Entry(root)

    preco_label = tk.Label(root, text="Preço:")
    preco_entry = tk.Entry(root)

    categoria_label = tk.Label(root, text="Categoria:")
    categoria_entry = tk.Entry(root)

    adicionar_button = tk.Button(root, text="Adicionar", command=adicionar_produto)
    atualizar_button = tk.Button(root, text="Atualizar Estoque", command=atualizar_estoque)
    listar_button = tk.Button(root, text="Listar Produtos", command=listar_produtos)
    buscar_button = tk.Button(root, text="Buscar Produto", command=buscar_produto)
    remover_button = tk.Button(root, text="Remover Produto", command=remover_produto)
    baixa_quantidade_button = tk.Button(root, text="Produtos em Baixa Quantidade", command=produtos_em_baixa_quantidade)

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
