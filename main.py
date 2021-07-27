from kivy.app import App

from API.currency_api import get_available_currencies, get_latest_rates
from Logic.Converter import Converter
from UI.UI import MainWindow


class ConverterApp(App):
    def build(self):
        self.title = 'Quite Accurate Currency Converter'
        currencyDict = get_available_currencies()
        ratesDict = get_latest_rates()
        if not currencyDict['success']:
            ratesDict = currencyDict
        elif not ratesDict['success']:
            currencyDict = ratesDict
        converter = Converter(ratesDict)
        return MainWindow(currencyDict, converter)


ConverterApp().run()
