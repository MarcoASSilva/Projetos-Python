from wsgiref.validate import validator


valor = 10
i = 0
while valor >= i:
    print(f"valor de (i) é igual a : {i}")
    i += 1

texto = "MARCO ANTONIO SILVA E SILVA"
VOGAIS = 'AEIOU'
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
print()

for numero in range(0, 51, 5):
    print(numero, end=" ")

while True:
    numero = int(input("Digite um numero: "))
    if numero == 10:
        break
    print(numero)