from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class UILogic:
    def __init__(self, currencyDict):
        self.currencyDict = currencyDict

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
