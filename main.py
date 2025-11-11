def main():
    """A simple calculator function."""
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)

            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)

            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)

            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(num1, "/", num2, "=", num1 / num2)
            
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()