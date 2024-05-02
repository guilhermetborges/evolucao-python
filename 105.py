def notas(*total,sit=False):
    boletim = {}
    boletim['total'] = len(total)
    boletim['maior'] = max(total)
    boletim['menor'] = min(total)
    soma = 0
    for notas in total:
        soma+= notas
    media = soma/len(total)
    boletim['media'] = media
    if sit == True:
        if media < 6:
            boletim['situação'] = 'RUIM'
        elif 7 > media >= 6:
            boletim['situação'] = 'MEDIANA'
        else: boletim['situação'] = 'OTIMA'
    return boletim

resp = notas(5.5, 2.5, 6.5,10,9.9,sit=True)
print(resp)