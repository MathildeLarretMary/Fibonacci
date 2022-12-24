"""
In mathematics, the Fibonacci sequence
is a sequence of integers in which each term is the sum of the two terms that precede it.
"""


def fibonacci() -> object:
    start = int(input("""First integer of Fibonacci sequence
>>>> """))

    limit = int(input("""How many numbers do you want for the Fibonacci sequence?
>>>> """))

    arr = [start]

    for i in range(limit - 1):
        arr.append(arr[i] + arr[i - 1])

    print(arr)


try:
    fibonacci()
except ValueError:
    print("ValueError : only numbers are available")
    fibonacci()
