import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ListProperty
class SpartanGrid(GridLayout):
    def __init__(self,**kwargs):
        super(SpartanGrid,self).__init__()
        self.cols=2


        background_normal_color = ListProperty([1, 1, 1, 1])
        background_hover_color = ListProperty([0.5, 0.5, 0.5, 1])
        self.add_widget(Label(text="Student Name:"))
        self.s_name = TextInput(multiline=True)
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Marks:"))
        self.s_marks=TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender:"))
        self.s_gender=TextInput()
        self.add_widget(self.s_gender)

        self.press=Button(text="View Details")
        self.press.bind(on_press=self.Click_Me)
        self.bind(on_enter=self.on_enter, on_leave=self.on_leave)
        self.add_widget(self.press)
    def Click_Me(self,instance):

        self.add_widget(Label(text="Student Name:  " +self.s_name.text ))
        self.add_widget(Label(text="Student Marks:  " + self.s_marks.text))
        self.add_widget(Label(text="Student Gender:  " +self.s_gender.text))
        self.bind(on_enter=self.on_enter, on_leave=self.on_leave)

    def on_enter(self, *args):
        self.background_color = self.background_hover_color

    def on_leave(self, *args):
        self.background_color = self.background_normal_color
class MYApp(App):
    def build(self):
        return SpartanGrid()

if __name__ =="__main__":
    MYApp().run()
