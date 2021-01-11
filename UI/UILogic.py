from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class UILogic:
    def __init__(self, currencyDict, ApiResponse):
        self.currencyDict = currencyDict
        self.ApiResponse = ApiResponse

    def DropDownCurrencyButton(self, defaultCurrency):
        dropdown = DropDown()
        for currencySymbol in self.currencyDict.keys():
            btnText = f"{currencySymbol}: {self.currencyDict[currencySymbol]}"
            btn = Button(text=btnText, size_hint_y=None, height=35)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        btnText = f"{defaultCurrency}: {self.currencyDict[defaultCurrency]}"
        mainButton = Button(text=btnText, size_hint=(None, None))
        mainButton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainButton, 'text', x))
        return mainButton

    def GetConvertedValue(self, currencyFrom, currencyTo, amount):
        return amount*self.ApiResponse['rates'][currencyTo]

    def GetUpdateDate(self):
        return f"Last update: {self.ApiResponse['date']}"

    def Get1EuroInDollars(self):
        value = self.GetConvertedValue('EUR', 'USD', 1)
        return f"1 EUR = {value} USD"

    def Get1DollarInEuros(self):
        value = self.GetConvertedValue('EUR', 'USD', 1)
        return f"1 USD = {value} EUR"

    def GetConvertedValueString(self, currencyFrom, currencyTo, amount):
        return f"{amount} {currencyFrom} = {self.GetConvertedValue(currencyFrom, currencyTo, amount)} {currencyTo}"