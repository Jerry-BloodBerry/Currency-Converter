from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config
from kivy.core.window import Window
from UILogic import Convert, DropDownCurrencyButton
Config.set('graphics', 'width', 900)
Config.set('graphics', 'height', 500)
Window.clearcolor = (0, 0.4, 0.6, 1)


class Header(GridLayout):
    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        self.cols = 1
        self.padding = [0, 10]
        self.add_widget(Label(text='Accurate Currency Converter'))


class ConverterPanel(GridLayout):
    def __init__(self, **kwargs):
        super(ConverterPanel, self).__init__(**kwargs)
        self.border = (10,10,10,10)
        self.cols = 5
        self.padding = [60, 30]
        self.add_widget(Label(text='Amount'))
        self.add_widget(Label(text='From'))
        self.add_widget(Label())
        self.add_widget(Label(text='To'))
        self.add_widget(Label(text=''))
        self.amountInput = TextInput(multiline=False, focus=True, allow_copy=True)
        self.add_widget(self.amountInput)
        currencyFromButton = DropDownCurrencyButton()
        currencyToButton = DropDownCurrencyButton()
        self.add_widget(currencyFromButton)
        switchButton = Button(background_normal='switch_icon.png')
        self.add_widget(switchButton)
        self.add_widget(currencyToButton)
        self.convertButton = Button(text='Convert')
        self.convertButton.bind(on_press=Convert)
        self.add_widget(self.convertButton)


class ResultPanel(AnchorLayout):
    def __init__(self, **kwargs):
        super(ResultPanel, self).__init__(**kwargs)


class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.cols = 1
        self.padding = [10, 10]
        self.add_widget(Header())
        self.add_widget(ConverterPanel())
        self.add_widget(ResultPanel())


class Program(App):
    def build(self):
        return MainWindow()


Program().run()
