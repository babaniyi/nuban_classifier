from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the Bank class and the list of banks
class Bank:
    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code

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

# Define the check digit calculation function
def calculate_check_digit(serial_number: str, bank_code: str) -> int:
    weights = [3, 7, 3] * 4
    combined_number = bank_code + serial_number
    weighted_sum = sum(int(digit) * weight for digit, weight in zip(combined_number, weights))
    mod = weighted_sum % 10
    return (10 - mod) if mod != 0 else 0

# Define the classify function
def classify_account_number(account_number: str):
    if len(account_number) != 10:
        return []

    serial_number = account_number[:-1]
    provided_check_digit = int(account_number[-1])

    possible_banks = []
    for bank in banks:
        expected_check_digit = calculate_check_digit(serial_number, bank.code)
        if expected_check_digit == provided_check_digit:
            possible_banks.append({"bankName": bank.name, "uniqueCbnBankCode": bank.code})

    return possible_banks

# API endpoint
@app.route('/classify-account', methods=['POST'])
def classify_account():
    data = request.json
    account_number = data.get("accountNumber")

    if not account_number or len(account_number) != 10 or not account_number.isdigit():
        return jsonify({
            "code": 400,
            "message": "Invalid account number. Please provide a valid 10-digit account number.",
            "data": []
        }), 400

    possible_banks = classify_account_number(account_number)

    return jsonify({
        "code": 200,
        "message": "Successful call",
        "data": possible_banks
    })

if __name__ == '__main__':
    app.run(debug=True)
