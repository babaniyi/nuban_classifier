# NUBAN Classifier

The NUBAN Classifier is a Python-based project for validating and classifying Nigerian bank account numbers based on the **Nigeria Uniform Bank Account Number (NUBAN)** scheme. The system uses the NUBAN algorithm defined by the Central Bank of Nigeria (CBN) to calculate check digits, validate account numbers, and identify the banks to which they belong.

---

## Features

1. **Check Digit Calculation**: Computes the check digit for a NUBAN account number using a standardized algorithm.
2. **Validation**: Verifies the integrity of a NUBAN account number based on its check digit.
3. **Bank Classification**: Identifies possible banks for a given account number.

---

## Installation

### Prerequisites
- Python 3.7+

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/babaniyi/nuban_classifier.git
   cd nuban-classifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests to verify the installation:
   ```bash
   pytest tests/
   ```

---

## Usage

### Example Code
```python
from nuban_classifier import classify_account_number

# Example account number
account_number = "1234567890"
matching_banks = classify_account_number(account_number)

if matching_banks:
    print(f"The account number may belong to: {', '.join(matching_banks)}")
else:
    print("No matching banks found.")
```

### Explanation
- `calculate_check_digit(serial_number, bank_code)`: Calculates the check digit for a given serial number and bank code.
- `classify_account_number(account_number)`: Identifies all possible banks an account number may belong to.

---

## Project Structure

```plaintext
.
├── nuban_classifier.py      # Core module with validation and classification logic
├── tests/                   # Unit tests
│   ├── test_account_classifier.py
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
```

---

## Tests

### Running Tests
Use `pytest` to run the included unit tests:
```bash
pytest tests/
```

### Example Tests
1. **Check Digit Calculation**:
   - Tests for correctness of the computed check digit.
2. **Account Classification**:
   - Verifies the identification of valid and invalid account numbers.

---

## References

- [CBN NUBAN Proposal Document](https://www.cbn.gov.ng/out/2011/circulars/bspd/nuban%20proposals%20v%200%204-%2003%2009%202010.pdf)
---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
