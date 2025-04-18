import sys
import re

# aqui se encontra o nosso dicionario de palavras reservadas, operadores e delimitadores
PALAVRAS_RESERVADAS = {'inteiro', 'real', 'booleano', 'se', 'então', 'senao', 'enquanto', 'para', 'retorne'}
OPERADORES = {'=': 'atribuicao', '+': 'soma', '-': 'subtracao', '*': 'multiplicacao', '/': 'divisao'}
DELIMITADORES = {';': 'ponto_virgula', '(': 'abre_parentese', ')': 'fecha_parentese'}

# aqui definimos as expressoes regulares para identificar identificadores e numeros
IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
NUMERO = r'\d+(\.\d+)?'

def analisar_linha(linha):
    tokens = []
    palavras = re.findall(r'\w+|[^\s\w]', linha)

    for palavra in palavras:
        if palavra in PALAVRAS_RESERVADAS:
            tokens.append((palavra, 'palavra_reservada'))
        elif palavra in OPERADORES:
            tokens.append((palavra, 'operador_' + OPERADORES[palavra]))
        elif palavra in DELIMITADORES:
            tokens.append((palavra, 'delimitador'))
        elif re.fullmatch(NUMERO, palavra):
            tokens.append((palavra, 'numero'))
        elif re.fullmatch(IDENTIFICADOR, palavra):
            tokens.append((palavra, 'identificador'))
        else:
            tokens.append((palavra, 'simbolo_desconhecido'))
    return tokens

def main():
    if len(sys.argv) != 3:
        print("Execute no prompt: python (ou python3) main.py entrada.txt saida.txt")
        return

    entrada_path = sys.argv[1]
    saida_path = sys.argv[2]

    with open(entrada_path, 'r', encoding='utf-8') as entrada, open(saida_path, 'w', encoding='utf-8') as saida:
        for linha in entrada:
            tokens = analisar_linha(linha)
            for lexema, tipo in tokens:
                saida.write(f"<{lexema}, {tipo}>\n")

if __name__ == "__main__":
    main()
