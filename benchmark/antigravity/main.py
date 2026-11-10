def validate_iban(iban: str) -> bool:
    """Valide un numéro IBAN selon la norme ISO 13616.

    Fonction pure effectuant :
    1. Normalisation : suppression des espaces et conversion en majuscules.
    2. Vérification de structure : longueur 15..34, alphanumérique ASCII uniquement,
       2 lettres (code pays) + 2 chiffres (clé), et longueur exacte de 27 si code pays 'FR'.
    3. Contrôle modulo 97 : déplacement des 4 premiers caractères à la fin,
       conversion A..Z -> 10..35, et vérification que l'entier modulo 97 vaut 1.
    """
    if not isinstance(iban, str):
        return False

    # 1. Normalisation : supprimer tous les espaces et convertir en majuscules
    normalized = iban.replace(" ", "").upper()

    # 2. Vérification de structure
    if not (15 <= len(normalized) <= 34):
        return False

    if not (normalized.isascii() and normalized.isalnum()):
        return False

    country_code = normalized[:2]
    check_digits = normalized[2:4]

    if not (country_code.isalpha() and check_digits.isdigit()):
        return False

    if country_code == "FR" and len(normalized) != 27:
        return False

    # 3. Contrôle modulo 97
    rearranged = normalized[4:] + normalized[:4]
    numeric_iban = "".join(
        str(ord(char) - ord("A") + 10) if char.isalpha() else char
        for char in rearranged
    )

    return int(numeric_iban) % 97 == 1

