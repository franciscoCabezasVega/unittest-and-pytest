import random
import string
import unittest

from src.practice_functions import add, is_even, greet, max_of_three, grade, average, find_max_length, \
    count_occurrences, safe_divide, reverse_string


class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(4, -5), -1)
        self.assertEqual(add(-6, 7), 1)
        self.assertEqual(add(-3, -4), -7)
        self.assertEqual(add(5, -5), 0)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(25, 17), 42)
        self.assertEqual(add(10, 100), 110)

    def test_add_subtests(self):
        test_cases = [
            (1, 2, 3),
            (4, -5, -1),
            (-6, 7, 1),
            (-3, -4, -7),
            (5, -5, 0),
            (0, 1, 1),
            (25, 17, 42),
            (10, 100, 110),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

class TestIsEven(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(4), True)
        self.assertEqual(is_even(-6), True)
        self.assertEqual(is_even(-3), False)
        self.assertEqual(is_even(5), False)
        self.assertEqual(is_even(0), True)

    def test_is_even_subtests(self):
        test_cases = [
            (1, False),
            (4, True),
            (-6, True),
            (-3, False),
            (5, False),
            (0, True)
        ]

        for a, expected in test_cases:
            with self.subTest(a=a, expected=expected):
                self.assertEqual(is_even(a), expected)

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Frank"), "Hello, Frank!")

class TestMaxOfThree(unittest.TestCase):
    def test_max_of_three(self):
        test_cases = [
            (1, 2, 3, 3),
            (5, 7, 1, 7),
            (-1, 0, -5, 0),
            (15, -29, 8, 15),
            (-7, -39, -1200, -7)
        ]

        for a, b, c, expected in test_cases:
            with self.subTest(a=a, b=b, c=c, expected=expected):
                self.assertEqual(max_of_three(a, b, c), expected)

class TestGrade(unittest.TestCase):

    def test_grade(self):
        test_cases = [
            (-1, ValueError),
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
            (101, ValueError),
        ]

        for score, expected in test_cases:
            with self.subTest(score=score):
                if expected == ValueError:
                    with self.assertRaises(ValueError):
                        grade(score)
                else:
                    self.assertEqual(grade(score), expected)

    def test_grade_cm(self):
        test_cases = [
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
        ]

        for score, expected in test_cases:
            with self.subTest(score=score):
                if score < 0 or score > 100:
                    with self.assertRaises(ValueError) as cm:
                        grade(score)
                    self.assertEqual(str(cm.exception), expected)
                else:
                    self.assertEqual(grade(score), expected)

class TestAverage(unittest.TestCase):

    def test_average(self):
        test_cases = [
            ([], ValueError),
            ([0], 0),
            ([1, 2, 3], 2),
            ([-1, 2, 0], 0.3333333333333333),
            ([-10, -20, -30], -20),
            ([300, 100, 200], 200)
        ]

        for item, expected in test_cases:
            with self.subTest(item=item):
                if expected == ValueError:
                    with self.assertRaises(ValueError):
                        average(item)
                else:
                    self.assertEqual(average(item), expected)

    def test_average_cm(self):
        test_cases = [
            ([], "List cannot be empty"),
            ([0], 0),
            ([1, 2, 3], 2),
            ([-1, 2, 0], 0.3333333333333333),
            ([-10, -20, -30], -20),
            ([300, 100, 200], 200)
        ]

        for item, expected in test_cases:
            with self.subTest(item=item):
                if not item:
                    with self.assertRaises(ValueError) as cm:
                        average(item)
                    self.assertEqual(str(cm.exception), expected)
                else:
                    self.assertEqual(average(item), expected)

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        test_cases = [
            ([], ValueError),
            (["hola"], "hola"),
            (["hola", "mundo"], "mundo"),
            (["hola", "mundo", "texto más largo ñamé"], "texto más largo ñamé"),
            (["ho  la  ", "mundo"], "ho  la  "),
        ]
        for item, expected in test_cases:
            with self.subTest(item=item):
                if expected == ValueError:
                    with self.assertRaises(ValueError):
                        find_max_length(item)
                else:
                    self.assertEqual(find_max_length(item), expected)

    def test_find_max_cm(self):
        test_cases = [
            ([], "List cannot be empty"),
            (["hola"], "hola"),
            (["hola", "mundo"], "mundo"),
            (["hola", "mundo", "texto más largo ñamé"], "texto más largo ñamé"),
            (["ho  la  ", "mundo"], "ho  la  "),
        ]
        for item, expected in test_cases:
            with self.subTest(item=item):
                if not item:
                    with self.assertRaises(ValueError) as cm:
                        find_max_length(item)
                    self.assertEqual(str(cm.exception), expected)
                else:
                    self.assertEqual(find_max_length(item), expected)

class TestCountOccurrences(unittest.TestCase):

    def test_count_occurrences(self):
        test_cases = [
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
        for item, expected in test_cases:
            with self.subTest(item=item):
                self.assertEqual(count_occurrences(item), expected)

    def test_count_occurrences_dynamic(self):
        dynamic_cases = [
            ([], {}),
            (["a"], {"a": 1}),
            (["a"] * 5, {"a": 5}),
            ([str(i % 3) for i in range(6)], {"0": 2, "1": 2, "2": 2}),
            (["ñ" if i % 2 == 0 else "á" for i in range(5)], {"ñ": 3, "á": 2}),
        ]
        for item, expected in dynamic_cases:
            with self.subTest(item=item):
                self.assertEqual(count_occurrences(item), expected)

    def test_count_occurrences_random(self):
        items = [random.choice(["a", "b", "c"]) for _ in range(1000)]
        result = count_occurrences(items)

        for letter in ["a", "b", "c"]:
            with self.subTest(letter=letter):
                expected_count = items.count(letter)
                self.assertEqual(result[letter], expected_count)

class TestSafeDivide(unittest.TestCase):

    def test_safe_divide_parametrized(self):
        test_cases = [
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
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                if b == 0:
                    with self.assertRaises(ZeroDivisionError) as cm:
                        safe_divide(a, b)
                    self.assertEqual(str(cm.exception), expected)
                else:
                    result = safe_divide(a, b)
                    self.assertEqual(round(result, 2), expected)

    def test_safe_divide_static(self):
        static_cases = [
            (10, 2, 5.0),
            (7, 3, 2.33),
            (-8, 2, -4.0),
            (8, -2, -4.0),
            (1, 3, 0.33),
            (2.5, 0.5, 5.0),
        ]
        for a, b, expected in static_cases:
            with self.subTest(a=a, b=b):
                result = safe_divide(a, b)
                self.assertEqual(round(result, 2), expected)

    def test_safe_divide_zero(self):
        zero_division_cases = [
            (1, 0),
            (-10, 0),
            (0, 0),
        ]
        for a, b in zero_division_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ZeroDivisionError) as cm:
                    safe_divide(a, b)
                self.assertEqual(str(cm.exception), "Cannot divide by zero")

    def test_safe_divide_random(self):
        a = round(random.uniform(-1000, 1000), 2)
        b = round(random.uniform(0.01, 1000), 2)
        expected = round(a / b, 2)
        result = safe_divide(a, b)
        self.assertEqual(round(result, 2), expected)

    def test_safe_divide_mixed(self):
        def generate_random_case():
            a = round(random.uniform(-1000, 1000), 2)
            b = round(random.uniform(0.01, 1000), 2)
            expected = round(a / b, 2)
            return a, b, expected, None

        mixed_cases = [
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
        ]

        for a, b, expected, error_msg in mixed_cases:
            with self.subTest(a=a, b=b):
                if error_msg:
                    with self.assertRaises(ZeroDivisionError) as cm:
                        safe_divide(a, b)
                    self.assertEqual(str(cm.exception), error_msg)
                else:
                    result = safe_divide(a, b)
                    self.assertEqual(round(result, 2), expected)

class TestReverseString(unittest.TestCase):

    def test_reverse_string_mixed(self):
        def generate_random_string():
            length = random.randint(1, 20)
            s = ''.join(random.choice(string.ascii_letters + string.digits + "áéíóúñ ") for _ in range(length))
            expected = s[::-1]
            return s, expected, None

        mixed_cases = [
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
        ]

        for s, expected, error_msg in mixed_cases:
            with self.subTest(s=s):
                if error_msg:
                    with self.assertRaises(TypeError) as cm:
                        reverse_string(s)
                    self.assertEqual(str(cm.exception), error_msg)
                else:
                    result = reverse_string(s)
                    self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
