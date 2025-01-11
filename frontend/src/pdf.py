import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Função para obter os dados do inquilino via API
def get_inquilino(inquilino_id):
    response = requests.get(f'http://backend:8000/inquilinos/{get_id}')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao obter dados do inquilino: {response.status_code}")

# Função para preencher o PDF com os dados do inquilino
def fill_pdf(inquilino_data, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter

    # Preencher o PDF com os dados do inquilino
    c.drawString(100, height - 100, f"Nome: {inquilino_data['nome']}")
    c.drawString(100, height - 120, f"CPF: {inquilino_data['cpf']}")
    c.drawString(100, height - 140, f"Telefone: {inquilino_data['telefone']}")
    c.drawString(100, height - 160, f"Endereço: {inquilino_data['cidade']}, {inquilino_data['estado']}, {inquilino_data['pais']}")
    c.drawString(100, height - 180, f"Profissão: {inquilino_data['profissao']}")
    c.drawString(100, height - 200, f"Estado Civil: {inquilino_data['estado_civil']}")
    c.drawString(100, height - 220, f"Automóvel: {inquilino_data['automovel']} - {inquilino_data['modelo_auto']} - {inquilino_data['placa_auto']}")

    # Adicione mais campos conforme necessário

    c.save()

if __name__ == "__main__":
    get_id = 1  # Substitua pelo ID do inquilino desejado
    output_pdf_path = f'ficha_inquilino_{get_id}.pdf'

    try:
        inquilino_data = get_inquilino(get_id)
        fill_pdf(inquilino_data, output_pdf_path)
        print(f"PDF gerado com sucesso: {output_pdf_path}")
    except Exception as e:
        print(f"Erro: {e}")