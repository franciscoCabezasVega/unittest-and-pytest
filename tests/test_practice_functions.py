from collections import Counter
from typing import List

import pytest
import string
import os

from src.practice_functions import add, is_even, greet, max_of_three, grade, average, find_max_length, \
    count_occurrences, safe_divide, reverse_string


def pytest_addoption(parser):
    parser.addoption(
        "--fixed-seed",
        action="store_true",
        default=False,
        help="Set the random seed to obtain reproducible results"
    )

def pytest_configure(config):
    use_fixed_seed = config.getoption("--fixed-seed") or os.getenv("FIXED_SEED", "true").lower() in ("1", "true", "yes")
    if use_fixed_seed:
        random.seed(42)
        print("\n🔒 Reproducible mode enabled (seed = 42)")
    else:
        print("\n🎲 Real random mode activated")


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (4, -5, -1),
    (-6, 7, 1),
    (-3, -4, -7),
    (5, -5, 0),
    (0, 1, 1),
    (25, 17, 42),
    (10, 100, 110)
])
def test_add(a: int, b: int, expected: int):
    assert add(a, b) == expected

@pytest.mark.parametrize("a,expected", [
    (1, False),
    (4, True),
    (-6, True),
    (-3, False),
    (5, False),
    (0, True)
])
def test_is_even(a: bool, expected: bool):
    assert is_even(a) == expected

def test_greeting():
    assert greet("Frank") == "Hello, Frank!"

@pytest.mark.parametrize("a,b,c,expected", [
    (1, 2, 3, 3),
    (5, 7, 1, 7),
    (-1, 0, -5, 0),
    (15, -29, 8, 15),
    (-7, -39, -1200, -7)
])
def test_multiply(a: int, b: int, c: int, expected: int):
    assert max_of_three(a, b, c) == expected

@pytest.mark.parametrize("score,expected", [
    (-1, "Score must be between 0 and 100"),
    (0, "F"),
    (1, "F"),
    (59, "F"),
    (60, "D"),
    (69, "D"),
    (70, "C"),
    (79, "C"),
    (80, "B"),
    (89, "B"),
    (90, "A"),
    (100, "A"),
    (101, "Score must be between 0 and 100"),
])
def test_grade(score: int, expected: str):
    if score < 0 or score > 100:
        with pytest.raises(ValueError) as excinfo:
            grade(score)
        assert str(excinfo.value) == expected
    else:
        assert grade(score) == expected

@pytest.mark.parametrize("values,expected", [
    ([], "List cannot be empty"),
    ([0], 0),
    ([1, 2, 3], 2),
    ([-1, 2, 0], 0.3333333333333333),
    ([-10, -20, -30], -20),
    ([300, 100, 200], 200)
])
def test_average(values: list, expected: float):
    if not values:
        with pytest.raises(ValueError) as excinfo:
            average(values)
        assert str(excinfo.value) == expected
    else:
        assert average(values) == expected

@pytest.mark.parametrize("words,expected", [
    ([], "List cannot be empty"),
    (["hola"], "hola"),
    (["hola", "mundo"], "mundo"),
    (["hola", "mundo", "texto más largo ñamé"], "texto más largo ñamé"),
    (["ho  la  ", "mundo"], "ho  la  "),
])
def test_find_max_length(words: list, expected: str):
    if not words:
        with pytest.raises(ValueError) as excinfo:
            find_max_length(words)
        assert str(excinfo.value) == expected
    else:
        assert find_max_length(words) == expected

@pytest.mark.parametrize("item,expected", [
    ([], {}),
    (["a"], {"a": 1}),
    (["a", "a", "a"], {"a": 3}),
    (["a", "b", "c"], {"a": 1, "b": 1, "c": 1}),
    (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
    (["A", "a", "A"], {"A": 2, "a": 1}),
    ([" ", " "], {" ": 2}),
    (["a", "", "a", ""], {"a": 2, "": 2}),
    (["ñ", "ñ", "á"], {"ñ": 2, "á": 1}),
    (["1", "2", "1", "3", "2", "1"], {"1": 3, "2": 2, "3": 1}),
])
def test_count_occurrences(item: list, expected: dict):
    assert count_occurrences(item) == expected

dynamic_cases = [
    ([], {}),
    (["a"], {"a": 1}),
    (["a"] * 5, {"a": 5}),
    ([str(i % 3) for i in range(6)], {"0": 2, "1": 2, "2": 2}),
    (["ñ" if i % 2 == 0 else "á" for i in range(5)], {"ñ": 3, "á": 2}),
]

@pytest.mark.parametrize("item,expected", dynamic_cases)
def test_count_occurrences_dynamic(item: list, expected: dict):
    assert count_occurrences(item) == expected

def test_count_occurrences_random():
    items = [random.choice(["a", "b", "c"]) for _ in range(1000)]
    expected = dict(Counter(items))
    assert count_occurrences(items) == expected

@pytest.fixture
def count_occurrences_data() -> List[tuple]:
    return [
        ([], {}),
        (["a"], {"a": 1}),
        (["a", "a", "a"], {"a": 3}),
        (["a", "b", "c"], {"a": 1, "b": 1, "c": 1}),
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["A", "a", "A"], {"A": 2, "a": 1}),
        ([" ", " "], {" ": 2}),
        (["a", "", "a", ""], {"a": 2, "": 2}),
        (["ñ", "ñ", "á"], {"ñ": 2, "á": 1}),
        (["1", "2", "1", "3", "2", "1"], {"1": 3, "2": 2, "3": 1}),
    ]

