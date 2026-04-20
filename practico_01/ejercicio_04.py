"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    """Determinar si una letra es vocal utilizando sólo IF."""
    letra_lower = letra.lower()
    if letra_lower == "a" or letra_lower == "e" or letra_lower == "i" or letra_lower == "o" or letra_lower == "u":
        return True
    else:
        return False

# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    if letra.lower() in "aeiouAEIOU":
        return True
    else:
        return False


# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    return letra.lower() in "aeiou"

# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
