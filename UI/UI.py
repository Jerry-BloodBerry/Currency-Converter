from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from UI.UILogic import UILogic
Window.clearcolor = (0, 0.4, 0.6, 1)
Window.size = (1000, 600)
#Window.clearcolor = (1, 1, 1, 1)


class Header(GridLayout):
    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        self.cols = 2
        self.padding = [0, 10, 0, 0]
        self.add_widget(Label(
            text='Quite Accurate Currency Converter',
            size_hint=(.5, 1),
            font_name='Roboto-Bold',
            font_size=23
        ))
        self.add_widget(Label(size_hint=(.5, 1)))


class MainPanel(BoxLayout):
    def __init__(self, uiLogic, converter, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        self.converter = converter
        self.uiLogic = uiLogic
        self.spacing = 30
        self.padding = [0, 10, 0, 0]
        self.converterPanel = GridLayout(cols=5, size_hint=(1, .2))
        self.add_widget(self.converterPanel)
        self.amountInput = TextInput(multiline=False, allow_copy=True)
        self.currencyFromButton = self.uiLogic.DropDownCurrencyButton('EUR')
        self.currencyToButton = self.uiLogic.DropDownCurrencyButton('USD')
        print(self.currencyToButton)
        self.switchButton = Button(background_normal='Resources/switch_icon.png')
        self.switchButton.bind(on_press=self.Switch)
        self.convertButton = Button(background_normal='Resources/convert_icon.png')
        self.convertButton.bind(on_press=self.Convert)
        self.InitiateConverterPanel()

        self.resultPanel = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, .8))
        self.add_widget(self.resultPanel)
        self.mainLabel = Label(text=self.converter.Get1EuroInDollars(), font_name='Roboto-Bold', font_size=32)
        self.exchangeRateLabel1 = Label(text=self.converter.Get1DollarInEuros(), font_name='Roboto-Bold', font_size=20)
        self.innerGridLayout = GridLayout(cols=3)
        self.exchangeRateLabel2 = Label(text=self.converter.Get1EuroInDollars(), font_name='Roboto-Bold', font_size=20,
                                        size_hint=(.4, 1))
        self.dateOfUpdateLabel = Label(text=self.converter.GetUpdateDate(), font_name='Roboto-Bold', font_size=14,
                                       size_hint=(.3, 1))
        self.InitiateResultPanel()

    def Convert(self, instance):
        currencyFrom = self.currencyFromButton.text[0:3]
        currencyTo = self.currencyToButton.text[0:3]
        amount = float(self.amountInput.text)
        self.mainLabel.text = self.converter.GetConvertedValueString(currencyFrom, currencyTo, amount)
        #self.exchangeRateLabel1.text = self.converter.GetConvertedValueString(currencyTo, currencyFrom, 1)
        self.exchangeRateLabel2.text = self.converter.GetConvertedValueString(currencyFrom, currencyTo, 1)
        self.dateOfUpdateLabel.text = self.converter.GetUpdateDate()

    def Switch(self, instance):
        tmp = self.currencyToButton.text
        print(type(tmp))
        self.currencyToButton.text = self.currencyFromButton.text
        self.currencyFromButton.text = tmp

    def InitiateConverterPanel(self):
        self.converterPanel.spacing = 5
        amountPanel = BoxLayout(orientation="vertical", spacing=10, size_hint=(.3, 1))
        self.converterPanel.add_widget(amountPanel)
        amountPanel.add_widget(Label(text='Amount', font_name='Roboto-Bold', font_size=18, size_hint=(1, .25)))
        amountPanel.add_widget(self.amountInput)

        currencyFromPanel = BoxLayout(orientation="vertical", spacing=10, size_hint=(.3, 1))
        self.converterPanel.add_widget(currencyFromPanel)
        currencyFromPanel.add_widget(Label(text='From', font_name='Roboto-Bold', font_size=18, size_hint=(1, .25)))
        currencyFromPanel.add_widget(self.currencyFromButton)

        switchPanel = BoxLayout(orientation="vertical", size_hint=(.1, 1))
        self.converterPanel.add_widget(switchPanel)
        switchPanel.add_widget(Label(size_hint=(1, .1)))
        switchPanel.add_widget(self.switchButton)

        currencyToPanel = BoxLayout(orientation="vertical", spacing=10, size_hint=(.3, 1))
        self.converterPanel.add_widget(currencyToPanel)
        currencyToPanel.add_widget(Label(text='To', font_name='Roboto-Bold', font_size=18, size_hint=(1, .25)))
        currencyToPanel.add_widget(self.currencyToButton)

        converterButtonPanel = BoxLayout(orientation="vertical", size_hint=(.1, 1))
        self.converterPanel.add_widget(converterButtonPanel)
        converterButtonPanel.add_widget(Label(size_hint=(1, .1)))
        converterButtonPanel.add_widget(self.convertButton)

    def InitiateResultPanel(self):
        self.resultPanel.add_widget(self.mainLabel)
        self.resultPanel.add_widget(self.exchangeRateLabel1)
        self.resultPanel.add_widget(self.innerGridLayout)
        self.innerGridLayout.add_widget(Label(text='', size_hint=(.3, 1)))
        self.innerGridLayout.add_widget(self.exchangeRateLabel2)
        self.innerGridLayout.add_widget(self.dateOfUpdateLabel)


class MainWindow(BoxLayout):
    def __init__(self, currencyDict, converter, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 30, 30, 35]
        self.spacing = 30
        self.add_widget(Header(size_hint=(1, .05)))
        uiLogic = UILogic(currencyDict)
        self.mainPanel = MainPanel(uiLogic, converter, orientation='vertical', size_hint=(1, .95))
        self.add_widget(self.mainPanel)


