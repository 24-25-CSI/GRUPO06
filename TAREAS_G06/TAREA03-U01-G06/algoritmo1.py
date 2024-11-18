from itertools import permutations

def generar_anagramas(palabra):

    permutaciones = sorted(set(''.join(p) for p in permutations(palabra)))
    

    total_permutaciones = len(permutaciones)
    print(f"Total de permutaciones: {total_permutaciones}")

    primeras_10 = permutaciones[:10]
    print("Primeras 10 permutaciones ordenadas alfabéticamente:")
    for perm in primeras_10:
        print(perm)


palabra = input("Introduce una palabra o frase: ")
generar_anagramas(palabra)
