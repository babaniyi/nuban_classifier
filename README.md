# NUBAN Classifier
The NUBAN Classifier project is a Python-based tool designed to validate and classify Nigerian bank account numbers according to the Nigeria Uniform Bank Account Number (NUBAN) standard. This standard was introduced by the Central Bank of Nigeria (CBN) to streamline electronic payments and ensure uniformity across all banks in the country.

## Features
- Validate NUBAN account numbers using the official check digit algorithm.
- Classify banks based on the first three digits of the NUBAN.

## Getting Started

### Prerequisites
- Python 3.7+

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/babaniyi/nuban_classifier.git
   cd nuban-classifier
   ```
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

### Usage
```python
from nuban_classifier import validate_nuban, classify_bank

example_nuban = "0110000014579"  # Example NUBAN for First Bank
if validate_nuban(example_nuban):
    print(f"Valid NUBAN. Bank: {classify_bank(example_nuban)}")
else:
    print("Invalid NUBAN.")
```

### Testing
Run the included tests to ensure functionality:
```bash
pytest tests/
```

## Project Structure
```
.
├── nuban_classifier.py      # Main module for NUBAN validation and classification
├── tests/
│   ├── test_nuban.py        # Unit tests for the project
├── requirements.txt         # Dependencies file
├── README.md                # Project documentation
```

## Reference
- [CBN NUBAN Proposals Document](https://www.cbn.gov.ng/out/2011/circulars/bspd/nuban%20proposals%20v%200%204-%2003%2009%202010.pdf)

## License
MIT License
