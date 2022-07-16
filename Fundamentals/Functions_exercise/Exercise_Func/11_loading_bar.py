def loading_bar(num):
    if num == 100:
        print(f"{num}% Complete!")
        print("[%%%%%%%%%%]")
    else:
        percent = (num//10) * '%'
        dots = (10 - (num//10)) * '.'
        print(f"{num}% [{percent}{dots}]")
        print("Still loading...")


number = int(input())
loading_bar(number)