@pytest.mark.parametrize("index", range(10))
def test_count_occurrences_fixture(count_occurrences_data, index):
    items, expected = count_occurrences_data[index]
    assert count_occurrences(items) == expected

@pytest.fixture
def random_items():
    data = [random.choice(["a", "b", "c", "ñ"]) for _ in range(random.randint(5, 20))]
    expected = dict(Counter(data))
    return data, expected

def test_count_occurrences_random_fixture(random_items):
    items, expected = random_items
    assert count_occurrences(items) == expected

@pytest.mark.parametrize("a,b,expected", [
    (1, 0, "Cannot divide by zero"),
    (0, 1, 0),
    (10, 2, 5.0),
    (7, 3, 2.33),
    (-8, 2, -4.0),
    (8, -2, -4.0),
    (-9, -3, 3.0),
    (0, 5, 0.0),
    (1, 3, 0.33),
    (1, 6, 0.17),
    (2.5, 0.5, 5.0),
    (10.5, 3.5, 3.0),
    (1000000, 2, 500000.0),
    (5, 0.3333, 15.0),
    (-0.5, 0.1, -5.0),
    (1, 0.0001, 10000.0),
])
def test_safe_divide(a: float, b: float, expected):
    if b == 0:
        with pytest.raises(ZeroDivisionError) as excinfo:
            safe_divide(a, b)
        assert str(excinfo.value) == expected
    else:
        result = safe_divide(a, b)
        assert round(result, 2) == expected

import pytest
import random

@pytest.fixture(params=[
    (10, 2, 5.0),
    (7, 3, 2.33),
    (-8, 2, -4.0),
    (8, -2, -4.0),
    (1, 3, 0.33),
    (2.5, 0.5, 5.0),
])
def static_cases(request):
    return request.param


@pytest.fixture(params=[
    (1, 0),
    (-10, 0),
    (0, 0),
])
def zero_division_cases(request):
    return request.param


@pytest.fixture
def random_valid_case():
    a = round(random.uniform(-1000, 1000), 2)
    b = round(random.uniform(0.01, 1000), 2)
    expected = round(a / b, 2)
    return a, b, expected


def test_safe_divide_static(static_cases):
    a, b, expected = static_cases
    result = safe_divide(a, b)
    assert round(result, 2) == expected


def test_safe_divide_zero(zero_division_cases):
    a, b = zero_division_cases
    with pytest.raises(ZeroDivisionError) as excinfo:
        safe_divide(a, b)
    assert str(excinfo.value) == "Cannot divide by zero"


def test_safe_divide_random(random_valid_case):
    a, b, expected = random_valid_case
    result = safe_divide(a, b)
    assert round(result, 2) == expected


def generate_random_case():
    a = round(random.uniform(-1000, 1000), 2)
    b = round(random.uniform(0.01, 1000), 2)
    expected = round(a / b, 2)
    return a, b, expected, None


@pytest.fixture(params=[
    (10, 2, 5.0, None),
    (7, 3, 2.33, None),
    (-8, 2, -4.0, None),
    (8, -2, -4.0, None),
    (2.5, 0.5, 5.0, None),
    (1, 3, 0.33, None),
    (1, 0, None, "Cannot divide by zero"),
    (-5, 0, None, "Cannot divide by zero"),
    (0, 0, None, "Cannot divide by zero"),
    *[generate_random_case() for _ in range(3)]
])
def mixed_cases(request):
    return request.param


def test_safe_divide_mixed(mixed_cases):
    a, b, expected, error_msg = mixed_cases

    if error_msg:
        with pytest.raises(ZeroDivisionError) as excinfo:
            safe_divide(a, b)
        assert str(excinfo.value) == error_msg
    else:
        result = safe_divide(a, b)
        assert round(result, 2) == expected


def generate_random_string():
    length = random.randint(1, 20)
    s = ''.join(random.choice(string.ascii_letters + string.digits + "áéíóúñ ") for _ in range(length))
    expected = s[::-1]
    return s, expected, None


@pytest.fixture(params=[
    ("", "", None),
    ("a", "a", None),
    ("ab", "ba", None),
    ("abc", "cba", None),
    ("racecar", "racecar", None),
    ("  hola  ", "  aloh  ", None),
    ("12345", "54321", None),
    ("áéíóú", "úóíéá", None),
    ("Hello World!", "!dlroW olleH", None),
    ("mañana", "anañam", None),
    (None, None, "Input must be a string"),
    (123, None, "Input must be a string"),
    (["a", "b"], None, "Input must be a string"),
    ({}, None, "Input must be a string"),
    (True, None, "Input must be a string"),
    *[generate_random_string() for _ in range(3)]
])
def mixed_cases_strings(request):
    return request.param


def test_reverse_string(mixed_cases_strings):
    s, expected, error_msg = mixed_cases_strings

    if error_msg:
        with pytest.raises(TypeError) as excinfo:
            reverse_string(s)
        assert str(excinfo.value) == error_msg
    else:
        result = reverse_string(s)
        assert result == expected