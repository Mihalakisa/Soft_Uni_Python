# enables extensibility
def print_list(ll):
    # print(ll)
    # [print(x) for x in ll]
    [print(x) for x in ll if x is not None]


ll1 = [1, 2, 3, 4, 5, 6]
print("Printing first list")
print_list(ll1)

# ll2 = [6, 5, 4, 3, 2, 1]
ll2 = [6, 5, 4, 3, None, 2, 1, None]
print("Printing second list")
print_list(ll2)