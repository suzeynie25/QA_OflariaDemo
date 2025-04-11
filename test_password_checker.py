from password_checker import is_strong_password


def test_strong_password():
    assert is_strong_password("Strong1!")


def test_too_short():
    assert not is_strong_password("S1!")


def test_no_uppercase():
    assert not is_strong_password("weak1!")


def test_no_lowercase():
    assert not is_strong_password("WEAK1!")


def test_no_digit():
    assert not is_strong_password("WeakPassword!")


def test_no_special_char():
    assert not is_strong_password("Weak1234")