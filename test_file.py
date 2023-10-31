import unittest
import exercise
import test  # This is where student's tests will be

# Mock incorrect implementations
def filter_even_numbers_bad(numbers):
    return numbers

def filter_even_numbers_bad_skip_first(numbers):
    return numbers[1:]

def sum_positive_numbers_bad(numbers):
    return sum(numbers)

def sum_positive_numbers_bad_abs(numbers):
    return sum(map(abs, numbers))

def find_largest_string_bad_last(strings):
    return strings[-1] if strings else ""

def find_largest_string_bad(strings):
    return strings[0] if strings else ""

def count_occurrences_bad(numbers):
    return {}

def count_occurrences_bad_double(numbers):
    return {num: 2 for num in numbers}

# Replacing the functions in exercise with bad implementations
exercise.filter_even_numbers = filter_even_numbers_bad
exercise.sum_positive_numbers = sum_positive_numbers_bad
exercise.find_largest_string = find_largest_string_bad
exercise.count_occurrences = count_occurrences_bad
exercise.filter_even_numbers = filter_even_numbers_bad_skip_first
exercise.sum_positive_numbers = sum_positive_numbers_bad_abs
exercise.find_largest_string = find_largest_string_bad_last
exercise.count_occurrences = count_occurrences_bad_double

from importlib import reload
reload(test)

class TestMeta(unittest.TestCase):

    def test_student_tests(self):
        suite = unittest.defaultTestLoader.loadTestsFromModule(test)
        results = unittest.TestResult()
        suite.run(results)

        # If student's tests failed for bad implementations, that's good.
        self.assertGreater(len(results.failures), 0, "Student tests did not catch the bad implementations!")

if __name__ == '__main__':
    unittest.main()
