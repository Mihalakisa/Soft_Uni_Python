# команда -> число под формата на текст или "Stop"
# повтарям: чета число + проверка дали е минимум
# спирам: команда == "Stop"
# продължавам: комдана != "Stop"
import sys

command = input()
min = sys.maxsize
while command != "Stop":
    # command -> число под формата на текст
    number = int(command)
    # проверка за минимум
    if number < min:
        min = number

    command = input()
else:
    # command == "Stop"
    print(min)