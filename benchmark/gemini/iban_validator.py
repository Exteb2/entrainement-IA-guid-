def validate_iban(iban: str) -> bool:
    """
    Fonction pure qui valide un numéro IBAN selon la norme ISO 13616.
    """
    # 1. Normalisation
    normalized = iban.replace(" ", "").upper()
    
    # 2. Vérification de structure
    if not (15 <= len(normalized) <= 34):
        return False
    if not normalized.isalnum():
        return False
    if not (normalized[0:2].isalpha() and normalized[2:4].isdigit()):
        return False
    if normalized[0:2] == "FR" and len(normalized) != 27:
        return False
        
    # 3. Contrôle modulo 97
    # Déplacement des 4 premiers caractères à la fin
    rearranged = normalized[4:] + normalized[:4]
    
    # Remplacement des lettres par leur valeur numérique (A=10, ..., Z=35)
    numeric_string = "".join(
        str(ord(char) - ord('A') + 10) if char.isalpha() else char 
        for char in rearranged
    )
    
    # Vérification modulo 97
    return int(numeric_string) % 97 == 1