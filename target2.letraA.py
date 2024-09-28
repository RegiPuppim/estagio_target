# Função para contar a ocorrência da letra 'a' (maiúscula ou minúscula)
def contarLetraA(texto):
    # Converte todas as letras do texto para minúsculas e conta as ocorrências de 'a'
    return texto.lower().count('a')


def main():
    texto = input("Digite o texto: ")
    ocorrencias = contarLetraA(texto)

    if ocorrencias > 0:
        print("A letra 'a' aparece %i vez(es) no texto." % ocorrencias)
    else:
        print("A letra 'a' não aparece no texto.")


main()
