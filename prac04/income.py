"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    incomes = []
    count_month = int(input("How many months? "))

    for month in range(1, count_month + 1):
        income = float(input("Enter income for month {} :".format(month)))
        incomes.append(income)
    print_report(incomes, count_month)

def print_report(incomes, count_month):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, count_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()