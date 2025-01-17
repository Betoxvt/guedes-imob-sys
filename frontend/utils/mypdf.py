import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def fill_ficha(ficha_data, image_path):
    file_name = f"ficha_{str(ficha_data['id'])}_{str(ficha_data['modificado_em'])}.pdf"
    directory = './files/filled_fichas/'
    path = os.path.join(directory, file_name)
    c = canvas.Canvas(path)
    
    # Desenha a imagem de fundo
    c.drawImage(image_path, 0, 0, width=A4[0], height=A4[1])

    # Insere o texto sobre a imagem, ajustando as coordenadas
    c.drawString(150, 680, f"Nome: {ficha_data['nome']}")  # Ajuste 150 e 680
    c.drawString(150, 630, f"Endereço: {ficha_data['\ufeffapto']}") # Ajuste 150 e 630
    # ... outros campos, ajustando as coordenadas

    c.save()
    return file_name

if __name__ == '__main__':
    import csv

    with open('./files/data_test.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        chaves = next(reader)  # Lê a primeira linha (chaves)
        valores = next(reader)  # Lê a segunda linha (valores)
        dados = dict(zip(chaves, valores))
        
    print(dados)

    caminho_da_imagem = "./files/ficha_model/ficha.png"
    nome_pdf = fill_ficha(dados, caminho_da_imagem)
    print(f"PDF gerado: {nome_pdf}")


'''
# mapping image
apto = 500 , 810
nome = 939 , 810
Anual = 771 , 860
Temporário = 1089 , 863
cidade = 796 , 911
cep = 1630, 910
uf = 2076 , 911
pais = 507 , 962
tel = 1256, 960
estado_civil = 650 , 1010
profissao = 1517, 1009
rg = 761 , 1058
cpf = 1450, 1050
mae = 511, 1106
automovel = 618, 1154
modelo = 1382, 1154
placa = 510, 1205
cor = 1311, 1204
a1={n= 440 , 1375 / d= 1265 , 1375 / i= 1727 , 1375 / p= 1907 , 1375}
a2={n= 440 , 1442 / d= 1265 , 1442 / i= 1727 , 1442 / p= 1907 , 1442}
a3={n= 440 , 1509 / d= 1265 , 1509 / i= 1727 , 1509 / p= 1907 , 1509}
a4={n= 440 , 1575 / d= 1265 , 1575 / i= 1727 , 1575 / p= 1907 , 1575}
a5={n= 440 , 1642 / d= 1265 , 1642 / i= 1727 , 1642 / p= 1907 , 1642}
a6={n= 440 , 1705 / d= 1265 , 1705 / i= 1727 , 1705 / p= 1907 , 1705}
a7={n= 440 , 1770 / d= 1265 , 1770 / i= 1727 , 1770 / p= 1907 , 1770}
a8={n= 440 , 1836 / d= 1265 , 1836 / i= 1727 , 1836 / p= 1907 , 1836}
a9={n= 440 , 1902 / d= 1265 , 1902 / i= 1727 , 1902 / p= 1907 , 1902}
a0={n= 440 , 1969 / d= 1265 , 1969 / i= 1727 , 1969 / p= 1907 , 1969}
checkin = 965 , 2064 / 1112 , 2066 / 1257 , 2065
checkout = 1648, 2065 / 1800 , 2066 / 1872 , 2067
observacoes = 643 , 2167 / 374 , 2219
locatario = 378 , 2803
imob respons = 1327 , 2807
imob_fone = 1551 , 2664 / 1668 , 2959
proprietario = 847 , 3106
'''