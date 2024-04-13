dados = {}
dados = {'nome':'Pedro', 'idade':25}
dados['sexo'] = 'M'
print(f'o {dados['nome']} tem {dados['idade']} anos')
for v , k in dados.items():
    print(f'{v}: {k}')
#dados['peso']= input('quantos KG você pesa: ')
#print(f'{dados["nome"]}')
#print(dados["peso"])
#del dados['idade']
goias = {'melhor':'diego','decpção':'vinicius','clube':'goias'}
fla = {'melhor':'pedro','decepção':'gabi','clube':'flamengo'}
flu = {'melhor':'cano','decepção':'r.augusto','clube':'fluminense'}
print(goias['clube'])
print(goias.values())
print(goias.keys())
print(goias.items())
for player, item in goias.items():
    print(f'o {player} é {item}')
times = []
times.append(goias)
times.append(fla)
times.append(flu)
print(times[1]['melhor']) 
  