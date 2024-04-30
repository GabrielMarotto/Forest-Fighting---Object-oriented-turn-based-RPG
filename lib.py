# Função de cabeçalho e linha
def linha():
    return "-" *48

def cabecalho(texto:str):
    print(linha())
    print(texto.center(48))
    print(linha())
