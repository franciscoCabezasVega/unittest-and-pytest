"""
🧩 Practice Functions - Pytest Training
File with functions from different categories
for practicing unit test design.
"""

from typing import List, Dict


# -------------------------
# 🧠 Level 1: Basic operations
# -------------------------

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


def is_even(n: int) -> bool:
    """Returns True if the number is even"""
    return n % 2 == 0


def greet(name: str) -> str:
    """Returns a personalized greeting"""
    return f"Hello, {name}!"


# -------------------------
# ⚙️ Level 2: Conditional logic
# -------------------------

def max_of_three(a: int, b: int, c: int) -> int:
    """Returns the largest of three numbers"""
    return max(a, b, c)


def grade(score: int) -> str:
    """
    Returns a grade based on the numerical score.
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: <60
    """
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# -------------------------
# 📦 Level 3: Collections
# -------------------------

def average(numbers: List[int]) -> float:
    """Returns the average of a list of numbers"""
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)


def find_max_length(words: List[str]) -> str:
    """Returns the longest word in a list"""
    if not words:
        raise ValueError("List cannot be empty")
    return max(words, key=len)


def count_occurrences(items: List[str]) -> Dict[str, int]:
    """Count how many times each item appears in the list."""
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result


# -------------------------
# 💡 Level 4: Validations and errors
# -------------------------

def safe_divide(a: float, b: float) -> float:
    """Divide two numbers and throw an error if the divisor is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return round(a / b, 2)


def reverse_string(s: str) -> str:
    """Returns a reversed string."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]