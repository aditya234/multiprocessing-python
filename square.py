def square(number):
    result = number * number
    print(f"The number {number} squared to {result}")


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]

    for number in numbers:
        square(number)
