import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class Signup:

    def __init__(self):
        self.box = toga.Box()
        self.box.style.update(direction=COLUMN, padding=5)

        self.label_first_name = toga.Label(text='First Name', id='label-first-name')
        self.label_last_name = toga.Label(text='Last Name', id='label-last-name')
        self.label_email = toga.Label(text='Email', id='label-email')
        self.label_password = toga.Label(text='Password', id='label-password')

        self.input_first_name = toga.TextInput(id='input-first-name', placeholder='First Name')
        self.input_last_name = toga.TextInput(id='input-last-name', placeholder='Last Name')
        self.input_email = toga.TextInput(id='input-email', placeholder='Email')
        self.input_password = toga.TextInput(id='input-password', placeholder='Password')

        self.button_signup = toga.Button(text='Signup', id='signup', enabled=True)

        self.box.add(self.label_first_name)
        self.box.add(self.input_first_name)
        self.box.add(self.label_last_name)
        self.box.add(self.input_last_name)
        self.box.add(self.label_email)
        self.box.add(self.input_email)
        self.box.add(self.label_password)
        self.box.add(self.input_password)
        self.box.add(self.button_signup)
