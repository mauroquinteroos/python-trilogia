def run():
    my_list = [1, "Hello", True, 4.15]

    my_dict = {
        "first_name": "Mauro",
        "last_name": "Quinteros"
    }

    super_list = [
        {"first_name": "Mauro", "last_name": "Quinteros"},
        {"first_name": "Miguel", "last_name": "Torres"},
        {"first_name": "Susana", "last_name": "Martinez"},
        {"first_name": "Thalia", "last_name": "Garcia"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "integer_nums": [-2, -1, 0, 1, 2,],
        "floating_nums": [1.1, 1.2, 1.3, 1.4,],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for value in super_list:
        print(value)


if __name__ == '__main__':
    run()