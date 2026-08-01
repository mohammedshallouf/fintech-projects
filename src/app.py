def calculate_balance(income, expenses):
    return income - expenses


def main():
    print("AI Financial Expense Analyzer")
    print("-" * 32)

    try:
        income = float(input("Enter your monthly income: "))
        expenses = float(input("Enter your total monthly expenses: "))

        balance = calculate_balance(income, expenses)

        print(f"\nRemaining balance: {balance:.2f}")

        if balance > 0:
            print("Status: You are spending within your income.")
        elif balance == 0:
            print("Status: Your income equals your expenses.")
        else:
            print("Status: Your expenses are higher than your income.")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    main()
