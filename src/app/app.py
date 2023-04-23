import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from app.modules.signin.signin import Signin

class App(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(id='app', title='App', position=(200, 200), size=(300, 300), resizeable=False)
        self.main_window.content = Signin().box
        self.main_window.show()

def main():
    return App()
