import tkinter as tk

# função de tradução para morse
def codigo_morse(codificar):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....", "..",".---","-.-",".-..","--",
             "-.","---",".--.","- -.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    alfabeto='abcdefghijklmnopqrstuvwxyz'
    for codigo in codificar:
        indice=alfabeto.find(codigo)
        if indice>-1:
            codificar=codificar.replace(codigo,morse[indice])#parâmetro passado para "replace" é a lista de string em morse
    return codificar

# função de evento do botão
def traduzir():
    texto = entrada.get() #obtém o texto digitado pelo usuário
    codigo = codigo_morse(texto.lower()) #traduz o texto para morse
    saida.config(text=codigo) #exibe o código morse na interface

# cria a janela
janela = tk.Tk()
janela.title("Tradutor Morse")

# cria o campo de entrada de texto
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=10)

# cria o botão de tradução
botao = tk.Button(janela, text="Traduzir", command=traduzir)
botao.pack()

# cria o campo de saída de texto
saida = tk.Label(janela, text="")
saida.pack(pady=10)

# inicia a interface gráfica
janela.mainloop()
