import base64
import pytest
from pytest import approx

def calculate_discount(amount: int, member: bool) -> float:
    """
    Calculates the discount for a purchase of juice depending on the amount a customer purchases and whether she is a
    bonus club member.
    :param amount: The amount of juice cartons the customer purchases
    :param member: Whether the customer is a bonus club member
    :return: The discount between 0 and 1
    :raises:
        ValueError: if amount is not an integer or not within the accepted range, e.g., 0 < amount <= 10
    """

    if not isinstance(amount, int):
        raise ValueError("amount must be an int")
    if amount < 1 or amount > 10:
        raise ValueError("amount has to be greater than 0 and less or equal to 10")

    percentages = {(1, 2): 1.0, (3, 3): 3 / 4, (4, 5): 2 / 3, (6, 10): 1 / 2}

    for interval, percentage in percentages.items():
        if interval[0] <= amount <= interval[1]:
            if member:
                percentage *= 4 / 5

            return 1 - percentage

    raise RuntimeError("Logical error. Check implementation.")

#-------------------------------------------------------------------
### TESTING AREA ###
#-------------------------------------------------------------------

def test_ID_1():
    with pytest.raises(ValueError):
        calculate_discount(0, False)

def test_ID_2():
    with pytest.raises(ValueError):
        calculate_discount(0, True)
        
def test_ID_3():
    result = calculate_discount(1, False)
    assert result == 0

def test_ID_4():
    result = calculate_discount(1, True)
    assert result == approx(0.20)

def test_ID_5():
    result = calculate_discount(2, False)
    assert result == 0

def test_ID_6():
    result = calculate_discount(2, True)
    assert result == approx(0.20)

def test_ID_7():
    result = calculate_discount(3, False)
    assert round(result, 2) == 0.25

def test_ID_8():
    result = calculate_discount(3, True)
    assert result == approx(0.40)

def test_ID_9():
    result = calculate_discount(4, False)
    assert round(result, 2) == 0.33

def test_ID_10():
    result = calculate_discount(4, True)
    assert result == approx(0.46, rel=1e-1)

def test_ID_11():
    result = calculate_discount(5, False)
    assert round(result, 2) == 0.33

def test_ID_12():
    result = calculate_discount(5, True)
    assert result == approx(0.46, rel=1e-1)

def test_ID_13():
    result = calculate_discount(6, False)
    assert round(result, 2) == 0.50

def test_ID_14():
    result = calculate_discount(6, True)
    assert result == approx(0.60, rel=1e-1)

def test_ID_15():
    result = calculate_discount(7, False)
    assert round(result, 2) == 0.50

def test_ID_16():
    result = calculate_discount(7, True)
    assert result == approx(0.60, rel=1e-1)

def test_ID_17():
    result = calculate_discount(8, False)
    assert round(result, 2) == 0.50

def test_ID_18():
    result = calculate_discount(8, True)
    assert result == approx(0.60, rel=1e-1)

def test_ID_19():
    result = calculate_discount(9, False)
    assert round(result, 2) == 0.50

def test_ID_20():
    result = calculate_discount(9, True)
    assert result == approx(0.60, rel=1e-1)

def test_ID_21():
    result = calculate_discount(10, False)
    assert round(result, 2) == 0.50

def test_ID_22():
    result = calculate_discount(10, True)
    assert result == approx(0.60, rel=1e-1)

def test_ID_23():
    with pytest.raises(ValueError):
        calculate_discount(11, False)

def test_ID_24():
    with pytest.raises(ValueError):
        calculate_discount(11, True)

def test_ID_25():
    with pytest.raises(ValueError):
        calculate_discount("Test", "Test")

def test_ID_26():
    with pytest.raises(TypeError):
        calculate_discount(10, 10, True)
