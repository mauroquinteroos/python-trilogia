def read():
    numbers = []

    with open("./files/number.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)

def write():
    names = ["Mauro", "Facundo", "Miguel", "Angie", "Andrea", "Rocío", "Iñigo"]

    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def append():
    names = ["Thalia", "Freddy", "Silvia"]

    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    append()


if __name__ == '__main__':
    run()