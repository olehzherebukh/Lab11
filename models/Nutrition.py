from models.goodsofpharmacy import GoodsOfPharmacy
from models.Quality import Quality
from models.TypeOfGood import TypeOfGood
from models.Food import Food

class Nutrition(GoodsOfPharmacy):

    def __init__(self,
                priceOfGood = 0,
                nameOfGood = "NoName",
                qualityOfGood = "NoName",
                amountOfCustomersPerDay = 0,
                typeOfGood = "NoName",
                typeOfFood = "NoName",
                volumePerCan = 0,
                tasteOfFood = "NoName"):
        super().__init__(priceOfGood, nameOfGood,
                         Quality.GOOD, amountOfCustomersPerDay,
                         TypeOfGood.NUTRITION)
        self.typeOfFood = typeOfFood
        self.volumePerCan = volumePerCan
        self.tasteOfFood = tasteOfFood
