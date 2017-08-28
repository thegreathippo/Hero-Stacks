from kvy import App
from kvy import ScreenManager


class GameApp(App):

    def build(self):
        return MainWindow()


class MainWindow(ScreenManager):
    pass


