# такса -> въвеждаме
# цена за кецове = такса - 40%
# цена за екип = цена за кецове - 20%
# цена за топка = цена за екип * 1/4
# цена за аксесоарите = цена за топка * 1/5
# разходи = такса + цена за кецове + цена за екип + цена за топка + цена за аксесоари
# печатаме разходите

tax_per_year = int(input())
#  може цена за кецове =  (1 - 0.4) * таксата
price_trainers = tax_per_year - 0.4 * tax_per_year
# може и (1 - 02) * екип
price_suit = price_trainers - 0.2 * price_trainers
# може и price_suit / 4
price_ball = 1/4 * price_suit
# или 1/5 * price_ball
price_acc = price_ball / 5

expenses = tax_per_year + price_trainers + price_suit + price_ball + price_acc
print(expenses)