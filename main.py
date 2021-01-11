from kivy.app import App
from Logic.Converter import Converter
from UI.UI import MainWindow

exampleCurrencies = {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        "EUR": "Euro",
        "AMD": "Armenian Dram",
        "USD": "US Dollar"
}
exampleApiResponse = {
    "success": True,
    "timestamp": 1519296206,
    "base": "EUR",
    "date": "2021-01-11",
    "rates": {
        "AED": 1.566015,
        "AFN": 1.560132,
        "ALL": 1.154727,
        "AMD": 7.827874,
        "USD": 4.323345
    }
}


class Program(App):
    def build(self):
        converter = Converter(exampleCurrencies, exampleApiResponse)
        return MainWindow(exampleCurrencies, converter)


Program().run()