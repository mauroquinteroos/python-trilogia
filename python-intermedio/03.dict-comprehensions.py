def run():
    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i ** 3

    print(my_dict)
    print("Result: %s" % len(my_dict))

    print("----\n")

    # Dict Comprehensions
    my_custom_dict = {f"valor_{i}": i ** 3 for i in range(1, 101) if i % 3 != 0}
    print(my_custom_dict)
    print("Result: %s" % len(my_custom_dict))


if __name__ == '__main__':
    run()