# --------------------------------------------------------Import Section-------------------------------------------------------------------------------------#

from kivy.config import Config
Config.set('graphics', 'resizable', True)
import psutil
from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import requests

#-------------------------------------------------------------Setting up global variables------------------------------------------------------------------#
global networkInterfaces
api_uri = "http://127.0.0.1:5000"
addrs = psutil.net_if_addrs() 
networkInterfaces = list(addrs.keys())
#---------------------------------------------------------Application class------------------------------------------------------------------------------#
class NetworkTrafficAnalyzer(App):
    def build(self):
        layout = FloatLayout()

        self.spinnero = Spinner(text = "Select the interface : ", values = networkInterfaces)
        self.spinnero.size_hint = (0.3, 0.2)
        self.spinnero.pos_hint ={'x': .35, 'y':.75}
        layout.add_widget(self.spinnero)
        self.spinnero.bind(text = self.on_spinner_select)
        self.spinnerSelection = Label(text ="%s" %self.spinnero.text)
  
        layout.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint ={'x': .01, 'y':.2}

        self.button1 = Button(text = "Scan" , )
        self.button1.size_hint = (0.25, 0.1)
        self.button1.pos_hint = {'x': 0.05 , 'y':.40}
        self.button1.bind(on_press = self.pressed)
        layout.add_widget(self.button1)

        return layout


    
    def on_spinner_select(self,spinner,text):
        self.spinnerSelection.text = "Selected interface is: %s"%self.spinnero.text
    def pressed(self,instance):
        networkInterface = self.spinnero.text
        send_data = {"networkInterface":networkInterface}
        
        header = {"Content-type":"application/json"}
        response = requests.post(api_uri+"/saveascsv",json = send_data,headers = header)
        print(response.content)
        
    
    
    
if __name__ == "__main__":
    NetworkTrafficAnalyzer().run()


    
