from main import calculate_overtime, calculate_pay


def test_no_overtime():
    assert calculate_overtime(40) == 0
    assert calculate_overtime(30) == 0


def test_overtime():
    assert calculate_overtime(45) == 5
    assert calculate_overtime(50) == 10


def test_regular_pay():
    assert calculate_pay(40, 10) == 400.0


def test_overtime_pay():
    # 40 regular + 5 overtime at 1.5x
    assert calculate_pay(45, 10) == 475.0


def test_zero_hours():
    assert calculate_pay(0, 10) == 0.0
