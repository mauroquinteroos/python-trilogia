def palindrome(word):
    try:
        if len(word) == 0:
            # Sirve para elevar una excepción del tipo ValueError
            # Se le pasa un mensaje del error
            raise ValueError("No se puede ingresar una cadena vacía")
        return word == word[::-1]
    # el keyword as sirve para ponerle un nombre al error
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        print(palindrome(""))
    # Si sucede un error del tipo TypeError se ejecuta lo que está dentro del except
    except TypeError:
        print("Solo se pueden ingresar strings")
    finally:
        # Cerrar un archivo dentro de python
        # Cerrar una conexión a la BD
        print("Siempre se ejecuta esta línea!")


if __name__ == '__main__':
    run()