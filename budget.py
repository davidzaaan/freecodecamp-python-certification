import time
class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __repr__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger: 
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total += item['amount']

        displayer = title + items + "Total: " + str(total)
        return displayer


    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description })

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({ 'amount': (amount * -1), 'description': description })
            return True
        else:
            return False

    def get_balance(self):
        total_funds = sum(item['amount'] for item in self.ledger)
        return round(total_funds, 2)

    def transfer(self, amount, budget_category):
        try:
            transfer = self.withdraw(amount, f"Transfer to {budget_category.category}")
            if not transfer:
                raise ValueError("Transaction could not be done successfully because you don't have enough funds")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        except ValueError:
            return False


    def check_funds(self, amount):
        return amount <= self.get_balance()

    ##### functions helpful to make the chart #####
    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item['amount'] < 0:
                total += item['amount']
        return total





def truncate(number):
    multiplier = 10
    return int(number * multiplier) / multiplier


def get_totals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())
    rounded = list(map(lambda x: truncate(x / total), breakdown))
    return rounded


def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = get_totals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i -= 10

    dashes = '-' + '---' * len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.category)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        name_str = '    '
        for name in names:
            if x >= len(name):
                name_str += "   "
            else:
                name_str += name[x] + "  "

        if (x != len(maxi) - 1):
            name_str += '\n'

        x_axis += name_str

    res += dashes.rjust(len(dashes) + 4) + '\n' + x_axis
    return res



start = time.time()
f = Category('Clothing')
a = Category('Food')
print(f.deposit(1000, 'initial deposit'))
print(a.deposit(1000, 'initial deposit'))
print(f.withdraw(10.15, 'groceries'))
print(f.withdraw(15.89, 'restaurant and more food'))
print(f.transfer(15, a))
print(a.transfer(15.43, f))
print(f.transfer(0.43, a))
print(f)
print(a)
end = time.time()
print(end - start)
print(create_spend_chart([a, f]))
