curso = "pYTHon"
## convertendo string tudo pra maiusculo
print(curso.upper())

## convertendo string tudo pra minusculo
print(curso.lower())

## convertendo string pra titulo
print(curso.title())

curso = "  python   "

## removendo espaços em branco da string da esquerda e da direita
print(curso.strip())

## removendo espaços em branco da string somente da esquerda
print(curso.lstrip())

## removendo espaços em branco da string somente da direita
print(curso.rstrip())

curso = "Python"

print(curso.center(10,"#"))

print(".".join(curso))