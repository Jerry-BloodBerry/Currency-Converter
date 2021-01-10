from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.config import Config
from kivy.core.window import Window
Config.set('graphics', 'width', 900)
Config.set('graphics', 'height', 500)
Window.clearcolor = (0, 0.4, 0.6, 1)


class Header(GridLayout):
    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        self.cols = 1
        self.padding = [0, 10]
        self.add_widget(Label(text='Accurate Currency Converter'))


def DropDownCurrencyList():
    dropdown = DropDown()
    for index in range(10):
        # When adding widgets, we need to specify the height manually
        # (disabling the size_hint_y) so the dropdown can calculate
        # the area it needs.

        btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

        # for each button, attach a callback that will call the select() method
        # on the dropdown. We'll pass the text of the button as the data of the
        # selection.
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))

        # then add the button inside the dropdown
        dropdown.add_widget(btn)
    mainbutton = Button(text='Hello', size_hint=(None, None))

    # show the dropdown menu when the main button is released
    # note: all the bind() calls pass the instance of the caller (here, the
    # mainbutton instance) as the first argument of the callback (here,
    # dropdown.open.).
    mainbutton.bind(on_release=dropdown.open)
    # one last thing, listen for the selection in the dropdown list and
    # assign the data to the button text.
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
    return mainbutton


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
        self.add_widget(DropDownCurrencyList())
        switchButton = Button(background_normal='switch_icon.png')
        self.add_widget(switchButton)
        self.add_widget(DropDownCurrencyList())
        self.convertButton = Button(text='Convert')
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
