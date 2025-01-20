import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from utils.mystr import two_liner

def fill_ficha(data: dict[str, str]):
    file_name = f'{str(data['checkin'])}_{str(data['apto'])}_{str(data['id'])}.pdf'
    img = './files/ficha_model/ficha.png'
    dir = './files/tmp_filled_fichas/'
    path = os.path.join(dir, file_name)
    c = canvas.Canvas(path)
    c.drawImage(img, 0, 0, width=A4[0], height=A4[1])
    s: dict[int, int] = {
        'apto':         [117, 193],
        'nome':         [217, 193],
        'cidade':       [187, 218],
        'cep':          [376, 218],
        'uf':           [482, 218],
        'pais':         [117, 230],
        'tel':          [300, 230],
        'estado_civil': [151, 241],
        'profissao':    [351, 241],
        'rg':           [178, 253.4],
        'cpf':          [348, 253],
        'mae':          [118, 265],
        'automovel':    [146, 276.5],
        'modelo_auto':  [321, 276.5],
        'placa_auto':   [118, 288.5],
        'cor_auto':     [303, 288.5],
        'proprietario': [195, 744],
    }
    acomp_coord = [
        {'doc': [293, 328], 'idade': [405, 328], 'nome': [101, 328], 'parentesco': [443, 328]},
        {'doc': [293, 344], 'idade': [405, 344], 'nome': [101, 344], 'parentesco': [443, 344]},
        {'doc': [293, 360], 'idade': [405, 360], 'nome': [101, 360], 'parentesco': [443, 360]},
        {'doc': [293, 376], 'idade': [405, 376], 'nome': [101, 376], 'parentesco': [443, 376]},
        {'doc': [293, 392], 'idade': [405, 392], 'nome': [101, 392], 'parentesco': [443, 392]},
        {'doc': [293, 407], 'idade': [405, 407], 'nome': [101, 407], 'parentesco': [443, 407]},
        {'doc': [293, 422], 'idade': [405, 422], 'nome': [101, 422], 'parentesco': [443, 422]},
        {'doc': [293, 438], 'idade': [405, 438], 'nome': [101, 438], 'parentesco': [443, 438]}, 
        {'doc': [293, 454], 'idade': [405, 454], 'nome': [101, 454], 'parentesco': [443, 454]},
        {'doc': [293, 470], 'idade': [405, 470], 'nome': [101, 470], 'parentesco': [443, 470]}
    ]
    acomps = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']
    counter = 0
    for k, v in data.items():
        for i, coord in s.items():
            if k == i:
                x = coord[0]
                y = (A4[1] - coord[1])
                if v != None:
                    c.drawString(x=x, y=y, text=str(v))
        if k in acomps and data[k] is not None:
            field: dict = data[k]
            for key, value in field.items():
                x, y = acomp_coord[counter][key]
                v = value
                if v != None:
                    c.drawString(x=x, y=A4[1] - y, text=str(v))
            counter += 1

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
        if len(str(data['observacoes'])) > 77:
            lines = two_liner(str(data['observacoes']))
            p1 = Paragraph(str(lines[0]))
            p2 = Paragraph(str(lines[1]))
            p1.wrap(400,800)
            p1.drawOn(c, x, A4[1]-y)
            x, y = observacoes['l2']
            p2.wrap(400,800)
            p2.drawOn(c, x, A4[1]-y)
        else:
            p = Paragraph(str(data['observacoes']))
            p.wrap(400, 800)
            p.drawOn(c, x, A4[1]-y)

    if data['imob_fone']:
        x, y = imob_fone['ddd']
        c.drawString(x, A4[1]-y, str(data['imob_fone'][5:7]))
        x, y = imob_fone['tel']
        c.drawString(x, A4[1]-y, str(data['imob_fone'][9:]))

    checkin = {'dia': [226, 494], 'mes': [262, 494], 'ano': [292, 494]}
    checkout = {'dia': [385, 494], 'mes': [422, 494], 'ano': [457, 494]}
    
    if data['checkin']:
        x, y = checkin['dia']
        c.drawString(x, A4[1]-y, str(data['checkin'][8:]))
        x, y = checkin['mes']
        c.drawString(x, A4[1]-y, str(data['checkin'][5:7]))
        x, y = checkin['ano']
        c.drawString(x, A4[1]-y, str(data['checkin'][:4]))

    if data['checkout']:
        x, y = checkout['dia']
        c.drawString(x, A4[1]-y, str(data['checkout'][8:]))
        x, y = checkout['mes']
        c.drawString(x, A4[1]-y, str(data['checkout'][5:7]))
        x, y = checkout['ano']
        c.drawString(x, A4[1]-y, str(data['checkout'][:4]))

    c.save()
    return path
