from datetime import datetime

class Converter:
    def __init__(self, currencyDict, ApiResponse):
        self.currencyDict = currencyDict
        self.ApiResponse = ApiResponse

    def GetConvertedValue(self, currencyFrom, currencyTo, amount):
        if currencyFrom == 'EUR':
            value = amount * self.ApiResponse['rates'][currencyTo]
        elif currencyTo == 'EUR':
            value = amount * (1 / self.ApiResponse['rates'][currencyFrom])
        else:
            value = amount * self.ConvertBettwenCurrencies(currencyFrom, currencyTo)

        return "{:.5f}".format(value)

    def ConvertBettwenCurrencies(self, currencyFrom, currencyTo):
        return self.ApiResponse['rates'][currencyTo] / self.ApiResponse['rates'][currencyFrom]

    def GetUpdateDate(self):
        return f"Last update: {self.ApiResponse['date']} {str(datetime.fromtimestamp(int(self.ApiResponse['timestamp']))).split()[1]}"

    def Get1EuroInDollars(self):
        value = self.GetConvertedValue('EUR', 'USD', 1)
        return f"1 EUR = {value} USD"

    def Get1DollarInEuros(self):
        value = self.GetConvertedValue('EUR', 'USD', 1)
        return f"1 USD = {value} EUR"

    def GetConvertedValueString(self, currencyFrom, currencyTo, amount):
        return f"{amount} {currencyFrom} = {self.GetConvertedValue(currencyFrom, currencyTo, amount)} {currencyTo}"