class PharmacyManager:

    def __init__(self, goods = None):
        self.goods = goods

    def find_by_price(self, priceOfGood):
        filteredList = []
        for good in self.goods:
            if good.priceOfGood <= priceOfGood:
                filteredList.append(good)
        return filteredList

    @staticmethod
    def sort_by_amount_of_customers_per_day_by_increase(goods):
        return sorted(goods, key = lambda x: x.amountOfCustomersPerDay)

    @staticmethod
    def sort_by_amount_of_customers_per_day_by_decrease(goods):
        return sorted(goods, key = lambda x: x.amountOfCustomersPerDay, reverse = True)

    @staticmethod
    def sort_by_name_of_good_by_increase(goods):
        return sorted(goods, key = lambda x: x.nameOfGood)

    @staticmethod
    def sort_by_name_of_good_by_decrease(goods):
        return sorted(goods, key = lambda x: x.nameOfGood, reverse = True)
                
