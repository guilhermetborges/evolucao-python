import PAC
import moeda


#num = int(input('valor: '))
#fat = PAC.fatorial(num)
#print(f'o fatorial de {num} é {fat}') 

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% temos {moeda.aumenta10(p,10)}')
print(f'Reduzindo 13% temos {moeda.reduz13(p,13)}')