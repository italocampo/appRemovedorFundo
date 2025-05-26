import fitz  # PyMuPDF

# Caminho do arquivo PDF
caminho_pdf = r"C:\Users\Windows OS\OneDrive\Área de Trabalho\Faculdade\3° sem ADS\Phyton3\Phyton\conteudo\PDF.pdf"

# Abrir o arquivo PDF
doc = fitz.open(caminho_pdf)

# Escolher uma página específica
pagina = doc[1]

# Adicionar um texto na página (posicionando em x=100, y=100)
pagina.insert_text((100, 100), "Doc em pdf da CodeLine")

# Ler o texto de todas as páginas
PDF = ""
for pagina in doc:
    PDF += pagina.get_text()

# Exibir todo o texto do PDF
print(PDF)
print("\t\t\t\t[Texto adicionado com sucesso!]")

# Salvar o PDF modificado
caminho_pdf_modificado = r"C:\Users\Windows OS\OneDrive\Área de Trabalho\Faculdade\3° sem ADS\Phyton3\Phyton\conteudo\PDF_modificado.pdf"
doc.save(caminho_pdf_modificado)
