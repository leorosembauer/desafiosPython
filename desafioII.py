def is_fibonacci(num):
    fib1 = 0
    fib2 = 1
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
    return fib2 == num

def main():
    try:
        num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        if is_fibonacci(num):
            print(f"O número {num} faz parte da sequência de Fibonacci.")
        else:
            print(f"O número {num} não faz parte da sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()