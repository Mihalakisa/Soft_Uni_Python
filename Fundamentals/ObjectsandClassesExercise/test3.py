class MyPerson:
    _value = 50  # защитен обект с една или двойна _ от неволна промяна

    def __init__(self):
        pass


obj = MyPerson()
print(obj._value)
