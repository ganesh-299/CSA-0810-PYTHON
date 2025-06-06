# 1) Check if a number is a palindrome:
num = int(input("Enter a number: "))
if str(num) == str(num)[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# 2)   Tower of Hanoi using recursion:   
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')
# 3) Print numbers 1 to 10, break at 5:
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# 4) Staircase problem (distinct ways to climb stairs):
def climb_stairs(n):
    if n <= 1:
        return 1
    return climb_stairs(n-1) + climb_stairs(n-2)

n = 4
print(f"Distinct ways to climb {n} steps: {climb_stairs(n)}")
# 5) Average of positive and negative numbers until -1:
positives = []
negatives = []

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num > 0:
        positives.append(num)
    else:
        negatives.append(num)

if positives:
    print(f"Average of positive numbers: {sum(positives)/len(positives):.2f}")
if negatives:
    print(f"Average of negative numbers: {sum(negatives)/len(negatives):.2f}")
# 6)Convert integer to Roman numeral:
def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman += sym[i]
            num -= val[i]
    return roman

num = int(input("Enter an integer: "))
print(f"Roman numeral: {int_to_roman(num)}")
# 7) Remove all even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [num for num in numbers if num % 2 != 0]
print("List after removing even numbers:", filtered)
# 8) Find max and min in a tuple:
t = (4, 2, 9, 1, 7)
print("Max:", max(t))
print("Min:", min(t))
# 9) Length of a dictionary:
d = {'a': 1, 'b': 2, 'c': 3}
print("Length of dictionary:", len(d))
# 10) Frequency of all elements in a dictionary:
d = {'a': 1, 'b': 2, 'a': 1, 'c': 2, 'b': 2}
from collections import Counter
freq = Counter(d.values())
print("Frequency of values:", dict(freq))














