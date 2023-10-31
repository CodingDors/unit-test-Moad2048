import unittest
import exercise
import test  # This is where student's tests will be
from importlib import reload

# Mock incorrect implementations for filter_even_numbers
def filter_even_numbers_return_all(numbers):
    return numbers

def filter_even_numbers_skip_first(numbers):
    return numbers[1:]

def filter_even_numbers_return_odds(numbers):
    return [num for num in numbers if num % 2 != 0]


# Mock incorrect implementations for sum_positive_numbers
def sum_positive_numbers_return_all(numbers):
    return sum(numbers)

def sum_positive_numbers_return_absolute_sum(numbers):
    return sum(map(abs, numbers))

def sum_positive_numbers_return_negative_sum(numbers):
    return -sum(filter(lambda x: x > 0, numbers))


# Mock incorrect implementations for find_largest_string
def find_largest_string_return_last(strings):
    return strings[-1] if strings else ""

def find_largest_string_return_first(strings):
    return strings[0] if strings else ""

def find_largest_string_return_smallest(strings):
    return min(strings, key=len, default="")


# Mock incorrect implementations for count_occurrences
def count_occurrences_return_empty(numbers):
    return {}

def count_occurrences_double_everything(numbers):
    return {num: 2 for num in numbers}

def count_occurrences_return_zero_count(numbers):
    return {num: 0 for num in set(numbers)}


# List of bad implementations to test against
bad_implementations = [
    ('filter_even_numbers', filter_even_numbers_return_all),
    ('filter_even_numbers', filter_even_numbers_skip_first),
    ('filter_even_numbers', filter_even_numbers_return_odds),
    
    ('sum_positive_numbers', sum_positive_numbers_return_all),
    ('sum_positive_numbers', sum_positive_numbers_return_absolute_sum),
    ('sum_positive_numbers', sum_positive_numbers_return_negative_sum),
    
    ('find_largest_string', find_largest_string_return_last),
    ('find_largest_string', find_largest_string_return_first),
    ('find_largest_string', find_largest_string_return_smallest),
    
    ('count_occurrences', count_occurrences_return_empty),
    ('count_occurrences', count_occurrences_double_everything),
    ('count_occurrences', count_occurrences_return_zero_count),
]

class TestMeta(unittest.TestCase):

    def test_student_tests(self):
        failed_functions = []

        for func_name, bad_impl in bad_implementations:
            # Replace the function in exercise with the bad implementation
            setattr(exercise, func_name, bad_impl)
            
            # Reload the student tests to ensure the new implementation is used
            reload(test)

            # Run the relevant student test for the function
            suite = unittest.defaultTestLoader.loadTestsFromName(f"TestFunctions.test_{func_name}", test)
            results = unittest.TestResult()
            suite.run(results)

            # If the student's tests did not fail for a bad implementation, note it down
            if not len(results.failures):
                failed_functions.append(func_name)

        self.assertEqual(len(failed_functions), 0, f"Student tests did not unit test all scenarious: {', '.join(failed_functions)}. Please ensure these functions are properly tested!")
