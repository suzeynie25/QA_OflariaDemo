from grades import calculate_average, get_letter_grade

def test_calculate_average():
    assert calculate_average([100, 80, 90]) == 90
    assert calculate_average([]) == 0

def test_get_letter_grade():
    assert get_letter_grade(95) == "A"
    assert get_letter_grade(85) == "B"
    assert get_letter_grade(75) == "C"
    assert get_letter_grade(65) == "D"
    assert get_letter_grade(50) == "F"