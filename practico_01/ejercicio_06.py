"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    letras = []
    numeros = []
    for x in lista:
        if isinstance(x, str):
            letras.append(x)
        else:
            numeros.append(x)
    return letras + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    numeros = [x for x in lista if isinstance(x, (int, float))]
    no_numeros = [x for x in lista if not isinstance(x, (int, float))]
    return no_numeros + numeros

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    return sorted(lista, key=lambda x: isinstance(x, (int, float)))


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:

    numeros = list(filter(lambda x: isinstance(x, (int, float)), lista))
    no_numeros = list(filter(lambda x: not isinstance(x, (int, float)), lista))
    return no_numeros + numeros


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    if not lista:
        return []
    primero = lista[0]
    resto = numeros_al_final_recursivo(lista[1:])
    if isinstance(primero, (int, float)):
        return resto + [primero]
    else:
        return [primero] + resto


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
