Soul_Gem = { '>':8, '<':9, '+':10, '-':11, '.':12, ',':13, '[':14, ']':15 }
Chito = input()
n = len(Chito)
MODoka = 10**6+3

modulos = [1]
for i in range(n-1):
    modulos.append( (modulos[i]*16)%MODoka )

Yuuri = 0
for i in range(n):
    Yuuri += Soul_Gem[ Chito[n-1-i] ] * modulos[i]
    Yuuri = Yuuri%MODoka

print(Yuuri)
