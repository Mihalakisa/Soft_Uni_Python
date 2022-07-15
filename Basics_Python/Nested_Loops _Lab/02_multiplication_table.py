# за всяка стойност на първия множител (1 до 10)
#  -> всяка стойност на втория множител ( до 10)

for first in range(1, 11):
    for second in range(1, 11):
        print(f"{first} * {second} = {first * second}")