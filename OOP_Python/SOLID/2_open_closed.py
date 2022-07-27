# Open for modification close for extension


class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4
        # if there is many if's for checks for the average_grade discount the code might break eventually


# !<> Open for extension close for modification <>!
class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2


discount = AdditionalDiscount("Test", 200, 6)
print(discount.get_discount())

# In existing class we better NOT modify and
# put if's and elif's we better create a new class!
