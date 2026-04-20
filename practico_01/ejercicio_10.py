"""For-Else, Any."""

from typing import Iterable


def tiene_pares_basico(numeros: Iterable[int]) -> bool:
    for n in numeros:
        if n % 2 == 0:
            return True
    return False


# NO MODIFICAR - INICIO
assert tiene_pares_basico([1, 3, 5]) is False
assert tiene_pares_basico([1, 3, 5, 6]) is True
assert tiene_pares_basico([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN

###############################################################################


def tiene_pares_for_else(numeros: Iterable[int]) -> bool:
    for n in numeros:
        if n % 2 == 0:
            return True
    else:
        return False


# NO MODIFICAR - INICIO
assert tiene_pares_for_else([1, 3, 5]) is False
assert tiene_pares_for_else([1, 3, 5, 6]) is True
assert tiene_pares_for_else([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN

###############################################################################


def tiene_pares_any(numeros: Iterable[int]) -> bool:
    return any(n % 2 == 0 for n in numeros)


# NO MODIFICAR - INICIO
assert tiene_pares_any([1, 3, 5]) is False
assert tiene_pares_any([1, 3, 5, 6]) is True
assert tiene_pares_any([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN
