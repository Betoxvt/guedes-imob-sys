import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime

## Descobrir as medidas e coordenadas corretas
## Minha medidas estão em px, (0,0) é top-left

def fill_ficha(data: dict[str, str], img: str, dir: str):
    file_name = f"ficha_{str(data['id'])}_{str(data['modificado_em'])}___{datetime.now()}.pdf"
    path = os.path.join(dir, file_name)
    c = canvas.Canvas(path)
    # canvas.setFont("Helvetica", 12)
    c.drawImage(img, 0, 0, width=A4[0], height=A4[1])
    s: dict[int, int] = {
        "apto":         [117, 193],
        "nome":         [217, 193],
        "cidade":       [187, 218],
        "cep":          [379, 218],
        "uf":           [480, 218],
        "pais":         [117, 230],
        "tel":          [300, 230],
        "estado_civil": [150, 241],
        "profissao":    [351, 241],
        "rg":           [178, 253],
        "cpf":          [348, 252.6],
        "mae":          [118, 265],
        "automovel":    [146, 276.5],
        "modelo_auto":  [320, 276.5],
        "placa_auto":   [117, 288.5],
        "cor_auto":     [302, 288.5],
        "proprietario": [195, 744],
    }
    for k, v in data.items():
        for i, coord in s.items():
            if k == i:
                x: int  = coord[0]
                y: int = (A4[1] - coord[1])
                c.drawString(x=x, y=y, text=v)
    
    tipo_residencia = {'anual': [177, 207], 'temp': [253, 207]}
    observacoes = {'l1': [148, 519], 'l2': [86, 531]}
    imob_fone = {'ddd': [360, 708], 'tel': [390, 708]}

    if data['tipo_residencia']:
        if data['tipo_residencia'] == 'Temporária':
            coords = tipo_residencia['temp']
            x, y = coords
            c.drawString(x, A4[1]-y, 'X')
        if data['tipo_residencia'] == 'Anual':
            coords = tipo_residencia['anual']
            x, y = coords
            c.drawString(x, A4[1]-y, 'X')
    
    if data['observacoes']:
        x, y = observacoes['l1']
        c.drawString(x, A4[1]-y, data['observacoes'])

    if data['imob_fone']:
        x, y = imob_fone['ddd']
        c.drawString(x, A4[1]-y, data['imob_fone'][5:7])
        x, y = imob_fone['tel']
        c.drawString(x, A4[1]-y, data['imob_fone'][9:])

    checkin = {'dia': [222, 494], 'mes': [262, 494], 'ano': [292, 494]}
    checkout = {'dia': [379, 494], 'mes': [422, 494], 'ano': [457, 494]}
    
    if data['checkin']:
        x, y = checkin['dia']
        c.drawString(x, A4[1]-y, data['checkin'][8:])
        x, y = checkin['mes']
        c.drawString(x, A4[1]-y, data['checkin'][5:7])
        x, y = checkin['ano']
        c.drawString(x, A4[1]-y, data['checkin'][:4])

    if data['checkout']:
        x, y = checkout['dia']
        c.drawString(x, A4[1]-y, data['checkout'][8:])
        x, y = checkout['mes']
        c.drawString(x, A4[1]-y, data['checkout'][5:7])
        x, y = checkout['ano']
        c.drawString(x, A4[1]-y, data['checkout'][:4])


    c.save()
    return file_name

if __name__ == '__main__':
    import csv

    with open('./files/data_test.csv', 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        chaves = next(reader)
        valores = next(reader)
        dados = dict(zip(chaves, valores))
    print(dados)
    dir = './files/filled_fichas/'
    img = "./files/ficha_model/ficha.png"
    pdf = fill_ficha(dados, img, dir)
    print(f"PDF gerado: {pdf}")



# a1 = {'nome': [101.2987012839, 329.36252415], 'doc': [291.23376619149, 329.36252415], 'idade': [397.5974025397, 329.36252415], 'parentesco': [439.0377803377, 329.36252415]}
# a2 = {'nome': [101.2987012839, 345.4114616904], 'doc': [291.23376619149, 345.4114616904], 'idade': [397.5974025397, 345.4114616904], 'parentesco': [439.0377803377, 345.4114616904]}
# a3 = {'nome': [101.2987012839, 361.4603992308], 'doc': [291.23376619149, 361.4603992308], 'idade': [397.5974025397, 361.4603992308], 'parentesco': [439.0377803377, 361.4603992308]}
# a4 = {'nome': [101.2987012839, 377.26980039], 'doc': [291.23376619149, 377.26980039], 'idade': [397.5974025397, 377.26980039], 'parentesco': [439.0377803377, 377.26980039]}
# a5 = {'nome': [101.2987012839, 393.3187379304], 'doc': [291.23376619149, 393.3187379304], 'idade': [397.5974025397, 393.3187379304], 'parentesco': [439.0377803377, 393.3187379304]}
# a6 = {'nome': [101.2987012839, 408.409529946], 'doc': [291.23376619149, 408.409529946], 'idade': [397.5974025397, 408.409529946], 'parentesco': [439.0377803377, 408.409529946]}
# a7 = {'nome': [101.2987012839, 423.979394724], 'doc': [291.23376619149, 423.979394724], 'idade': [397.5974025397, 423.979394724], 'parentesco': [439.0377803377, 423.979394724]}
# a8 = {'nome': [101.2987012839, 439.7887958832], 'doc': [291.23376619149, 439.7887958832], 'idade': [397.5974025397, 439.7887958832], 'parentesco': [439.0377803377, 439.7887958832]}
# a9 = {'nome': [101.2987012839, 455.5981970424], 'doc': [291.23376619149, 455.5981970424], 'idade': [397.5974025397, 455.5981970424], 'parentesco': [439.0377803377, 455.5981970424]}
# a10 = {'nome': [101.2987012839, 471.6471345828], 'doc': [291.23376619149, 471.6471345828], 'idade': [397.5974025397, 471.6471345828], 'parentesco': [439.0377803377, 471.6471345828]}
