class Converter:
    def __init__(self, currencyDict, ApiResponse):
        self.currencyDict = currencyDict
        self.ApiResponse = ApiResponse

    def GetConvertedValue(self, currencyFrom, currencyTo, amount):
        # TODO - should work with every currency (that function works only if currencyFrom is EUR)
        value = amount * self.ApiResponse['rates'][currencyTo]
        return "{:.5f}".format(value)

    def GetUpdateDate(self):
        # TODO - get date and time
        return f"Last update: {self.ApiResponse['date']}"

    def Get1EuroInDollars(self):
        value = self.GetConvertedValue('EUR', 'USD', 1)
        return f"1 EUR = {value} USD"

    def Get1DollarInEuros(self):
        value = self.GetConvertedValue('EUR', 'USD', 1)
        return f"1 USD = {value} EUR"

    def GetConvertedValueString(self, currencyFrom, currencyTo, amount):
        return f"{amount} {currencyFrom} = {self.GetConvertedValue(currencyFrom, currencyTo, amount)} {currencyTo}"