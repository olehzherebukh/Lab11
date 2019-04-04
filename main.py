from models.goodsofpharmacy import GoodsOfPharmacy
from models.Quality import Quality
from models.TypeOfGood import TypeOfGood
from models.MedicineType import MedicineType
from models.Food import Food
from models.VitaminType import VitaminType
from managers.PharmacyManager import PharmacyManager

goodNaN = GoodsOfPharmacy(122,
                                "NaN",
                                Quality.GOOD,
                                23,
                                TypeOfGood.NUTRITION)

goodPektolvan = GoodsOfPharmacy(80.49,
                                "Pektolvan",
                                Quality.BAD,
                                33,
                                TypeOfGood.MEDICINE)

goodAgusha = GoodsOfPharmacy(127.40,
                                "Agusha",
                                Quality.PERFECT,
                                63,
                                TypeOfGood.NUTRITION)

goodPingvin = GoodsOfPharmacy(130,
                                "Pingvin",
                                Quality.GOOD,
                                35,
                                TypeOfGood.VITAMINS)

goodSpray = GoodsOfPharmacy(21,
                                "Spray",
                                Quality.BAD,
                                23,
                                TypeOfGood.MEDICINE)

goodVaselin = GoodsOfPharmacy(151,
                                "Vaselin",
                                Quality.GOOD,
                                63,
                                TypeOfGood.MEDICINE)

goodMeril = GoodsOfPharmacy(162,
                                "Meril",
                                Quality.BAD,
                                34,
                                TypeOfGood.VITAMINS)

goods = [goodNaN, goodPektolvan, goodAgusha, goodPingvin, goodSpray, goodVaselin, goodMeril]
manager = PharmacyManager(goods)

for i in manager.find_by_price(123):
    print(i)

print("")

for i in manager.sort_by_amount_of_customers_per_day_by_increase(goods):
    print(i)

print("")

for i in manager.sort_by_amount_of_customers_per_day_by_decrease(goods):
    print(i)

print("")

for i in manager.sort_by_name_of_good_by_increase(goods):
    print(i)

print("")

for i in manager.sort_by_name_of_good_by_decrease(goods):
    print(i)
