from models.goodsofpharmacy import GoodsOfPharmacy
from models.Quality import Quality
from models.TypeOfGood import TypeOfGood
from models.VitaminType import VitaminType

class Vitamin(GoodsOfPharmacy):

    def __init__(self,
                priceOfGood = 0,
                nameOfGood = "NoName",
                qualityOfGood = "NoName",
                amountOfCustomersPerDay = 0,
                typeOfGood = "NoName",
                amountOfPills = 0,
                amountOfDifferentVitamins = 0,
                typeOfVitamin = "NoName"):
        super().__init__(priceOfGood, nameOfGood,
                         Quality.NORMAL, amountOfCustomersPerDay,
                         TypeOfGOod.VITAMIN)
        self.amountOfPills = amountOfPills
        self.amountOfDifferentVitamins = amountOfDifferentVitamins
        self.typeOfVitamin = typeOfVitamin
