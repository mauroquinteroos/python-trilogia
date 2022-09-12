from functools import reduce


def run():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(my_list)

    odd = [i for i in my_list if i % 2 != 0]
    print(odd)

    # Recibe 2 parametros: una lambda function y un iterable
    odd_filter = list(filter(lambda x: x % 2 != 0, my_list))
    print(odd_filter)

    squares = [i ** 2 for i in my_list]
    print(squares)

    # Recibe 2 parametros: una lambda function y un iterable
    squares_map = list(map(lambda x: x ** 2, my_list))
    print(squares_map)

    def calculate(x, y):
        if y % 2 == 0:
            return x * y
        else:
            return x + y

    my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    all_multiplied = reduce(lambda x, y: calculate(x, y), my_list_1)
    print(all_multiplied, type(all_multiplied))


if __name__ == '__main__':
    run()