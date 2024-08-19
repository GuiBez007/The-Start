from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import json

Window.size = (400, 600)

class Manager(ScreenManager):
    pass


# each screen just supports one unique object
# by this we use the boxlayout
class FirstScreen(Screen):
    def checkStatus(self):
        try:
            with open("status.json", "r") as fileJson:
                contentFile = json.load(fileJson)
        except:
            with open("status.json", "w") as fileJson:
                contentFile = {'Status': 1}
                json.dump(contentFile, fileJson)  # what I'll write and where = dump(what, where)

        if contentFile['Status'] == 1:
            App.get_running_app().root.transition.direction = 'left'
            App.get_running_app().root.current = 'beforeAlarm'


class BeforeCreateAlarm(Screen):
    pass


class CreateAlarm(Screen):
    pass


class TimerScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        return Manager()


MyApp().run()