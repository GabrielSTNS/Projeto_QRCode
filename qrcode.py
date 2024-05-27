# Já há um executável criado para utilização, mas caso prefira você pode criar seu próprio arquivo seguindo os passos abaixo:

# Para criar um arquivo executável do código você precisará ter em sua máquina a biblioteca pyinstaller (pip install pyinstaller)
# Após isso, abra o terminal do seu VSCode e utilize seguinte comando: pyinstaller --noconsole --onefile --icon=qricon.ico qrcode.py
# Não precisa utilizar --icon caso não queira utilizar o icone do qrcode
# --noconsole é utilizado para que não abra o terminal do Windows enquanto o programa esteja sendo executado. O Windows Defender pode apontar como vírus, basta permitir o arquivo.
# --onefile é utilizado para que seja criado um único arquivo executável.
# Seerão criadas duas pastas (build e dist) e um arquivo que o nome será o nome do arquivo com a extensão .spec. Ex: qrcode.spec. Você pode excluir a pasta build e o arquivo .spec, restará apenas a pasta dist onde o executável que você criou estará.

# As informações solicitadas pelo programa são:
# Link do site que o QR Code irá redirecionar
# Um nome para o QR Code, por exemplo: Meu QR Code
# Pasta onde o QR Code será salvo, por exemplo: C:\Users\gabri\Downloads\Nova pasta

from tkinter import *
import pyqrcode
import os

def gerar_qrcode():
    link = link_site.get()
    nome = nome_qrcode.get()
    pasta = caminho_pasta.get()

    # Caso o link esteja em branco, será solicitado um link válido
    if not link:
        resultado.config(text='Por favor, insira um link válido.')
        return

    # Caso o nome esteja em branco, será solicitado um nome válido para a criação do arquivo
    if not nome:
        resultado.config(text='Por favor, insira um nome válido para o arquivo.')
        return

    # Caso seja inserido algum símbolo no nome do arquivo, o programa informará que há caracteres inválidos
    if any(char in r'<>:"/\|?*' for char in nome):
        resultado.config(text='O nome do arquivo contém caracteres inválidos.')
        return
    
    # Caso o caminho da pasta esteja em branco, será solicitado um caminho válido
    if not pasta:
        resultado.config(text='Por favor, insira um caminho de pasta válido.')
        return
    
    # Verifica se a pasta existe
    if not os.path.isdir(pasta):
        resultado.config(text='O caminho da pasta não existe.')
        return

    try:
        url = pyqrcode.create(link)
        caminho_completo = os.path.join(pasta, f'{nome}.png')
        url.png(caminho_completo, scale=8)
        resultado.config(text=f'QR Code criado: {caminho_completo}')
    except Exception as e:
        resultado.config(text=f'Erro ao criar QR Code: {e}') # Caso ocorra algum erro na criação do QR Code, será informado ao usuário

janela = Tk()
janela.title('Criador de QR Codes')

# Labels
inicio = Label(janela, text='Olá, seja bem vindo! Para criar seu QR Code, insira os dados abaixo:')
inicio.grid(column=0, row=0, columnspan=2, pady=10)

link_label = Label(janela, text='Insira o link do site:')
link_label.grid(column=0, row=1, sticky=E, padx=5, pady=5)

nome_label = Label(janela, text='Informe um nome para o arquivo:')
nome_label.grid(column=0, row=2, sticky=E, padx=5, pady=5)

caminho_label = Label(janela, text='Informe o caminho da pasta:')
caminho_label.grid(column=0, row=3, sticky=E, padx=5, pady=5)

# Prompts de entrada
link_site = Entry(janela, width=40)
link_site.grid(column=1, row=1, padx=5, pady=5)

nome_qrcode = Entry(janela, width=40)
nome_qrcode.grid(column=1, row=2, padx=5, pady=5)

caminho_pasta = Entry(janela, width=40)
caminho_pasta.grid(column=1, row=3, padx=5, pady=5)

# Botão para criação do QR Code
botao = Button(janela, text='Clique aqui para criar seu QRCode.', command=gerar_qrcode)
botao.grid(column=0, row=4, columnspan=2, pady=10)

# Resultado
resultado = Label(janela, text='')
resultado.grid(column=0, row=5, columnspan=2, pady=10)

janela.mainloop()