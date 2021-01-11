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
from UI.UILogic import UILogic
Config.set('graphics', 'width', 900)
Config.set('graphics', 'height', 500)
Window.clearcolor = (0, 0.4, 0.6, 1)
#Window.clearcolor = (1, 1, 1, 1)


class Header(GridLayout):
    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        self.cols = 1
        self.padding = [0, 10]
        self.add_widget(Label(text='Accurate Currency Converter'))


class MainPanel(GridLayout):
    def __init__(self, uiLogic, converter, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        self.converter = converter
        self.uiLogic = uiLogic
        self.converterPanel = GridLayout(cols=5)
        self.add_widget(self.converterPanel)
        self.currencyFrom = 'EUR'
        self.currencyTo = 'USD'
        self.amountInput = TextInput(multiline=False, allow_copy=True)
        self.currencyFromButton = self.uiLogic.DropDownCurrencyButton('EUR')
        self.currencyToButton = self.uiLogic.DropDownCurrencyButton('USD')
        self.switchButton = Button(background_normal='switch_icon.png')
        self.switchButton.bind(on_press=self.Switch)
        self.convertButton = Button(text='Convert')
        self.convertButton.bind(on_press=self.Convert)
        self.InitiateConverterPanel()

        self.resultPanel = GridLayout(cols=1)
        self.add_widget(self.resultPanel)
        self.mainLabel = Label(text=self.converter.Get1EuroInDollars())
        self.exchangeRateLabel1 = Label(text=self.converter.Get1DollarInEuros())
        self.innerGridLayout = GridLayout(cols=2)
        self.exchangeRateLabel2 = Label(text=self.converter.Get1EuroInDollars())
        self.dateOfUpdateLabel = Label(text=self.converter.GetUpdateDate())
        self.InitiateResultPanel()

    def Convert(self, instance):
        self.currencyFrom = self.currencyFromButton.text[0:3]
        self.currencyTo = self.currencyToButton.text[0:3]
        amount = float(self.amountInput.text)
        self.mainLabel.text = self.converter.GetConvertedValueString(self.currencyFrom, self.currencyTo, amount)
        #self.exchangeRateLabel1.text = self.converter.GetConvertedValueString(self.currencyTo, self.currencyFrom, 1)
        self.exchangeRateLabel2.text = self.converter.GetConvertedValueString(self.currencyFrom, self.currencyTo, 1)
        self.dateOfUpdateLabel.text = self.converter.GetUpdateDate()

    def Switch(self, instance):
        pass

    def InitiateConverterPanel(self):
        self.converterPanel.add_widget(Label(text='Amount'))
        self.converterPanel.add_widget(Label(text='From'))
        self.converterPanel.add_widget(Label())
        self.converterPanel.add_widget(Label(text='To'))
        self.converterPanel.add_widget(Label(text=''))
        self.converterPanel.add_widget(self.amountInput)
        self.converterPanel.add_widget(self.currencyFromButton)
        self.converterPanel.add_widget(self.switchButton)
        self.converterPanel.add_widget(self.currencyToButton)
        self.converterPanel.add_widget(self.convertButton)

    def InitiateResultPanel(self):
        self.resultPanel.add_widget(self.mainLabel)
        self.resultPanel.add_widget(self.exchangeRateLabel1)
        self.resultPanel.add_widget(self.innerGridLayout)
        self.innerGridLayout.add_widget(self.exchangeRateLabel2)
        self.innerGridLayout.add_widget(self.dateOfUpdateLabel)


class MainWindow(BoxLayout):
    def __init__(self, currencyDict, converter, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = (40, 30)
        self.add_widget(Header())
        uiLogic = UILogic(currencyDict)
        self.mainPanel = MainPanel(uiLogic, converter, cols=1)
        self.add_widget(self.mainPanel)


