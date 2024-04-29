# Função de cabeçalho e linha
def linha():
    return "-" *42

def cabecalho(texto:str):
    print(linha())
    print(texto.center(42))
    print(linha())
