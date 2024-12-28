BANK_CODES = {
    "044": "Access Bank",
    "014": "Afribank",
    "023": "Citibank",
    "063": "Diamond Bank",
    "050": "Ecobank",
    "040": "Equitorial Trust Bank",
    "011": "First Bank",
    "214": "FCMB",
    "070": "Fidelity Bank",
    "085": "Finbank",
    "058": "Guaranty Trust Bank",
    "069": "Intercontinental Bank",
    "056": "Oceanic Bank",
    "082": "BankPhb",
    "076": "Skye Bank",
    "084": "SpringBank",
    "221": "StanbicIBTC",
    "068": "Standard Chartered Bank",
    "232": "Sterling Bank",
    "033": "United Bank for Africa",
    "032": "Union Bank",
    "035": "Wema Bank",
    "057": "Zenith Bank",
    "215": "Unity Bank",
}


def calculate_check_digit(account_number: str, bank_code: str) -> int:
    """
    Calculate the check digit for a NUBAN account number.

    Parameters:
        account_number (str): The 10-digit NUBAN serial number (excluding bank code and check digit).
        bank_code (str): The 3-digit bank code assigned to the bank.

    Returns:
        int: The calculated check digit for the account number.
    """
    weights = [3, 7, 3] * 4
    combined_number = bank_code + account_number
    weighted_sum = sum(int(digit) * weight for digit, weight in zip(combined_number, weights))
    mod = weighted_sum % 10
    return (10 - mod) if mod != 0 else 0


def validate_nuban(account_number: str) -> bool:
    """
    Validate a NUBAN account number.

    Parameters:
        account_number (str): The full 13-digit NUBAN account number to validate.

    Returns:
        bool: True if the NUBAN is valid, False otherwise.
    """
    if len(account_number) != 13:
        return False

    bank_code = account_number[:3]
    nuban_serial = account_number[3:-1]
    check_digit = int(account_number[-1])

    if bank_code not in BANK_CODES:
        return False

    calculated_check_digit = calculate_check_digit(nuban_serial, bank_code)
    return calculated_check_digit == check_digit


def classify_bank(account_number: str) -> str:
    """
    Classify the bank based on the NUBAN account number.

    Parameters:
        account_number (str): The full 13-digit NUBAN account number.

    Returns:
        str: The name of the bank if identified, or an error message if invalid or unknown.
    """
    if not validate_nuban(account_number):
        return "Invalid NUBAN account number."

    bank_code = account_number[:3]
    return BANK_CODES.get(bank_code, "Unknown Bank")


# Example usage
example_nuban = "0110000014579"  # Example NUBAN for First Bank
if validate_nuban(example_nuban):
    print(f"Valid NUBAN. Bank: {classify_bank(example_nuban)}")
else:
    print("Invalid NUBAN.")
