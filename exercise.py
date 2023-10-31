def filter_even_numbers(numbers):
    """
    Returns a list containing only the even numbers from the given list.

    Input: 
    numbers: a list of integers.

    Output: 
    A list containing only the even integers from the input list.

    Example:
    >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    pass

def sum_positive_numbers(numbers):
    """
    Returns the sum of all positive numbers in the list.

    Input: 
    numbers: a list of integers.

    Output: 
    An integer representing the sum of all positive integers in the input list.

    Example:
    >>> sum_positive_numbers([-1, 1, -2, 2, -3, 3])
    6
    """
    pass

def find_largest_string(strings):
    """
    Returns the largest string (by character count) from the given list.
    If two strings have the same length, return the first one.
    If the list is empty, return an empty string.

    Input: 
    strings: a list of strings.

    Output: 
    A string representing the longest string in the list.

    Example:
    >>> find_largest_string(["apple", "banana", "cherry"])
    "banana"
    """
    pass

def count_occurrences(numbers):
    """
    Returns a dictionary where the keys are numbers and the values are the number of times
    each number appears in the given list.

    Input: 
    numbers: a list of integers.

    Output: 
    A dictionary where each key is an integer from the input list and its corresponding value is its count.

    Example:
    >>> count_occurrences([1, 2, 2, 3, 3, 3])
    {1: 1, 2: 2, 3: 3}
    """
    pass


def driver():
    while True:
        print("Choose a function to test:")
        print("1. Filter even numbers from a list.")
        print("2. Sum positive numbers from a list.")
        print("3. Find the largest string from a list of strings.")
        print("4. Count occurrences of numbers in a list.")
        print("5. Exit.")
        
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print(filter_even_numbers(numbers))

        elif choice == "2":
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print(sum_positive_numbers(numbers))

        elif choice == "3":
            strings = input("Enter strings separated by commas: ").split(", ")
            print(find_largest_string(strings))

        elif choice == "4":
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print(count_occurrences(numbers))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    driver()
