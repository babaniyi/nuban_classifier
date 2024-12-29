import pytest
from nuban_classifier import calculate_check_digit, classify_account_number


def test_calculate_check_digit():
    """
    Test the calculate_check_digit function.
    """
    # Test for valid inputs
    assert calculate_check_digit("123456789", "011") == 6, "Expected check digit: 6 for First Bank"
    assert calculate_check_digit("987654321", "044") == 4, "Expected check digit: 4 for Access Bank"

    # Test for edge cases
    assert calculate_check_digit("000000000", "011") == 9, "Expected check digit: 9 for zero serial number"
    assert calculate_check_digit("999999999", "044") == 7, "Expected check digit: 7 for max serial number"

def test_classify_account_number():
    """
    Test the classify_account_number function.
    """
    # Test for valid account numbers
    assert "First Bank" in classify_account_number("1234567896"), "1234567896 should belong to First Bank"
    assert "Access Bank" in classify_account_number("9876543214"), "9876543214 should belong to Access Bank"

    # Test for invalid account numbers
    assert classify_account_number("1234501234") == [], "Invalid account number should return an empty list"
    assert classify_account_number("0000000000") == [], "Zeroed account number should return an empty list"

    # Test for multiple possible banks
    # Hypothetically, "123456789X" could match multiple banks depending on their check digit
    assert len(classify_account_number("123456789X")) >= 1, "Should identify at least one possible bank"

if __name__ == "__main__":
    pytest.main()