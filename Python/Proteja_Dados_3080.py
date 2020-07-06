# Detectar Frases Repetidas em discursos k vezes 
# Ideia 1 : Pegar Partes de Srings e procura-las 
# Ideia 2 : Dividir o texto original em subtextos com determinadas palavras 
# Ideia 3 : Texto em vetor e sem espacos 
''' Maior trecho repetido k vezes '''
def CapturaTexto(texto):
    texto_total = ''
    for x in texto:
        if x != " ":
            texto_total += x
    return texto_total

def Proc_Setenca(texto , texto_total , repeticoes):
    texto.split(' ') ; texto_inv = texto[::-1]
    texto[0]+texto[1].find(texto_total,1,-1)

def main():
    texto = input().strip().lower()
    repeticoes = int(input())