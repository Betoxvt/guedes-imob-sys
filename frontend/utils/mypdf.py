from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def gerar_pdf_com_fundo(dados_ficha, caminho_imagem):
    nome_arquivo = f"ficha_{dados_ficha['id']}.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=letter)

    # Desenha a imagem de fundo
    c.drawImage(caminho_imagem, 0, 0, width=letter[0], height=letter[1])

    # Insere o texto sobre a imagem, ajustando as coordenadas
    c.drawString(150, 680, f"Nome: {dados_ficha['nome']}")  # Ajuste 150 e 680
    c.drawString(150, 630, f"Endereço: {dados_ficha['endereco']}") # Ajuste 150 e 630
    # ... outros campos, ajustando as coordenadas

    c.save()
    return nome_arquivo

# Exemplo de uso
dados = {'id': 1, 'nome': 'João da Silva', 'endereco': 'Rua Exemplo, 123'}
caminho_da_imagem = "ficha_escaneada.png" # Substitua pelo caminho da sua imagem
nome_pdf = gerar_pdf_com_fundo(dados, caminho_da_imagem)
print(f"PDF gerado: {nome_pdf}")