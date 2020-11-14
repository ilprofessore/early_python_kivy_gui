# this is the final stable version of this series.

import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# we will be using grid layouts with this project.
class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_submit_pressed = False
        # number of columns (this is a bultin variable named cols)
        self.cols = 1
        # creating and placing widgets
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        self.med01_grid = GridLayout()
        self.med01_grid.cols = 2
        self.med02_grid = GridLayout()
        self.med02_grid.cols = 2
        self.bott_grid = GridLayout()
        self.bott_grid.cols = 2
        self.text01 = Label(text="what is your name: ")
        self.top_grid.add_widget(self.text01)
        self.field01 = TextInput(multiline=False)
        self.top_grid.add_widget(self.field01)
        self.text02 = Label(text="what is your domain: ")
        self.med01_grid.add_widget(self.text02)
        self.field02 = TextInput(multiline=False)
        self.med01_grid.add_widget(self.field02)
        self.text03 = Label(text="what is your major: ")
        self.med02_grid.add_widget(self.text03)
        self.field03 = TextInput(multiline=False)
        self.med02_grid.add_widget(self.field03)
        self.add_widget(self.top_grid)
        self.add_widget(self.med01_grid)
        self.add_widget(self.med02_grid)
        self.add_widget(self.bott_grid)
        # creating the submit button
        self.submit = Button(text="submit", font_size=32)
        # binding the button to a function
        self.submit.bind(on_press=self.button_pressed)
        # displaying the button
        self.bott_grid.add_widget(self.submit)
    # creating methods (outside of the constructor)
    @property
    def clear_field(self):
        self.field01.text = ""
        self.field02.text = ""
        self.field03.text = ""
    # the button takes self, and the instance as an argument because of the binding.
    def button_pressed(self, instance):
        # if condition ensures that the label is only added if the fields are not empty.
        if self.field01.text != "" and self.field02.text != "" and self.field03.text != "":
            # have to use a bool condition to test if the button has been pressed before or not.
            if self.is_submit_pressed:
                self.remove_widget(self.added_label)
            self.added_label = Label(text=
            "your name is {} \nand your field\\major are {}\nand {} respectively.".format(
                self.field01.text, self.field02.text, self.field03.text))
            self.add_widget(self.added_label)
            # i used format thing instead of concatenation (new experience).
            # clearing the boxes after pressing submit button:
            self.is_submit_pressed = True
            self.clear_field

# this is the build class, this makes the main window.
class PrototypeFinal(App):
    def build(self):
        return MyLayout()
# this is the main function in python.
if __name__ == '__main__':
    PrototypeFinal().run()