

















def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def sum_positive_numbers(numbers):
    positive_sum = 0
    for num in numbers:
        if num > 0:
            positive_sum += num
    return positive_sum

def find_largest_string(strings):
    if len(strings) == 0:
        return ""

    largest_string = strings[0]
    for s in strings:
        if len(s) > len(largest_string):
            largest_string = s
    return largest_string

def count_occurrences(numbers):
    occurrences = {}
    for num in numbers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    return occurrences



import unittest
from exercise import *

class TestFunctions(unittest.TestCase):

    def test_filter_even_numbers(self):
        # Students write their tests here
        # TODO: Write a test for a list that only has odd numbers.
        self.assertEqual(filter_even_numbers([1, 3, 5, 7]), [])
        
        # TODO: Write a test for an empty list.
        self.assertEqual(filter_even_numbers([]), [])
        
        # TODO: Write a test for a list that starts with zero.
        self.assertEqual(filter_even_numbers([0, 1, 2, 3, 4]), [0, 2, 4])

    def test_sum_positive_numbers(self):
        # Students write their tests here
        # TODO: Write a test for a list with positive and negative numbers.
        self.assertEqual(sum_positive_numbers([-3, -2, 1, 2, 3]), 6)
        
        # TODO: Write a test for a list with all negative numbers.
        self.assertEqual(sum_positive_numbers([-3, -2, -1]), 0)
        
        # TODO: Write a test for an empty list.
        self.assertEqual(sum_positive_numbers([]), 0)

    def test_find_largest_string(self):
        # Students write their tests here
        # TODO: Write a test for a list where the largest string is at the beginning.
        self.assertEqual(find_largest_string(["apple", "banana", "cherry"]), "banana")
        
        # TODO: Write a test for a list where the largest string is in the middle.
        self.assertEqual(find_largest_string(["apple", "blueberry", "cherry"]), "blueberry")
        
        # TODO: Write a test for an empty list.
        self.assertEqual(find_largest_string([]), "")

    def test_count_occurrences(self):
        # Students write their tests here
        # TODO: Write a test for a list with multiple occurrences of the same number.
        self.assertEqual(count_occurrences([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})
        
        # TODO: Write a test for a list with no repeated numbers.
        self.assertEqual(count_occurrences([1, 2, 3]), {1: 1, 2: 1, 3: 1})
        
        # TODO: Write a test for an empty list.
        self.assertEqual(count_occurrences([]), {})

if __name__ == '__main__':
    unittest.main()
