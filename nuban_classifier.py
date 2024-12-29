class Bank:
    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code

# List of banks with their unique CBN codes
banks = [
    Bank("Access Bank", "044"),
    Bank("Afribank", "014"),
    Bank("Citibank", "023"),
    Bank("Diamond Bank", "063"),
    Bank("Ecobank", "050"),
    Bank("Equitorial Trust Bank", "040"),
    Bank("First Bank", "011"),
    Bank("FCMB", "214"),
    Bank("Fidelity Bank", "070"),
    Bank("Finbank", "085"),
    Bank("Guaranty Trust Bank", "058"),
    Bank("Intercontinental Bank", "069"),
    Bank("Oceanic Bank", "056"),
    Bank("BankPhb", "082"),
    Bank("Skye Bank", "076"),
    Bank("SpringBank", "084"),
    Bank("StanbicIBTC", "221"),
    Bank("Standard Chartered Bank", "068"),
    Bank("Sterling Bank", "232"),
    Bank("United Bank for Africa", "033"),
    Bank("Union Bank", "032"),
    Bank("Wema Bank", "035"),
    Bank("Zenith Bank", "057"),
    Bank("Unity Bank", "215"),
]


def calculate_check_digit(serial_number: str, bank_code: str) -> int:
    """
    Calculate the check digit for a NUBAN.

    Parameters:
        serial_number (str): The 9-digit serial number of the account.
        bank_code (str): The 3-digit bank code assigned to the bank.

    Returns:
        int: The calculated check digit for the serial number.
    """
    weights = [3, 7, 3] * 4  # Weights for calculating the check digit
    combined_number = bank_code + serial_number
    weighted_sum = sum(int(digit) * weight for digit, weight in zip(combined_number, weights))
    mod = weighted_sum % 10
    return (10 - mod) if mod != 0 else 0


def classify_account_number(account_number: str) -> list:
    """
    Generate a list of banks the account number likely belongs to.

    Parameters:
        account_number (str): The 10-digit account number (9-digit serial + 1 check digit).

    Returns:
        list: A list of banks that the account number could belong to.
    """
    if len(account_number) != 10:
        return []  # Return an empty list if the account number is not 10 digits

    serial_number = account_number[:-1]  # Extract the first 9 digits as the serial number
    provided_check_digit = int(account_number[-1])  # Extract the last digit as the check digit

    possible_banks = []
    for bank in banks:
        # Calculate the expected check digit for each bank and compare with the provided check digit
        expected_check_digit = calculate_check_digit(serial_number, bank.code)
        if expected_check_digit == provided_check_digit:
            possible_banks.append(bank.name)  # Add the bank name to the list if it matches

    return possible_banks