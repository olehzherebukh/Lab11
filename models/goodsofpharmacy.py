class GoodsOfPharmacy:

    def __init__(self,
                priceOfGood = 0,
                nameOfGood = "NoName",
                qualityOfGood = "NoName",
                amountOfCustomersPerDay = 0,
                typeOfGood = "NoName"):
        self.priceOfGood = priceOfGood
        self.nameOfGood = nameOfGood
        self.qualityOfGood = qualityOfGood
        self.amountOfCustomersPerDay = amountOfCustomersPerDay
        self.typeOfGood = typeOfGood

    def __str__(self):
        info = ("priceOfGood = " + str(self.priceOfGood) + ", " +
    "nameOfGood = " + str(self.nameOfGood) + ", " +
    "qualityOfGood = " + str(self.qualityOfGood) + ", " +
    "amountOfCustomersPerDay = " + str(self.amountOfCustomersPerDay) + ", " +
    "typeOfGood = " + str(self.typeOfGood))
        return info
