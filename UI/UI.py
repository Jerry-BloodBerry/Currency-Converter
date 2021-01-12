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
import re
from ErrorHandling.errors import UIError
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
    def __init__(self, uiLogic, converter, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        self.converter = converter
        self.uiLogic = uiLogic
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
        self.currencyFromButton = self.uiLogic.DropDownCurrencyButton('EUR')
        self.currencyToButton = self.uiLogic.DropDownCurrencyButton('USD')
        self.converterPanel.add_widget(self.currencyFromButton)
        switchButton = Button(background_normal='switch_icon.png')
        self.converterPanel.add_widget(switchButton)
        switchButton.bind(on_press=self.Switch)
        self.converterPanel.add_widget(self.currencyToButton)
        self.convertButton = Button(text='Convert')
        self.converterPanel.add_widget(self.convertButton)
        self.convertButton.bind(on_press=self.Convert)
        self.resultPanel = GridLayout(cols=1)
        self.add_widget(self.resultPanel)
        self.mainLabel = Label(text=self.converter.Get1EuroInDollars())
        self.resultPanel.add_widget(self.mainLabel)
        self.labelUnit1 = Label(text=self.converter.Get1DollarInEuros())
        self.resultPanel.add_widget(self.labelUnit1)
        self.innerGridLayout = GridLayout(cols=2)
        self.resultPanel.add_widget(self.innerGridLayout)
        self.labelUnit2 = Label(text=self.converter.Get1EuroInDollars())
        self.dateOfUpdateLabel = Label(text=self.converter.GetUpdateDate())
        self.innerGridLayout.add_widget(self.labelUnit2)
        self.innerGridLayout.add_widget(self.dateOfUpdateLabel)

    def Convert(self, instance):
        self.currencyFrom = self.currencyFromButton.text[0:3]
        self.currencyTo = self.currencyToButton.text[0:3]
        match  = re.match(r'^[1-9][0-9]*|[0]*[1-9]+[0-9]*$',self.amountInput.text) #ROBOCZY REGEX DLA MARTY
        if match is None:
            self.mainLabel.text = "ZLY INPUT"
            self.amountInput.text=""
        else:
            amount = float(self.amountInput.text) 
            self.mainLabel.text = self.converter.GetConvertedValueString(self.currencyFrom, self.currencyTo, amount)
            
        #self.mainLabel.text = self.converter.GetConvertedValueString(self.currencyFrom, self.currencyTo, amount)
        #self.labelUnit1.text = self.converter.GetConvertedValueString(self.currencyTo, self.currencyFrom, 1)
        self.labelUnit2.text = self.converter.GetConvertedValueString(self.currencyFrom, self.currencyTo, 1)
        self.dateOfUpdateLabel.text = self.converter.GetUpdateDate()

    def Switch(self, instance):
        pass


class MainWindow(BoxLayout):
    def __init__(self, currencyDict, converter, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Header())
        uiLogic = UILogic(currencyDict)
        self.mainPanel = MainPanel(uiLogic, converter, cols=1)
        self.add_widget(self.mainPanel)


