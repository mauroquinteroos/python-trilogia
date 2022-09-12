import os
import random


def read_words(filepath="./files/data.txt"):
    data = []
    with open(filepath) as data_file:
        data =  list(map(lambda line: line.strip().upper(), data_file))
    return data


def run():
    words = read_words()

    chosen_word = random.choice(words)
    print(chosen_word)

    chosen_word_list = [letter for letter in chosen_word]

    empty_words = ["_"]
    empty_words_underscore = empty_words * len(chosen_word)

    word_dict = {}
    for index, letter in enumerate(chosen_word):
        if not word_dict.get(letter):
            word_dict[letter] = []
        word_dict[letter].append(index)

    while True:
        os.system("clear")
        print("¡Adivina la palabra!")
        for element in empty_words_underscore:
            print(element, end=" ")
        print("\n")

        letter = input("Ingrese una letra: ").upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for index in word_dict[letter]:
                empty_words_underscore[index] = letter

        if "_" not in empty_words_underscore:
            os.system("clear")
            print(f"¡Ganaste, la palabra era {chosen_word}!")
            break


if __name__ == '__main__':
    run()