def run():
    squares = []

    for i in range(1, 101):
        squares.append(i ** 2)

    print(squares)
    print("Result: %s" % len(squares))

    print("----\n")

    # List Comprehensions
    custom_squares = [(i ** 2) for i in range(1, 101) if (i % 3) != 0]
    print(custom_squares)
    print("Result: %s" % len(custom_squares))


if __name__ == '__main__':
    run()