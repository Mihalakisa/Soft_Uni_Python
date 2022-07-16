def sorting_cheeses(**kwargs):
    '''
    This function sorts the cheeses by their quantity desc,
    then by name asc.
    Concats the string with the result and sorts the elements of the result
    quantity dsc for each cheese.
    return str -> the sorted result
    '''
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for name, quantities in sorted_cheeses:
        result += name + '\n'
        sorted_quantities = sorted(quantities, reverse=True)
        result += '\n'.join([str(x) for x in sorted_quantities]) + '\n'

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)