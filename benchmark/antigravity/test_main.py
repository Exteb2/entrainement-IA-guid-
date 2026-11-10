from main import validate_iban


def test_valid_french_iban_with_spaces():
    """(1) Un IBAN français valide avec espaces."""
    assert validate_iban("FR76 3000 6000 0112 3456 7890 189") is True


def test_valid_french_iban_lowercase_no_spaces():
    """(2) Le même IBAN sans espaces ni majuscules."""
    assert validate_iban("fr7630006000011234567890189") is True


def test_invalid_check_digits():
    """(3) Un IBAN avec une clé de contrôle invalide."""
    assert validate_iban("FR99 3000 6000 0112 3456 7890 189") is False


def test_invalid_french_iban_length():
    """(4) Un IBAN FR de mauvaise longueur (26 caractères au lieu de 27)."""
    assert validate_iban("FR76 3000 6000 0112 3456 7890 18") is False


def test_iban_with_special_character():
    """(5) Une chaîne contenant un caractère spécial."""
    assert validate_iban("FR76 3000 6000 0112 3456 7890 18@") is False

