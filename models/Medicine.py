from models.goodsofpharmacy import GoodsOfPharmacy
from models.Quality import Quality
from models.TypeOfGood import TypeOfGood
from models.MedicineType import MedicineType

class Medicine(GoodsOfPharmacy):

    def __init__(self,
                priceOfGood = 0,
                nameOfGood = "NoName",
                qualityOfGood = "NoName",
                amountOfCustomersPerDay = 0,
                typeOfGood = "NoName",
                amountOfMedicine = 0,
                producingCountry = "NoName",
                typeOfMedicine = "NoName"):
        super().__init__(priceOfGood, nameOfGood,
                         Quality.PERFECT, amountOfCustomersPerDay,
                         TypeOfGood.MEDICINE)
        self.amountOfMedicine = amountOfMedicine
        self.producingCountry = producingCountry
        self.typeOfMedicine = typeOfMedicine
        
        
