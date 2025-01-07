import tkinter as tk

# Função para exibir uma mensagem quando o botão for clicado
def exibir_mensagem():
  print("O botão foi clicado!")

# Criar uma janela
janela = tk.Tk()
janela.title("Posicionamento com Grid")

# Adicionar um rótulo
rotulo = tk.Label(janela, text="Olá, Tkinter!")
rotulo.grid(row=0, column=0, padx=10, pady=10)  # Posicionado na primeira linha e primeira coluna

# Adicionar um botão
botao = tk.Button(janela, text="Clique Aqui", command=exibir_mensagem)
botao.grid(row=1, column=0, padx=10, pady=10)  # Posicionado na segunda linha e primeira coluna

# Ajustar o tamanho da tela
janela.geometry("300x200")
# Tela não é responsiva
janela.resizable(False, False)

# Criar um input de texto
input_texto = tk.Entry(janela)
input_texto.grid(row=2, column=0, padx=10, pady=10)

# Imprimir o texto digitado
def imprimir_texto():
  print("Texto digitado:", input_texto.get())
  # mostrar em tela
  rotulo.config(text=f"Olá, Tkinter! Texto digitado: {input_texto.get()}")

botao_imprimir = tk.Button(janela, text="Imprimir Texto", command=imprimir_texto)

botao_imprimir.grid(row=3, column=0, padx=10, pady=10)

# Executar o loop principal
janela.mainloop()

# comando para compilar como executável .exe
# pyinstaller --onefile --noconsole exemplo_tela_tkinter.py