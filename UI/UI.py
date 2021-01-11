from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config
from kivy.core.window import Window
from UILogic import DropDownCurrencyButton, GetConvertedValue, GetUpdateDate, Get1EuroInDollars, Get1DollarInEuros, GetConvertedValueString
Config.set('graphics', 'width', 900)
Config.set('graphics', 'height', 500)
Window.clearcolor = (0, 0.4, 0.6, 1)


class Header(GridLayout):
    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        self.cols = 1
        self.padding = [0, 10]
        self.add_widget(Label(text='Accurate Currency Converter'))


class MainPanel(GridLayout):
    def __init__(self, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        self.converterPanel = GridLayout(cols=5)
        self.add_widget(self.converterPanel)
        #self.convertedValue = 1
        self.currencyFrom = 'EUR'
        self.currencyTo = 'EUR'
        self.converterPanel.add_widget(Label(text='Amount'))
        self.converterPanel.add_widget(Label(text='From'))
        self.converterPanel.add_widget(Label())
        self.converterPanel.add_widget(Label(text='To'))
        self.converterPanel.add_widget(Label(text=''))
        self.amountInput = TextInput(multiline=False, allow_copy=True)
        self.converterPanel.add_widget(self.amountInput)
        self.currencyFromButton = DropDownCurrencyButton('EUR')
        self.currencyToButton = DropDownCurrencyButton('USD')
        self.converterPanel.add_widget(self.currencyFromButton)
        switchButton = Button(background_normal='switch_icon.png')
        self.converterPanel.add_widget(switchButton)
        self.converterPanel.add_widget(self.currencyToButton)
        self.convertButton = Button(text='Convert')
        self.converterPanel.add_widget(self.convertButton)
        self.convertButton.bind(on_press=self.Convert)
        self.resultPanel = GridLayout(cols=1)
        self.add_widget(self.resultPanel)
        self.mainLabel = Label(text=Get1EuroInDollars())
        self.resultPanel.add_widget(self.mainLabel)
        self.labelUnit1 = Label(text=Get1DollarInEuros())
        self.resultPanel.add_widget(self.labelUnit1)
        self.innerGridLayout = GridLayout(cols=2)
        self.resultPanel.add_widget(self.innerGridLayout)
        self.labelUnit2 = Label(text=Get1EuroInDollars())
        self.dateOfUpdateLabel = Label(text=GetUpdateDate())
        self.innerGridLayout.add_widget(self.labelUnit2)
        self.innerGridLayout.add_widget(self.dateOfUpdateLabel)

    def Convert(self, instance):
        self.currencyFrom = self.currencyFromButton.text[0:3]
        self.currencyTo = self.currencyToButton.text[0:3]
        amount = float(self.amountInput.text)
        self.mainLabel.text = GetConvertedValueString(self.currencyFrom, self.currencyTo, amount)
        #self.labelUnit1.text = GetConvertedValueString(self.currencyTo, self.currencyFrom, 1)
        self.labelUnit2.text = GetConvertedValueString(self.currencyFrom, self.currencyTo, 1)
        self.dateOfUpdateLabel.text = GetUpdateDate()


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Header())
        self.mainPanel = MainPanel(cols=1)
        self.add_widget(self.mainPanel)


class Program(App):
    def build(self):
        return MainWindow()


Program().run()
