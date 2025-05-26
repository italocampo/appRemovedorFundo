import sys
import os
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QVBoxLayout,
    QApplication, QLineEdit, QFileDialog
)
from rembg import remove
from PIL import Image
import io

def selecionar_imagem():
    caminho_arquivo, _ = QFileDialog.getOpenFileName(
        janela,
        "Selecione uma imagem",
        "",
        "Imagens (*.png *.jpg *.jpeg)"
    )

    if caminho_arquivo:
        campo_caminho.setText(caminho_arquivo)
        texto_status.setText("Imagem selecionada com sucesso.")

def remover_fundo():
    caminho_imagem = campo_caminho.text()

    if not caminho_imagem:
        texto_status.setText("Por favor, selecione uma imagem primeiro.")
        return

    try:
        with open(caminho_imagem, 'rb') as arquivo:
            imagem_bytes = arquivo.read()
            imagem_tratada = remove(imagem_bytes)

        imagem_pronta = Image.open(io.BytesIO(imagem_tratada))

        nome_arquivo = os.path.basename(caminho_imagem)
        nome_saida = os.path.splitext(nome_arquivo)[0] + "_sem_fundo.png"
        caminho_saida = os.path.join(os.path.dirname(caminho_imagem), nome_saida)

        imagem_pronta.save(caminho_saida)
        texto_status.setText(f"Fundo removido com sucesso. Imagem salva em: {caminho_saida}")

    except Exception as erro:
        texto_status.setText(f"Erro ao remover fundo: {str(erro)}")

aplicativo = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle('Removedor de Fundo de Imagens')
janela.setGeometry(250, 250, 600, 300)

estilo_css = """
    QWidget {
        background-color: #f4f4f4;
        font-family: Arial;
        font-size: 14px;
        color: #222;
    }

    QLabel {
        margin-bottom: 10px;
    }

    QLineEdit {
        padding: 8px;
        border: 1px solid #bbb;
        border-radius: 6px;
    }

    QPushButton {
        background-color: #0066cc;
        color: #fff;
        border: none;
        padding: 10px;
        border-radius: 6px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #004c99;
    }
"""

aplicativo.setStyleSheet(estilo_css)

texto_descricao = QLabel("Este programa permite selecionar uma imagem e remover o fundo automaticamente.")
texto_status = QLabel("Pronto para iniciar.")
campo_caminho = QLineEdit()
campo_caminho.setPlaceholderText("Caminho da imagem selecionada...")

botao_buscar = QPushButton('Buscar Imagem')
botao_buscar.clicked.connect(selecionar_imagem)

botao_remover = QPushButton('Remover Fundo')
botao_remover.clicked.connect(remover_fundo)

layout = QVBoxLayout()
layout.addWidget(texto_descricao)
layout.addWidget(texto_status)
layout.addWidget(campo_caminho)
layout.addWidget(botao_buscar)
layout.addWidget(botao_remover)

janela.setLayout(layout)
janela.show()

sys.exit(aplicativo.exec_())
