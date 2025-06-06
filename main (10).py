# 1) Selection Sort and Merge Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
arr1 = [64, 25, 12, 22, 11]
selection_sort(arr1)
print("Selection Sort:", arr1)

arr2 = [64, 25, 12, 22, 11]
print("Merge Sort:", merge_sort(arr2))
# 2) Copy File Contents
def copy_file(src, dest):
    with open(src, 'r') as f_src:
        content = f_src.read()
    with open(dest, 'w') as f_dest:
        f_dest.write(content)
copy_file('source.txt', 'destination.txt')
# 3)  Python Package utilities
utilities/
│
├── __init__.py
├── math_utils.py
└── string_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()
from utilities import math_utils, string_utils
print("Addition:", math_utils.add(5, 3))
print("Subtraction:", math_utils.subtract(5, 3))
print("Uppercase:", string_utils.to_upper("hello"))
print("Lowercase:", string_utils.to_lower("HELLO"))
# 4) Module math_extended
import math

def square_root(n):
    return math.sqrt(n)

def gcd(a, b):
    return math.gcd(a, b)
import math_extended
num = int(input("Enter number for square root: "))
print("Square Root:", math_extended.square_root(num))

a = int(input("Enter first number for GCD: "))
b = int(input("Enter second number for GCD: "))
print("GCD:", math_extended.gcd(a, b))
# 5) Module file_operations
def write_to_file(filename):
    data = input("Enter text to write to file: ")
    with open(filename, 'w') as f:
        f.write(data)
def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    print("File contents:\n", content)
import file_operations
filename = "example.txt"
file_operations.write_to_file(filename)
file_operations.read_file(filename)
# 6) Real-time/Technical Applications with Exception Handling
# Divide by zero error handling
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero!"
    else:
        return result

# Voter's age validation
def check_voter_age(age):
    try:
        if age < 18:
            raise ValueError("Not eligible to vote.")
        return "Eligible to vote."
    except ValueError as e:
        return f"Error: {e}"
def validate_marks(marks):
    try:
        if not (0 <= marks <= 100):
            raise ValueError("Marks should be between 0 and 100.")
        return "Marks are valid."
    except ValueError as e:
        return f"Error: {e}"
# 7) Library Management System
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
library = {}
def add_book(book):
    library[book.isbn] = book
def borrow_book(isbn):
    if isbn in library and library[isbn].available:
        library[isbn].available = False
        return f"You have borrowed '{library[isbn].title}'."
    return "Book not available."
def borrowed_books():
    return [book.title for book in library.values() if not book.available]
def return_book(isbn):
    if isbn in library and not library[isbn].available:
        library[isbn].available = True
        return f"'{library[isbn].title}' has been returned."
    return "Book not found or not borrowed."
# 8) Quiz Application
# a. Represent a question
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

# b. Store questions in a list
quiz = [
    Question("Capital of France?", ["Paris", "London", "Rome"], "Paris"),
    Question("5 + 3?", ["6", "8", "10"], "8"),
]

# c, d, e. Run quiz
def run_quiz():
    score = 0
    for q in quiz:
        print(q.question)
        for idx, opt in enumerate(q.options, 1):
            print(f"{idx}. {opt}")
        user_input = int(input("Choose an option (1-3): ")) - 1
        if q.options[user_input] == q.answer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! Correct answer: {q.answer}\n")
    print(f"Quiz completed. Final Score: {score}/{len(quiz)}")
# 9)  Element-wise Addition and Multiplication of Two Matrices (NumPy)
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
addition = np.add(a, b)
multiplication = np.multiply(a, b)
print("Addition:\n", addition)
print("Multiplication:\n", multiplication)
# 10) Read CSV File Line-by-Line using csv Module
import csv
filename = 'example.csv'  # replace with your CSV file path
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))









































