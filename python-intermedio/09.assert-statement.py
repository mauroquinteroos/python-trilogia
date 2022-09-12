def divisors(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return divisors

def run():
    num = input("Ingrese un número: ")
    assert num.isnumeric(), "Debe ingresar un Número"

    print(divisors(int(num)))


if __name__ == '__main__':
    run()