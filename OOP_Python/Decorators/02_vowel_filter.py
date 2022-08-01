def vowel_filter(function):
    def wrapper():
        letters = function()
        return [letter for letter in letters if letter.lower() in 'aeouiy']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
