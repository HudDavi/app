import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class Signin:

    def __init__(self):
        self.box = toga.Box()
        self.box.style.update(direction=COLUMN, padding=5)

        self.label_email = toga.Label(text='Email', id='label-email')
        self.label_password = toga.Label(text='Password', id='label-password')

        self.input_email = toga.TextInput(id='input-email', placeholder='Email')
        self.input_password = toga.TextInput(id='input-password', placeholder='Password')

        self.button_signin = toga.Button(text='Signin', id='signin', enabled=True)

        self.box.add(self.label_email)
        self.box.add(self.input_email)
        self.box.add(self.label_password)
        self.box.add(self.input_password)
        self.box.add(self.button_signin)
