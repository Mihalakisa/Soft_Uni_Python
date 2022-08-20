class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = toys_cost

    def sum_child_cost(self):
        result = 0
        for toy in self.toys_cost:
            result += toy
        return result + self.food_cost