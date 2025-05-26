import sys
import os
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QVBoxLayout,
    QApplication, QLineEdit, QFileDialog, QSpacerItem, QSizePolicy, QHBoxLayout
)
from PyQt5.QtGui import QFont, QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt
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
        texto_status.setText(f"Fundo removido com sucesso.\nImagem salva em: {caminho_saida}")

    except Exception as erro:
        texto_status.setText(f"Erro ao remover fundo:\n{str(erro)}")

def criar_logo_arredondada(caminho_imagem, tamanho=60):
    pixmap_original = QPixmap(caminho_imagem).scaled(tamanho, tamanho, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    mask = QPixmap(tamanho, tamanho)
    mask.fill(Qt.transparent)

    painter = QPainter(mask)
    painter.setRenderHint(QPainter.Antialiasing)
    path = QPainterPath()
    path.addEllipse(0, 0, tamanho, tamanho)
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap_original)
    painter.end()

    return mask

aplicativo = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle('Removedor de Fundo de Imagens')
janela.setGeometry(250, 250, 600, 350)

# Estilo visual
estilo_css = """
    QWidget {
        background-color: #ffffff;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 14px;
        color: #333;
    }

    QLabel {
        margin-bottom: 6px;
        font-weight: 500;
    }

    QLineEdit {
        padding: 10px;
        border: 1px solid #bbb;
        border-radius: 8px;
        background-color: #f7f7f7;
    }

    QLineEdit:focus {
        border: 1px solid #444;
        background-color: #ffffff;
    }

    QPushButton {
        background-color: #2c3e50;
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 600;
    }

    QPushButton:hover {
        background-color: #1a252f;
    }

    QPushButton:pressed {
        background-color: #121a21;
    }

    QPushButton:disabled {
        background-color: #cccccc;
        color: #666666;
    }
"""
aplicativo.setStyleSheet(estilo_css)

# Logo com nome (usando imagem imgCodeLine.jpg)
caminho_logo = "imgCodeLine.jpg"  # sua imagem da logo
logo_pixmap = criar_logo_arredondada(caminho_logo, tamanho=60)

logo_label = QLabel()
logo_label.setPixmap(logo_pixmap)
logo_label.setFixedSize(60, 60)

texto_logo = QLabel("Codeline")
texto_logo.setFont(QFont("Segoe UI", 20, QFont.Bold))
texto_logo.setStyleSheet("color: #2c3e50; margin-left: 10px;")

logo_layout = QHBoxLayout()
logo_layout.addStretch()
logo_layout.addWidget(logo_label)
logo_layout.addWidget(texto_logo)
logo_layout.addStretch()

# Outros elementos da interface
texto_descricao = QLabel("Selecione uma imagem do seu computador para remover o fundo automaticamente.")
texto_status = QLabel("Pronto para iniciar.")
campo_caminho = QLineEdit()
campo_caminho.setPlaceholderText("Caminho da imagem selecionada...")

botao_buscar = QPushButton('Buscar Imagem')
botao_buscar.clicked.connect(selecionar_imagem)

botao_remover = QPushButton('Remover Fundo')
botao_remover.clicked.connect(remover_fundo)

rodape = QLabel("© 2025 Codeline. Todos os direitos reservados.")
rodape.setStyleSheet("font-size: 12px; color: #888; margin-top: 20px;")

# Layout principal
layout = QVBoxLayout()
layout.setSpacing(12)
layout.addLayout(logo_layout)
layout.addWidget(texto_descricao)
layout.addWidget(campo_caminho)
layout.addWidget(botao_buscar)
layout.addWidget(botao_remover)
layout.addWidget(texto_status)
layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
layout.addWidget(rodape)

janela.setLayout(layout)
janela.show()

sys.exit(aplicativo.exec_())
