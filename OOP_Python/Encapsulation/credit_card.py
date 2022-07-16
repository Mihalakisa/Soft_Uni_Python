class CreditCard:
    def __init__(self, number, exp_date, cvv, name, pin):
        self.number = number
        self.exp_date = exp_date
        self.cvv = cvv
        self.name = name
        self.__pin = pin  # __pin --> Private data <--  '__'

    # def get_info(self):
    #     return self.__pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return
        raise ValueError("Old pin is not correct")


card = CreditCard(12345566778, "2022-10", 256, "Test Name", 7887)
# print(card._CreditCard__pin)
card.change_pin(7887, 1234)
print(card._CreditCard__pin)
