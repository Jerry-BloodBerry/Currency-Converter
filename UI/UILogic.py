from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

exampleCurrencies = {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        "EUR": "Euro",
        "AMD": "Armenian Dram"
}
exampleApiResponse = {
    "success": True,
    "timestamp": 1519296206,
    "base": "EUR",
    "date": "2021-01-11",
    "rates": {
        "AUD": 1.566015,
        "CAD": 1.560132,
        "CHF": 1.154727,
        "CNY": 7.827874,
        "GBP": 0.882047,
        "JPY": 132.360679,
        "USD": 1.23396
    }
}


def Convert(instance):
    return 1.56


def DropDownCurrencyButton(currencyDict=exampleCurrencies):
    dropdown = DropDown()
    for currencySymbol in currencyDict.keys():
        btnText = f"{currencySymbol}: {currencyDict[currencySymbol]}"
        btn = Button(text=btnText, size_hint_y=None, height=35)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
    btnText = f"EUR: {currencyDict['EUR']}"
    mainButton = Button(text=btnText, size_hint=(None, None))
    mainButton.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(mainButton, 'text', x))
    return mainButton

