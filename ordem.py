c = []
for i in range (4):
    i = int(input("digite um numero: "))
    c.append(i)
print(c)
crescente = sorted(c)
decrescente = sorted(c,reverse=True)
print(f"""ordem crescente: {crescente}
ordem decrescente{decrescente}""")