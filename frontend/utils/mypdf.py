import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def fill_ficha(data, img, dir):
    file_name = f"ficha_{str(data['id'])}_{str(data['modificado_em'])}.pdf"
    path = os.path.join(dir, file_name)
    c = canvas.Canvas(path)
    c.drawImage(img, 0, 0, width=A4[0], height=A4[1])
    c.drawString(150, 680, f"Nome: {data['nome']}")


    c.save()
    return file_name

if __name__ == '__main__':
    import csv

    with open('./files/data_test.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        chaves = next(reader)
        valores = next(reader)
        dados = dict(zip(chaves, valores))
        
    print(dados)
    dir = './files/filled_fichas/'
    img = "./files/ficha_model/ficha.png"
    pdf = fill_ficha(dados, img, dir)
    print(f"PDF gerado: {pdf}")



apto = [500, 810]
nome = [939, 810]
anual = [771, 860]
temp = [1089, 863]
cidade = [796, 911]
cep = [1630, 910]
uf = [2076, 911]
pais = [507, 962]
tel = [1256, 960]
estado_civil = [650, 1010]
profissao = [1517, 1009]
rg = [761, 1058]
cpf = [1450, 1050]
mae = [511, 1106]
automovel = [618, 1154]
modelo = [1382, 1154]
placa = [510, 1205]
cor = [1311, 1204]
locatario = [378, 2803]
imob_respons = [1327, 2807]
proprietario = [847, 3106]

observacoes = {'l1': [643, 2167], 'l2': [374, 2219]}
imob_fone = {'ddd': [1551, 2664], 'tel': [1668, 2959]}

checkin = {'dia': [965, 2064], 'mes': [1112, 2066], 'ano': [1257, 2065]}
checkout = {'dia': [1648, 2065], 'mes': [1800, 2066], 'ano': [1872, 2067]}

a1 = {'nome': [440, 1375], 'doc': [1265, 1375], 'idade': [1727, 1375], 'parentesco': [1907, 1375]}
a2 = {'nome': [440, 1442], 'doc': [1265, 1442], 'idade': [1727, 1442], 'parentesco': [1907, 1442]}
a3 = {'nome': [440, 1509], 'doc': [1265, 1509], 'idade': [1727, 1509], 'parentesco': [1907, 1509]}
a4 = {'nome': [440, 1575], 'doc': [1265, 1575], 'idade': [1727, 1575], 'parentesco': [1907, 1575]}
a5 = {'nome': [440, 1642], 'doc': [1265, 1642], 'idade': [1727, 1642], 'parentesco': [1907, 1642]}
a6 = {'nome': [440, 1705], 'doc': [1265, 1705], 'idade': [1727, 1705], 'parentesco': [1907, 1705]}
a7 = {'nome': [440, 1770], 'doc': [1265, 1770], 'idade': [1727, 1770], 'parentesco': [1907, 1770]}
a8 = {'nome': [440, 1836], 'doc': [1265, 1836], 'idade': [1727, 1836], 'parentesco': [1907, 1836]}
a9 = {'nome': [440, 1902], 'doc': [1265, 1902], 'idade': [1727, 1902], 'parentesco': [1907, 1902]}
a0 = {'nome': [440, 1969], 'doc': [1265, 1969], 'idade': [1727, 1969], 'parentesco': [1907, 1969]}


