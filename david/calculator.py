
def add(a, b) -> int:
    return a + b

def subtract(a, b) -> int:
    return a - b

def multiply(a, b) -> int:
    return a * b

def divide(a, b) -> float:
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b

def main():
    try:
        a = float(input("input number1: "))
        b = float(input("input number2: "))
        a = int(a)
        b = int(b)
    
        op = input("input operator: ")
        if op == '+':
            print("Result: ", add(a, b))
        elif op == '-':
            print("Result: ", subtract(a, b))
        elif op == '*':
            print("Result: ", multiply(a, b))
        elif op == '/':
            result = divide(a, b)
            if result is not None:
                print("Result: ", result)
        else:
            raise ValueError('')

    except ValueError:
        print("Invalid input number.")
        exit(1)


if __name__ == "__main__":
    main()


        
