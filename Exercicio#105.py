def notas(*num, sit = False):
    resp = {}
    resp['total'] = len(num)
    resp['maior'] = max(num)
    resp['menor'] = min(num)
    resp['média'] = sum(num)/(len(num))
    if sit:
        if resp['média'] >= 7:
            resp['situação'] = 'BOA'
        elif 5 <= resp['média'] <7:
            resp['situação'] = 'RAZOÁVEL'
        else:
            resp['situação'] = 'RUIM'
        
    return resp

valores = notas(6,7,8,9, sit = True)
print(valores)
valores = notas(4,5,3,2)
print(valores)