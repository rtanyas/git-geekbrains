from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

from kivy.config import Config
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

class AuthFormApp(App):

    def build(self):
        bl = BoxLayout(orientation='vertical', padding=25)
        bl1 = BoxLayout(orientation='vertical', size_hint=[1, .6], padding=25, spacing=10)

        bl1.add_widget(TextInput(text="Login"))
        bl1.add_widget(TextInput(text="Password"))

        bl2 = BoxLayout(orientation='horizontal', size_hint=[1, .2], padding=25, spacing=3)
        btn_login = Button(text="Login",
                           font_size=20, on_press=self.btn_login_press,
                           background_color=[.31, .55, .94, 1], background_normal='')
        btn_cancel = Button(text="Cancel",
                            font_size=20,
                            on_press=self.btn_cancel_press,
                            background_color=[.31, .55, .94, 1], background_normal='')
        bl2.add_widget(btn_login)
        bl2.add_widget(btn_cancel)

        bl.add_widget(bl1)
        bl.add_widget(bl2)
        return bl

    def btn_login_press(self, instance):
        instance.text = "I am pressed"
        instance.background_color = [.1, .1, .1, 1]

    def btn_cancel_press(self, instance):
        instance.text = "I am pressed"
        instance.background_color = [.1, .1, .1, 1]

if __name__ == "__main__":
    AuthFormApp().run()