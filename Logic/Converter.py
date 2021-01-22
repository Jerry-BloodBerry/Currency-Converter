from datetime import datetime


class Converter:
    def __init__(self, ApiResponse):
        self.ApiResponse = ApiResponse

    def GetConvertedValue(self, currencyFrom, currencyTo, amount):
        if currencyFrom == 'EUR':
            value = amount * self.ApiResponse['rates'][currencyTo]
        elif currencyTo == 'EUR':
            value = amount * (1 / self.ApiResponse['rates'][currencyFrom])
        else:
            value = amount * self.ConvertBetweenCurrencies(currencyFrom, currencyTo)

        return "{:.5f}".format(value)

    def ConvertBetweenCurrencies(self, currencyFrom, currencyTo):
        return self.ApiResponse['rates'][currencyTo] / self.ApiResponse['rates'][currencyFrom]

    def GetUpdateDate(self):
        return f"Last update: {self.ApiResponse['date']} {str(datetime.fromtimestamp(int(self.ApiResponse['timestamp']))).split()[1]}"

    def Get1EuroInDollars(self):
        value = self.GetConvertedValue('EUR', 'USD', 1)
        return f"1 EUR = {value} USD"

    def Get1DollarInEuros(self):
        value = self.GetConvertedValue('USD', 'EUR', 1)
        return f"1 USD = {value} EUR"

    def GetConvertedValueString(self, currencyFrom, currencyTo, amount):
        return f"{amount} {currencyFrom} = {self.GetConvertedValue(currencyFrom, currencyTo, amount)} {currencyTo}"
