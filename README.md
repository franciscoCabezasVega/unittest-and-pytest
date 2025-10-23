# 🧩 Testing Template (Python)
This base project will serve as a professional template for testing in Python with unittest and pytest.

📁 Repository structure
```
testing-template-py/
│
├── src/
│   ├── __init__.py
│   ├── calculator.py
│
├── tests/
│   ├── __init__.py
│   ├── test_calculator_unittest.py
│   ├── test_calculator_pytest.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

🧰 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🧪 Test execution

### 🧠 With unittest
```bash
python -m unittest discover -s tests
```

### ⚡ With pytest
```bash
python -m pytest
```