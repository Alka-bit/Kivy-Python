import kivy
from kivy.app import App
kivy.require('2.0.0')
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.label import Label 

class MultipleLayout(PageLayout):
    pass
class App1(App):
    def build(self):
        return Label(text="Hello World!")
        
MlApp = App1()

MlApp.run()