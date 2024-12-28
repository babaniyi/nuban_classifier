import pytest
from nuban_classifier import calculate_check_digit, validate_nuban, classify_bank

def test_calculate_check_digit():
    # Test with example account numbers
    assert calculate_check_digit("000001457", "011") == 9  # First Bank example
    assert calculate_check_digit("000000022", "011") == 0  # First Bank example with check digit 0

def test_validate_nuban():
    # Valid NUBANs
    assert validate_nuban("0110000014579") is True  # Valid First Bank NUBAN
    assert validate_nuban("0110000000220") is True  # Valid First Bank NUBAN

    # Invalid NUBANs
    assert validate_nuban("0110000014570") is False  # Incorrect check digit
    assert validate_nuban("01100000145") is False    # Too short
    assert validate_nuban("1234567890123") is False  # Invalid bank code

def test_classify_bank():
    # Valid bank classification
    assert classify_bank("0110000014579") == "First Bank"
    assert classify_bank("0441234567890") == "Access Bank"

    # Invalid classifications
    assert classify_bank("0110000014570") == "Invalid NUBAN account number."
    assert classify_bank("9991234567890") == "Invalid NUBAN account number."  # Unknown bank code

if __name__ == "__main__":
    pytest.main()
